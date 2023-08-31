# import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Load CPI or inflation rate data
# Data has been provided by: https://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/
data = pd.read_csv('CPI-U_1913-2022.csv')

# Add labels and title
years = data['Year']
cpi_values = data['Avg']

# Calculate the relative increase of CPI over the course of the last 110 years
relative_increase = ((cpi_values.iloc[-1] - cpi_values.iloc[0]) / cpi_values.iloc[0]) * 100

# Print the relative increase in percentage
print(f"Cost of living increased by {relative_increase:.2f}% from {years.iloc[0]} to {years.iloc[-1]}.")

# Create a bar chart to visualize the change
plt.figure(figsize=(10, 6))
plt.plot(years, cpi_values, marker='o', linestyle='-', color='blue')    
plt.xlabel('Year')
plt.ylabel('Consumer Price Index')
plt.title('Consumer Price Index for All Urban Consumers (CPI-U) from 1913 to 2022')
plt.grid(True)
plt.show()






