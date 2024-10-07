import pandas as pd
import matplotlib.pyplot as plt

# Load the data 
file_path = "D:\data science\dairy_week_sales.csv" 
df = pd.read_csv(file_path)

# Display data
print(df.head())

# Total sales
total_sales = df['Sales'].sum()
print(f"Total Sales: {total_sales} INR")

# Average transaction value 
total_transactions = 200
avg_transaction_value = total_sales / total_transactions
print(f"Average Transaction Value: {avg_transaction_value} INR")

# Sales by week
sales_by_week = df.groupby('Week')['Sales'].sum()
print("\nSales by Week:")
print(sales_by_week)

# Sales by category
sales_by_category = df.groupby('Category')['Sales'].sum()
print("\nSales by Category:")
print(sales_by_category)

# Visualize data
# Line chart for weekly sales
sales_by_week.plot(kind='line', marker='o')
plt.title('Weekly Sales Trends')
plt.xlabel('Week')
plt.ylabel('Sales (INR)')
plt.grid(True)
plt.show()

# Bar chart for sales by category
sales_by_category.plot(kind='bar')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales (INR)')
plt.show()
