# REQUIRED LIBRARIES
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#  VISUAL SETTINGS
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

#  LOAD DATA
df = pd.read_csv("cleaned-cafe-sales/data/dirty_cafe_sales.csv")

#  PREVIEW DATA
print("First 5 Rows:\n", df.head())

#  CLEAN TEXT DATA: lowercase & strip whitespace
df_obj = df.select_dtypes(include='object')
df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip().str.lower())

#  REPLACE DIRTY STRINGS WITH NaN
df.replace(['unknown', 'n/a', 'error', 'null', 'nan'], np.nan, inplace=True)

#  CONVERT DATA TYPES
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

#  DUPLICATE CHECK
duplicates = df[df.duplicated()]
print(f"\n Duplicate rows found: {duplicates.shape[0]}")

#  MISSING VALUE CHECK
print("\nMissing Values:\n", df.isnull().sum())

#  DROP ROWS WITH MISSING VALUES
df.dropna(inplace=True)

# TIME FEATURES
df['Month'] = df['Transaction Date'].dt.to_period('M')
df['Weekday'] = df['Transaction Date'].dt.day_name()



#  1. PAYMENT METHOD PIE CHART
df['Payment Method'].value_counts().plot.pie(
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.show()

#  2. TOP SELLING ITEMS BAR CHART
top_items = df['Item'].value_counts().nlargest(10)
sns.barplot(
    x=top_items.values,
    y=top_items.index,
    hue=top_items.index,
    palette="magma",
    legend=False
)
plt.title("Top 10 Selling Items")
plt.xlabel("Sales Count")
plt.ylabel("Item")
plt.show()

#  3. MONTHLY SALES TREND
monthly_sales = df.groupby('Month')['Total Spent'].sum()
monthly_sales.plot(kind='line', marker='o', color='coral')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.grid(True)
plt.show()

#  4. WEEKDAY SALES ANALYSIS
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_sales_df = (
    df.groupby('Weekday')['Total Spent']
    .sum()
    .reindex(weekday_order)
    .reset_index()
)

sns.barplot(
    data=weekday_sales_df,
    x='Weekday',
    y='Total Spent',
    hue='Weekday',
    palette="viridis",
    legend=False 
)
plt.title("Revenue by Weekday")
plt.xlabel("Weekday")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.show()


#  5. SALES BY LOCATION TYPE (Takeaway vs In-store)
location_stats = df.groupby('Location').agg({
    'Quantity': 'sum',
    'Total Spent': 'sum',
    'Transaction ID': 'count'
}).rename(columns={'Transaction ID': 'Transaction Count'})

location_stats_reset = location_stats.reset_index()

sns.barplot(
    data=location_stats_reset,
    x='Location',
    y='Total Spent',
    hue='Location',
    palette="Set2",
    legend=False
)
plt.title("Total Revenue by Location Type")
plt.xlabel("Location")
plt.ylabel("Revenue")
plt.show()
