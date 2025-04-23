import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Load the CSV file using pandas
file_path = "sales_data.csv" #path to your CSV file
df = pd.read_csv(file_path) #load the CSV into a DataFrame

#Convert The_Date column to datetime for time-based analysis
df['The_Date'] = pd.to_datetime(df['The_Date'])

#Calculate the total revenue
total_revenue = df['Revenue_in_$'].sum()

#Find the best selling product (based on total Quantity_sold)
product_sales = df.groupby('Product')['Quantity_sold'].sum()
best_selling_product = product_sales.idxmax() #product with max sales
quantity_of_best_selling_product = product_sales.max()

#Identify the day with the highest sales
daily_revenue = df.groupby('The_Date')['Revenue_in_$'].sum()
highest_selling_day = daily_revenue.idxmax() #date with the highest sales
highest_sales_amount = daily_revenue.max() #revenue on that day

#Save the summary to sales_summary.txt
summary_text = f""" 
Sales Summary Report
------------------
Total Revenue = {total_revenue}
Best Selling Product = {best_selling_product}
Total Units sold = {quantity_of_best_selling_product}
Day with the highest sales = {highest_selling_day.date()}
Sales on that day = {highest_sales_amount}
"""
#Write the summary to a text file
with open("sales_summary.txt","w") as file:
    print(file.write(summary_text))

#Visualize sales trends using seaborn

#Set seaborn style
sns.set(style = 'whitegrid')

#Prepare daily revenue data for plotting
daily_sales = daily_revenue.reset_index()

#Create a line plot to show revenue trends over years
plt.figure(figsize =(10,6)) # set figure size
sns.lineplot(data = daily_sales, x = "The_Date", y = "Revenue_in_$", marker = 'o')

#Add labels and title
plt.title('Daily Revenue trends',fontsize = 14)
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation = 45) #rotate the x-axis labels for readability

#Make the layout tight and show the plot
plt.tight_layout()
plt.show()
