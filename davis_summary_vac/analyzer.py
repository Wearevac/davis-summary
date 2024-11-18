import csv
import statistics
import math
import base64
from io import BytesIO
import argparse

def analyze_csv(file_path):
    data = []
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return data

def generate_summary(data):
    summary = {}
    
    if not data:
        return summary
    
    for column in data[0].keys():
        numeric_values = []
        non_numeric_values = []
        
        for row in data:
            try:
                value = float(row[column])
                numeric_values.append(value)
            except (ValueError, TypeError):
                if row[column].strip():
                    non_numeric_values.append(row[column])
        
        if numeric_values:
            summary[column] = {
                'count': len(numeric_values),
                'min': min(numeric_values),
                'max': max(numeric_values),
                'mean': statistics.mean(numeric_values),
                'median': statistics.median(numeric_values),
                'range': max(numeric_values) - min(numeric_values),
                'variance': statistics.variance(numeric_values) if len(numeric_values) > 1 else 0,
                'standard_deviation': statistics.stdev(numeric_values) if len(numeric_values) > 1 else 0,
                'quartiles': {
                    'Q1': statistics.quantiles(numeric_values)[0],
                    'Q3': statistics.quantiles(numeric_values)[2]
                },
                'iqr': statistics.quantiles(numeric_values)[2] - statistics.quantiles(numeric_values)[0],
                'potential_outliers': detect_outliers(numeric_values)
            }
        
        if non_numeric_values:
            if column not in summary:
                summary[column] = {}
            summary[column]['unique_values'] = list(set(non_numeric_values))
            summary[column]['value_counts'] = count_values(non_numeric_values)

    return summary

def detect_outliers(values, method='iqr'):
    if len(values) < 4:
        return []
    
    q1 = statistics.quantiles(values)[0]
    q3 = statistics.quantiles(values)[2]
    iqr = q3 - q1
    
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    
    outliers = [v for v in values if v < lower_bound or v > upper_bound]
    return outliers

def count_values(values):
    value_counts = {}
    for value in values:
        value_counts[value] = value_counts.get(value, 0) + 1
    
    return dict(sorted(value_counts.items(), key=lambda x: x[1], reverse=True))

def generate_html_report(data, summary):
    html = """
    <html>
    <head>
        <title>Comprehensive CSV Analysis Report</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                max-width: 1200px; 
                margin: 0 auto; 
                padding: 20px; 
                display: flex;
                flex-direction: column;
                min-height: 100vh;
            }
            table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            .section { margin-bottom: 30px; }
            h1, h2 { color: #333; }
            .content { flex: 1 0 auto; }
            .footer {
                flex-shrink: 0;
                text-align: center;
                padding: 20px;
                background-color: #f2f2f2;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>Descriptive Summary Report</h1>
    """

    # Numeric Columns Summary
    html += "<div class='section'><h2>Numeric Columns Summary</h2>"
    html += "<table><tr><th>Column</th><th>Count</th><th>Min</th><th>Max</th><th>Mean</th><th>Median</th><th>Std Dev</th><th>Outliers</th></tr>"
    
    for column, stats in summary.items():
        if 'mean' in stats:
            outliers = stats.get('potential_outliers', [])
            html += f"""
            <tr>
                <td>{column}</td>
                <td>{stats['count']}</td>
                <td>{stats['min']:.2f}</td>
                <td>{stats['max']:.2f}</td>
                <td>{stats['mean']:.2f}</td>
                <td>{stats['median']:.2f}</td>
                <td>{stats.get('standard_deviation', 0):.2f}</td>
                <td>{len(outliers)}</td>
            </tr>
            """
    html += "</table></div>"

    # Non-Numeric Columns Summary
    html += "<div class='section'><h2>Non-Numeric Columns Summary</h2>"
    html += "<table><tr><th>Column</th><th>Unique Values</th><th>Top Values</th></tr>"
    
    for column, stats in summary.items():
        if 'unique_values' in stats:
            unique_values = stats['unique_values']
            top_values = list(stats.get('value_counts', {}).items())[:5]
            html += f"""
            <tr>
                <td>{column}</td>
                <td>{len(unique_values)}</td>
                <td>{', '.join([f"{val} ({count})" for val, count in top_values])}</td>
            </tr>
            """
    html += "</table></div>"

    html += """
        </div>
        <div class="footer">
            <p>Developed by <a href="https://wearevac.github.io/wearevac/" target="_blank">Visionary Arts Company</a></p>
            <p>We are improving day by day. Stay connected. Enjoy!</P>
        </div>
    </body>
    </html>
    """

    return html

def main(csv_file_path, output_html_path):
    data = analyze_csv(csv_file_path)
    if not data:
        print(f"No data to analyze. Please check your CSV file: {csv_file_path}")
        return

    summary = generate_summary(data)
    html_report = generate_html_report(data, summary)

    try:
        with open(output_html_path, 'w', encoding='utf-8') as f:
            f.write(html_report)
        print(f"Analysis complete. Report saved to {output_html_path}")
    except Exception as e:
        print(f"Error writing HTML report: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze a CSV file and generate an HTML report.")
    parser.add_argument("csv_file", help="Path to the CSV file to analyze")
    parser.add_argument("--output", default="analysis_report.html", help="Path for the output HTML report")
    args = parser.parse_args()

    main(args.csv_file, args.output)