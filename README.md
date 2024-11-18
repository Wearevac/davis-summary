# **Davis Summary VAC** 📊✨
**A comprehensive tool for CSV analysis with automated HTML reporting.**

[![PyPI version](https://badge.fury.io/py/davis-summary-vac.svg)](https://badge.fury.io/py/davis-summary-vac)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)

## **Overview**
- `davis-summary-vac` is a light weight Python package that analyzes CSV files and generates a detailed HTML report.
- It offers a summary of both numeric and non-numeric columns, detecting potential outliers and providing insights into your data. Whether you're a data scientist, analyst, or just someone exploring data, this tool simplifies the analysis process and presents it in a visually appealing format.

---

## **Features** 🌟
- 📊 **Detailed summary of numeric columns**:
  - Count, Minimum, Maximum, Mean, Median, Standard Deviation
  - Variance, Quartiles, Interquartile Range (IQR)
  - Detection of potential outliers
- 🛠️ **Analysis of non-numeric columns**:
  - Unique values
  - Value counts of the top items
- 🖥️ **Automatically generates a structured HTML report** with tables and highlights.
- 📝 **User-friendly interface** for quick and easy CSV file analysis.

---

## **Installation** 🚀
Ensure you have Python 3.6 or higher installed. Then, use `pip` to install the package:

```bash
pip install davis-summary-vac
```

---
## **Usage** 🖥️
To analyze a CSV file and generate an HTML report, run the following command:

```bash
davis-summary-vac <path_to_your_csv_file> --output <output_html_file>
Arguments:
<path_to_your_csv_file>: The path to the CSV file you want to analyze.
--output (optional): The path to save the generated HTML report. Default is analysis_report.html.
```
Example:
```bash
davis-summary-vac data.csv --output my_report.html
```
Output Example 📄
After running the command, an HTML report will be generated containing:

Numeric Columns Summary: Statistical metrics like mean, median, standard deviation, and outlier detection.
Non-Numeric Columns Summary: Unique value counts and the top frequent items.
Here's a sample snapshot of what the generated report looks like:

API Usage (In Python Scripts)
If you'd like to use this package programmatically within a Python script:

```python

from davis_summary_vac import analyze_csv, generate_summary, generate_html_report

data = analyze_csv('data.csv')
summary = generate_summary(data)
html_report = generate_html_report(data, summary)

with open('output.html', 'w') as file:
    file.write(html_report)
    
```
## **Dependencies** 📦
- Python 3.6+
- csv
- statistics
- math
- base64
- argparse
- All dependencies are included with Python's standard library, making it lightweight and easy to use.

## **Contributing** 🤝
We welcome contributions to improve this package! If you find a bug or have suggestions for new features:

## **Fork the repository.**
- Create a new branch (feature/my-feature).
- Commit your changes.
- Push to the branch.
- Open a Pull Request.

## **License** 📄
This project is licensed under the MIT License - see the LICENSE file for details.

## **Author** ✍️
- Developed by the **Visionary Arts Company (VAC)**.  
- Stay connected and explore more at [wearevac.github.io](https://wearevac.github.io/wearevac/).  
If you enjoyed this package, please give it a ⭐ on [GitHub](https://github.com/Wearevac/davis-summary)!


## **Support** 💬
If you have any questions, issues, or suggestions, please feel free to reach out by opening an issue on the GitHub repository or by contacting us directly via the website.

Happy Analyzing! 📊🎉