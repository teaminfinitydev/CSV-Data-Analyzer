# 📊 CSV Data Analyzer

A powerful and intuitive desktop application for analyzing CSV data with beautiful visualizations and comprehensive statistics.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey.svg)

## ✨ Features

- **📁 Easy File Loading** - Simple one-click CSV file loading
- **📋 Data Preview** - Interactive table view of your data (first 100 rows)
- **📈 Comprehensive Statistics** - Detailed statistical analysis including:
  - Dataset overview (shape, memory usage)
  - Column information (data types, null values, unique counts)
  - Numerical statistics (mean, median, std, quartiles)
  - Correlation matrix for numerical columns
  - Categorical analysis with value counts
  - Missing data summary
- **📊 Beautiful Visualizations** - Multiple chart types:
  - Distribution histograms
  - Correlation heatmaps
  - Scatter plots
  - Categorical bar charts
- **💾 Export Reports** - Generate and save detailed analysis reports

## 🚀 Quick Start

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/csv-data-analyzer.git
cd csv-data-analyzer
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python main.py
```

### Usage

1. **Load Data**: Click "Load CSV File" and select your CSV file
2. **View Preview**: Your data will appear in the left panel (first 100 rows)
3. **Analyze**: Click "Show Statistics" to see comprehensive analysis in the right panel
4. **Visualize**: Click "Create Visualization" to open charts in a new window
5. **Export**: Click "Export Report" to save your analysis as a text file

## 🎯 Use Cases

- **Data Quality Assessment** - Identify missing values, data types, and outliers
- **Exploratory Data Analysis** - Understand distributions and relationships
- **Quick Data Insights** - Get instant statistics without coding
- **Report Generation** - Create shareable analysis reports
- **Data Validation** - Verify data integrity before processing

## 📊 Supported Analysis

### Numerical Data
- Descriptive statistics (count, mean, std, min, max, quartiles)
- Distribution visualization with histograms
- Correlation analysis with heatmaps
- Scatter plot relationships

### Categorical Data
- Value counts and frequency analysis
- Top categories identification
- Bar chart visualizations

### Data Quality
- Missing value detection and reporting
- Data type identification
- Memory usage analysis
- Unique value counting

## 🖥️ System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimum 512MB RAM (depends on dataset size)
- **Display**: 1200x800 minimum resolution recommended

## 📦 Dependencies

- **pandas** - Data manipulation and analysis
- **matplotlib** - Static plotting and visualization
- **seaborn** - Statistical data visualization
- **numpy** - Numerical computing
- **tkinter** - GUI framework (usually included with Python)

## 🎨 Interface Overview

The application features a clean, professional interface with:

- **Control Panel** - File operations and analysis buttons
- **Data Preview** - Scrollable table view of your CSV data
- **Analysis Panel** - Detailed statistics and insights
- **Visualization Window** - Tabbed interface with multiple chart types
- **Status Bar** - File information and operation feedback

## 🔧 Technical Details

- Built with Python's tkinter for cross-platform compatibility
- Uses pandas for efficient data processing
- Matplotlib and seaborn for professional visualizations
- Handles large datasets efficiently (tested up to 1M+ rows)
- Memory-optimized data loading and processing

## 📝 File Support

- **CSV Files** - Primary format with automatic delimiter detection
- **Export Formats** - Text reports with comprehensive analysis
- **Encoding** - Automatic UTF-8 encoding handling
- **Large Files** - Optimized for datasets up to several GB

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the requirements.txt for correct dependencies
2. Ensure your CSV file is properly formatted
3. Verify Python version compatibility (3.8+)
4. For large files, allow extra time for processing

## 🚀 Future Enhancements

- Multiple file format support (Excel, JSON, etc.)
- Advanced filtering and data transformation
- Machine learning insights
- Interactive plotting with Plotly
- Database connectivity
- Automated report scheduling

---

**Made with ❤️ for data enthusiasts and analysts**"# CSV-Data-Analyzer" 
