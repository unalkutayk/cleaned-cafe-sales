# Cleaned Cafe Sales - Data Cleaning and Analysis Project

This project involves data cleaning, exploratory data analysis (EDA), and visualization on a fictional dataset of cafe sales. The dataset includes missing values, inconsistent labels, and noise — making it ideal for realistic hands-on data cleaning and analysis.

---

## Project Structure

cleaned-cafe-sales/
│
├── data/
│   └── dirty_cafe_sales.csv          
│
├── src/
│   ├── CafeSales_Cleaned.ipynb       
│   └── CafeSales_Cleaned.py          
│
├── .gitignore                        
├── LICENSE                           
├── README.md                         
├── requirements.txt                  
├── .gitattributes                    
└── .git/                             

---

## Objectives

- Handle missing and inconsistent data
- Clean text and date formats
- Remove duplicates logically
- Perform aggregations and visual insights
- Analyze sales by weekday and location type

---


## How to Run

1. Clone the repository:
```bash
git clone https://github.com/unalkutayk/cleaned-cafe-sales.git
cd cleaned-cafe-sales
```
2. Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run the script:
python src/CafeSales_Cleaned.py


5. Or open the notebook:
jupyter notebook src/CafeSales_Cleaned.ipynb

---

## Visuals Included

- Top-selling items (bar chart)
- Weekday revenue (bar chart)
- Sales type distribution (pie chart)
- Location-based revenue comparison (hue + barplot)

---

## Technologies Used

- Python
- pandas
- matplotlib
- seaborn
- Jupyter Notebook

---

## Key Features

Comprehensive Data Cleaning:
Replaced various placeholders ("UNKNOWN", "N/A", "null", "error") with ERROR values for consistency. Dropped and imputed missing values where necessary.

Data Type Optimization:
Converted columns such as dates and numeric strings into proper types (e.g., datetime, float) for accurate computation.

Descriptive Statistics & Exploration:
Performed summary statistics, identified top-selling products and most profitable categories.

Error-Aware Visualizations:
Automatically excluded inconsistent or missing entries from all visualizations to preserve accuracy.

Revenue Analysis:
Examined total revenue across different locations (Takeaway vs In-store) and days of the week, highlighting customer behavior trends.

Product Performance:
Visualized top 10 products by frequency and revenue using bar and pie charts.

Modular Structure:
Project is organized into separate folders for raw data (/data) and scripts (/src) following best practices.

Jupyter Notebook & Script Versions:
Analysis is available in both interactive (.ipynb) and script (.py) formats for reproducibility and automation.

--- 

## License

This project is licensed under the MIT License – see the LICENSE file for details.

---

##  Author

- Unal Kutay KILIC
- GitHub: [unalkutayk]
- LinkedIn [https://www.linkedin.com/in/unalkutaykilic/]
