import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import numpy as np
from pathlib import Path

class CSVAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Data Analyzer")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        self.df = None
        self.setup_ui()
        
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        title_label = ttk.Label(main_frame, text="CSV Data Analyzer", 
                               font=('Arial', 20, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        control_frame = ttk.LabelFrame(main_frame, text="Controls", padding="10")
        control_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Button(control_frame, text="Load CSV File", 
                  command=self.load_file).grid(row=0, column=0, padx=(0, 10))
        
        ttk.Button(control_frame, text="Show Statistics", 
                  command=self.show_statistics).grid(row=0, column=1, padx=(0, 10))
        
        ttk.Button(control_frame, text="Create Visualization", 
                  command=self.create_visualization).grid(row=0, column=2, padx=(0, 10))
        
        ttk.Button(control_frame, text="Export Report", 
                  command=self.export_report).grid(row=0, column=3)
        
        content_frame = ttk.Frame(main_frame)
        content_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        content_frame.columnconfigure(0, weight=1)
        content_frame.columnconfigure(1, weight=1)
        content_frame.rowconfigure(0, weight=1)
        
        data_frame = ttk.LabelFrame(content_frame, text="Data Preview", padding="5")
        data_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))
        data_frame.columnconfigure(0, weight=1)
        data_frame.rowconfigure(0, weight=1)
        
        self.tree = ttk.Treeview(data_frame)
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        tree_scroll = ttk.Scrollbar(data_frame, orient="vertical", command=self.tree.yview)
        tree_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=tree_scroll.set)
        
        analysis_frame = ttk.LabelFrame(content_frame, text="Analysis Results", padding="5")
        analysis_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(5, 0))
        analysis_frame.columnconfigure(0, weight=1)
        analysis_frame.rowconfigure(0, weight=1)
        
        self.analysis_text = tk.Text(analysis_frame, wrap=tk.WORD, font=('Consolas', 10))
        self.analysis_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        analysis_scroll = ttk.Scrollbar(analysis_frame, orient="vertical", 
                                      command=self.analysis_text.yview)
        analysis_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.analysis_text.configure(yscrollcommand=analysis_scroll.set)
        
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
        self.status_label = ttk.Label(status_frame, text="Ready - Load a CSV file to begin")
        self.status_label.grid(row=0, column=0, sticky=tk.W)
        
    def load_file(self):
        file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                self.display_data()
                self.status_label.config(text=f"Loaded: {Path(file_path).name} - {len(self.df)} rows, {len(self.df.columns)} columns")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {str(e)}")
                
    def display_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        if self.df is not None:
            self.tree["columns"] = list(self.df.columns)
            self.tree["show"] = "headings"
            
            for col in self.df.columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=100, anchor=tk.CENTER)
            
            for index, row in self.df.head(100).iterrows():
                self.tree.insert("", "end", values=list(row))
                
    def show_statistics(self):
        if self.df is None:
            messagebox.showwarning("Warning", "Please load a CSV file first")
            return
            
        self.analysis_text.delete(1.0, tk.END)
        
        stats_text = "=== DATASET OVERVIEW ===\n"
        stats_text += f"Shape: {self.df.shape[0]} rows × {self.df.shape[1]} columns\n"
        stats_text += f"Memory usage: {self.df.memory_usage(deep=True).sum() / 1024:.2f} KB\n\n"
        
        stats_text += "=== COLUMN INFORMATION ===\n"
        for col in self.df.columns:
            dtype = str(self.df[col].dtype)
            null_count = self.df[col].isnull().sum()
            unique_count = self.df[col].nunique()
            stats_text += f"{col}:\n"
            stats_text += f"  Type: {dtype}\n"
            stats_text += f"  Non-null: {len(self.df) - null_count}\n"
            stats_text += f"  Unique values: {unique_count}\n\n"
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            stats_text += "=== NUMERICAL STATISTICS ===\n"
            desc = self.df[numeric_cols].describe()
            stats_text += desc.to_string() + "\n\n"
            
            stats_text += "=== CORRELATION MATRIX ===\n"
            if len(numeric_cols) > 1:
                corr = self.df[numeric_cols].corr()
                stats_text += corr.to_string() + "\n\n"
        
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            stats_text += "=== CATEGORICAL ANALYSIS ===\n"
            for col in categorical_cols[:5]:
                stats_text += f"\n{col} - Top 5 values:\n"
                value_counts = self.df[col].value_counts().head()
                stats_text += value_counts.to_string() + "\n"
        
        missing_data = self.df.isnull().sum()
        if missing_data.sum() > 0:
            stats_text += "\n=== MISSING DATA ===\n"
            stats_text += missing_data[missing_data > 0].to_string() + "\n"
        
        self.analysis_text.insert(1.0, stats_text)
        
    def create_visualization(self):
        if self.df is None:
            messagebox.showwarning("Warning", "Please load a CSV file first")
            return
            
        viz_window = tk.Toplevel(self.root)
        viz_window.title("Data Visualization")
        viz_window.geometry("1000x700")
        
        notebook = ttk.Notebook(viz_window)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) > 0:
            self.create_distribution_plots(notebook, numeric_cols)
            
            if len(numeric_cols) > 1:
                self.create_correlation_heatmap(notebook, numeric_cols)
                self.create_scatter_plots(notebook, numeric_cols)
        
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            self.create_categorical_plots(notebook, categorical_cols)
            
    def create_distribution_plots(self, notebook, numeric_cols):
        dist_frame = ttk.Frame(notebook)
        notebook.add(dist_frame, text="Distributions")
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle('Numeric Column Distributions', fontsize=16)
        axes = axes.flatten()
        
        for i, col in enumerate(numeric_cols[:4]):
            if i < len(axes):
                self.df[col].hist(bins=30, ax=axes[i], alpha=0.7, color='skyblue', edgecolor='black')
                axes[i].set_title(f'{col}')
                axes[i].set_xlabel('Value')
                axes[i].set_ylabel('Frequency')
        
        for i in range(len(numeric_cols), len(axes)):
            axes[i].remove()
            
        plt.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, dist_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def create_correlation_heatmap(self, notebook, numeric_cols):
        corr_frame = ttk.Frame(notebook)
        notebook.add(corr_frame, text="Correlation")
        
        fig, ax = plt.subplots(figsize=(10, 8))
        correlation_matrix = self.df[numeric_cols].corr()
        
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
                   square=True, ax=ax, fmt='.2f')
        ax.set_title('Correlation Matrix', fontsize=16)
        
        plt.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, corr_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def create_scatter_plots(self, notebook, numeric_cols):
        scatter_frame = ttk.Frame(notebook)
        notebook.add(scatter_frame, text="Scatter Plots")
        
        if len(numeric_cols) >= 2:
            fig, ax = plt.subplots(figsize=(10, 8))
            
            x_col = numeric_cols[0]
            y_col = numeric_cols[1]
            
            ax.scatter(self.df[x_col], self.df[y_col], alpha=0.6, c='coral', edgecolors='black')
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title(f'{x_col} vs {y_col}')
            ax.grid(True, alpha=0.3)
            
            plt.tight_layout()
            
            canvas = FigureCanvasTkAgg(fig, scatter_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
    def create_categorical_plots(self, notebook, categorical_cols):
        cat_frame = ttk.Frame(notebook)
        notebook.add(cat_frame, text="Categories")
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle('Categorical Column Distributions', fontsize=16)
        axes = axes.flatten()
        
        for i, col in enumerate(categorical_cols[:4]):
            if i < len(axes):
                value_counts = self.df[col].value_counts().head(10)
                value_counts.plot(kind='bar', ax=axes[i], color='lightgreen', edgecolor='black')
                axes[i].set_title(f'{col}')
                axes[i].set_xlabel('Categories')
                axes[i].set_ylabel('Count')
                axes[i].tick_params(axis='x', rotation=45)
        
        for i in range(len(categorical_cols), len(axes)):
            axes[i].remove()
            
        plt.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, cat_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def export_report(self):
        if self.df is None:
            messagebox.showwarning("Warning", "Please load a CSV file first")
            return
            
        file_path = filedialog.asksaveasfilename(
            title="Save Report",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write("CSV DATA ANALYSIS REPORT\n")
                    f.write("=" * 50 + "\n\n")
                    
                    f.write(f"Dataset Shape: {self.df.shape[0]} rows × {self.df.shape[1]} columns\n\n")
                    
                    f.write("COLUMN SUMMARY:\n")
                    f.write("-" * 20 + "\n")
                    for col in self.df.columns:
                        f.write(f"{col}: {self.df[col].dtype}, {self.df[col].isnull().sum()} nulls\n")
                    
                    numeric_cols = self.df.select_dtypes(include=[np.number]).columns
                    if len(numeric_cols) > 0:
                        f.write("\nNUMERICAL STATISTICS:\n")
                        f.write("-" * 20 + "\n")
                        f.write(self.df[numeric_cols].describe().to_string())
                        f.write("\n\n")
                    
                    f.write("MISSING DATA SUMMARY:\n")
                    f.write("-" * 20 + "\n")
                    missing = self.df.isnull().sum()
                    f.write(missing[missing > 0].to_string())
                    
                messagebox.showinfo("Success", f"Report exported to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export report: {str(e)}")

def main():
    root = tk.Tk()
    app = CSVAnalyzer(root)
    root.mainloop()

if __name__ == "__main__":
    main()