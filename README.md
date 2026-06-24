# Sales Data Analysis using Python

## Project Overview

This project analyzes company sales data to identify business trends, top-performing employees, department-wise performance, and profit distribution across cities.

The analysis was performed using Python libraries such as Pandas, Matplotlib, and Seaborn.

## Objectives

* Analyze total sales and average profit.
* Identify top-performing employees.
* Compare department-wise sales performance.
* Analyze city-wise profit distribution.
* Visualize business data using charts.

## Tools and Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

## Dataset Columns

* Employee
* Department
* City
* Sales
* Profit

## Analysis Performed

### 1. Dataset Exploration

The following functions were used to understand the dataset:

* `head()`
* `info()`
* `describe()`

### 2. Business Analysis

* Calculated total sales.
* Calculated average profit.
* Identified the employee with the highest sales.
* Found department-wise average sales.
* Found city-wise total profit.

### 3. Data Visualization

The following visualizations were created:

* Bar Chart: Average Sales by Department
* Histogram: Sales Distribution
* Heatmap: Correlation between Sales and Profit

## Visualizations

### Average Sales by Department

![Department Average Sales](Depart_avg.png)

### Sales Distribution

![Sales Distribution](Distribution.png)

### Correlation Heatmap

![Correlation Heatmap](heatmap.png)

## Key Insights

* The Sales department generated the highest average sales.
* Rohan achieved the highest sales among all employees.
* Pune generated the highest total profit.
* Sales and Profit showed a strong positive correlation.
* The Sales department outperformed other departments in terms of average sales.

## Project Structure

```text
sales-data-analysis/
│
├── sales_data.csv
├── main.py
├── Depart_avg.png
├── Distribution.png
├── heatmap.png
└── README.md
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Shindemukesh17/sales-data-analysis.git
```

### 2. Navigate to the project folder

```bash
cd sales-data-analysis
```

### 3. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### 4. Run the project

```bash
python main.py
```

## Future Improvements

* Add more records for deeper analysis.
* Create interactive dashboards using Power BI.
* Perform advanced exploratory data analysis (EDA).
* Add interactive visualizations.

## Author

**Mukesh Shinde**
Aspiring Data Analyst | Python | SQL | Excel | Power BI
