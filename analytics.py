import pandas as pd
import matplotlib.pyplot as plt

# Load the data 
file_path = 'D:\\data science\\dairy_store_sales.csv'
df = pd.read_csv(file_path)


df.rename(columns={'Catagory': 'Category'}, inplace=True)

# Display the data
print(df.head())

# Total sales
total_sales = df['Sales'].sum()
print(f"Total Sales: {total_sales} INR")

# Average transaction value 
total_transactions = 200  
avg_transaction_value = total_sales / total_transactions
print(f"Average Transaction Value: {avg_transaction_value} INR")

# Sales by category
sales_by_category = df.groupby('Category').sum()
print("\nSales by Category:")
print(sales_by_category)

# Visualize data 
# Pie chart for sales by category
sales_by_category.plot(kind='pie', y='Sales', autopct='%1.1f%%')
plt.title('Sales by Category')
plt.ylabel('')
plt.show()

# Bar chart for sales by category
sales_by_category.plot(kind='bar', y='Sales')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales (INR)')
plt.show()
