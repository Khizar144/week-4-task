# Q.1:Import libraries (Numpy, pandas, matplotlib, plotly and seaborn) and then read csv file.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly as pt
import seaborn as sn

# read csv
df=pd.read_csv("D:/EDA internship/menu.csv")
with pd.option_context('display.max_columns', None):
    print(df.describe(include='all'))

# calculate max values
attributes = ['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars', 'Protein',
              'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)', 'Calcium (% Daily Value)',
              'Iron (% Daily Value)']

max_values = df[attributes].max()
print("Maximum values:")
print(max_values)

# : Check to see if infact there is any correlation between Calories and other independent variables by
# plotting a correlation matrix next

# Select only numeric columns
numeric_df = df.select_dtypes(include=['number'])
# calculte correlation
correlation_matrix = numeric_df.corr()
plt.title('Correlation Matrix')

plt.figure(figsize=(12,8))


# heat map
sn.heatmap(correlation_matrix, cmap='coolwarm',fmt=".2f")
plt.show()

# : Draw boxplot for Calories vs Category to spot outliers and max calories category
sn.boxplot(x='Calories',y='Category',data=df)
plt.legend()
plt.show()

attributes1 = ['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars', 'Protein',
              'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)', 'Calcium (% Daily Value)',
              'Iron (% Daily Value)']
max_items = {}
for att in attributes1:
    max_index=df[att].idxmax()
    max_items[att]=df.loc[max_index]

summary=pd.DataFrame(max_items).transpose()
print(summary)


attributes = ['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars', 'Protein',
              'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)', 'Calcium (% Daily Value)',
              'Iron (% Daily Value)']

# Set the size of the plot
plt.figure(figsize=(16, 12))

# Loop through each attribute
for i, attribute in enumerate(attributes, 1):
    plt.subplot(3, 4, i)
    sn.stripplot(x='Category', y=attribute, data=df, jitter=True, alpha=0.5)
    plt.title(attribute)
    plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
#
# plt.figure(figsize=(10, 8))
#
# # Filter unique categories
# categories = df['Category'].unique()
#
# # Loop through each category
# for category in categories:
#     # Filter data for the current category
#     category_df = df[df['Category'] == category]
#
#     # Plot a horizontal bar graph for items in the current category against calories
#     sn.barplot(x='Calories', y='Item', data=category_df, orient='h', errbar=None)
#
#     # Add category name as title
#     plt.title(category)
#
#     # Show the plot
#     plt.show()