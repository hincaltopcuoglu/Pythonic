import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
1. Basic Plotting
Exercise 1.1: Create a simple line plot.
'''

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8,4))

plt.plot(x,y,label='sin(x)')

# add labels and title
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Simple Sine Wawe')

# add legend
plt.legend()

# add grid
plt.grid()

#show the plot
plt.show()

################################################################

'''
2. Multiple Plots
Exercise 2.1: Create a figure with multiple subplots.
'''

# create a figure with 2 rows and 2 columns
fig, axes  = plt.subplots(2,2,figsize=(10,8))

# plot on the first plot (top-left)

axes[0,0].plot(x,np.sin(x))
axes[0,0].set_title('Sine')

# plot on hte second subplot (top-right)
axes[0,1].plot(x,np.cos(x), 'g-')
axes[0,1].set_title('Cosine')

# plot on the third subplot (bottom-left)
axes[1,0].plot(x, np.sin(x)*np.cos(x),'r-')
axes[1,0].set_title('Sine * Cosine')

# plot on the fourth plot (bottom-right)
axes[1,1].plot(x, np.sin(x) + np.cos(x), 'k-')
axes[1,1].set_title('Sine + Cosine')

# adjust layout
plt.tight_layout()

# show the plot
plt.show()


################################################################

'''
Problem 1: Data Visualization with Matplotlib
You are given a dataset of monthly sales data for a company over the past 3 years:
'''

# create sample data
np.random.seed(42)

# generate dates for 3 years of montly data
dates = pd.date_range(start='2020-01-01', end='2022-12-31', freq='ME')

# generate sales data with seasonal pattern and upward trend
base = 1000
trend = np.linspace(0,500,len(dates)) #upward trend
seasonal = 200 * np.sin(np.arange(len(dates))) * (2 * np.pi / 12) # seasonal pattern
noise = np.random.normal(0, 50, len(dates)) #random noise

sales = base + trend + seasonal + noise

# create data frame
sales_df =  pd.DataFrame({
    'date': dates,
    'sales': sales,
    'year': dates.year,
    'month': dates.month
})

# cover the basics and then move to more advanced visualizations.

################################################################

'''
Let's start with a practical problem to apply these concepts:

Problem 1: Data Visualization with Matplotlib
You are given a dataset of monthly sales data for a company over the past 3 years:
'''

# Tasks:

# Create a line plot of monthly sales over time
# Create a bar chart comparing total sales by year
# Create a box plot showing the distribution of monthly sales for each year
# Create a histogram of all sales values
# Create a scatter plot of month vs. sales with different colors for each year

# 1-) Create a line plot of monthly sales over time


plt.figure(figsize=(8,4))

plt.plot(sales_df['date'], sales_df['sales'], marker='o', linestyle='-', markersize=4)

plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Montly Sales Over Time (2020-2022)')


plt.grid(True)

plt.tight_layout()

plt.show()



# 2-) Create a bar chart comparing total sales by year

sales_year = sales_df.groupby('year')['sales'].sum().reset_index()

plt.figure(figsize=(10,6))

# use plt.bar() to create bar chart
plt.bar(sales_year['year'],sales_year['sales'], color='skyblue', width=0.6)

#plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.title('Total Sales by Year')

# add text labels on top of each bar
for i ,value in enumerate(sales_year['sales']):
    plt.text(sales_year['year'][i], value + 500, f'{int(value):,}', ha='center', va='bottom')


# customize x-axis ticks
plt.xticks(sales_year['year'])

# add grid for the y-axis only
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()



# 3-)Create a box plot showing the distribution of monthly sales for each year

plt.figure(figsize=(10,6))

# create the box plot
# the boxplot function takes a list of data arrays and labes
boxplot = plt.boxplot(
    [sales_df[sales_df['year']==2000]['sales'],
     sales_df[sales_df['year']==2021]['sales'],
     sales_df[sales_df['year']==2022]['sales']],
    labels = ['2020','2021','2022'],
    patch_artist=True # fill boxes with color
)

# customize box colors
colors = ['lightblue','lightgreen','salmon']
for box, color in zip(boxplot['boxes'],colors):
    box.set(facecolor=color)

# add labels and title
plt.xlabel('Year')
plt.ylabel('Monthly Sales')
plt.title('Distribution of Monthly Sales by Year') 

# add a grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()




# 4-) Create a histogram of all sales values
# Histograms are great for visualizing the distribution of a single variable.

plt.figure(figsize=(10,6))

# create the histogram
plt.hist(sales_df['sales'], bins=15, color='skyblue', edgecolor='black', alpha=0.7)

# add labels
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.title('Distribution of Monthly Sales (2020-2022)')

plt.grid(axis='y', linestyle='--', alpha=0.7)

# add vertical line for mean and median
plt.axvline(sales_df['sales'].mean(), color='red', linestyle='--', linewidth=2,
            label=f"Mean: {sales_df['sales'].mean(): .0f}")
plt.axvline(sales_df['sales'].median(), color='green', linestyle='-', linewidth=2,
            label=f"Median: {sales_df['sales'].median(): .0f}")

# add legend
plt.legend()
plt.tight_layout()
plt.show()



# 5-) Create a scatter plot of month vs. sales with different colors for each year

# Simplest approach - plot each year separately
plt.figure(figsize=(12, 6))

# 2020 data
data_2020 = sales_df[sales_df['date'].dt.year == 2020]
plt.scatter(data_2020['month'], data_2020['sales'], color='blue', alpha=0.7, label='2020', s=80)

# 2021 data
data_2021 = sales_df[sales_df['date'].dt.year == 2021]
plt.scatter(data_2021['month'], data_2021['sales'], color='green', alpha=0.7, label='2021', s=80)

# 2022 data
data_2022 = sales_df[sales_df['date'].dt.year == 2022]
plt.scatter(data_2022['month'], data_2022['sales'], color='red', alpha=0.7, label='2022', s=80)

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales by Year')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Year')
plt.tight_layout()
plt.show()