import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator

# Define the data
data = {
    'Area': ['China, mainland', 'India', 'United States of America', 'Türkiye', 'Vietnam',
             'Nigeria', 'Egypt', 'Mexico', 'Russian Federation', 'Spain', 'Indonesia',
             'Italy', 'Uzbekistan', 'Japan', 'Ukraine', 'Republic of Korea',
             'Iran', 'Brazil', 'Algeria', 'Bangladesh'],
    'Value': [600013076.6, 137988472.4, 27917337.76, 26646111, 17224210.24,
              15794509.84, 15570923.9, 14747053.05, 13543961.11, 13535730,
              13009595.16, 11440760, 10347671.66, 10176782.13, 9959144.55,
              9768907.13, 9331126.66, 8571771.95, 7652177.11, 7318383]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Sort the DataFrame by Value in descending order
df = df.sort_values(by='Value', ascending=False)

# Create the bar plot with logarithmic y-axis scale
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(df['Area'], df['Value'], color='cornflowerblue')
ax.set_yscale('log')  # Set logarithmic scale for the y-axis

# Set axis labels and title
ax.set_xlabel('Country')
ax.set_ylabel('Vegetable Production (t)')
ax.set_title('Top 20 Countries with Highest Vegetable Production in 2021')

# Customize the major ticks on the y-axis
ax.yaxis.set_major_locator(LogLocator(base=10, subs=(1, 2, 5)))

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Show the plot
plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    'Item': ['Artichokes', 'Asparagus', 'Broad beans and horse beans, green', 'Cabbages',
             'Carrots and turnips', 'Cassava leaves', 'Cauliflowers and broccoli',
             'Chillies and peppers, green (Capsicum spp. and Pimenta spp.)',
             'Cucumbers and gherkins', 'Eggplants (aubergines)', 'Green corn (maize)',
             'Green garlic', 'Leeks and other alliaceous vegetables', 'Lettuce and chicory',
             'Mushrooms and truffles', 'Okra', 'Onions and shallots, dry (excluding dehydrated)',
             'Onions and shallots, green', 'Other beans, green', 'Other vegetables, fresh n.e.c.',
             'Peas, green', 'Pumpkins, squash and gourds', 'Spinach', 'String beans', 'Tomatoes'],
    'Value': [1470332.21, 8501442.93, 1725395.71, 71707238.96, 41666714.44, 86574.72,
              25843741.37, 36286643.77, 93528796, 58646098.21, 8858138.91, 28204854.32,
              2213183.35, 27011747.55, 44207117.25, 10822248.74, 106592088.9, 4562530.02,
              23411172.66, 292200232.7, 20529759.32, 23783936.41, 32294452.3, 1310002.11, 189133955]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Sort the DataFrame by Value in descending order
df = df.sort_values(by='Value', ascending=False)

# Create the bar plot
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(df['Item'], df['Value'], color='cornflowerblue')

# Set axis labels and title
ax.set_xlabel('Production (t)')
ax.set_ylabel('Item')
ax.set_title('Vegetable Production by Item')

# Show the plot
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator

# Define the data for the first plot
data1 = {
    'Area': ['China, mainland', 'India', 'United States of America', 'Türkiye', 'Vietnam',
             'Nigeria', 'Egypt', 'Mexico', 'Russian Federation', 'Spain', 'Indonesia',
             'Italy', 'Uzbekistan', 'Japan', 'Ukraine', 'Republic of Korea',
             'Iran', 'Brazil', 'Algeria', 'Bangladesh'],
    'Value': [600013076.6, 137988472.4, 27917337.76, 26646111, 17224210.24,
              15794509.84, 15570923.9, 14747053.05, 13543961.11, 13535730,
              13009595.16, 11440760, 10347671.66, 10176782.13, 9959144.55,
              9768907.13, 9331126.66, 8571771.95, 7652177.11, 7318383]
}

# Create a DataFrame from the data
df1 = pd.DataFrame(data1)

# Sort the DataFrame by Value in descending order
df1 = df1.sort_values(by='Value', ascending=False)

# Define the data for the second plot
data2 = {
    'Vegetable': ['Artichokes', 'Asparagus', 'Broad beans and horse beans, green', 'Cabbages',
             'Carrots and turnips', 'Cassava leaves', 'Cauliflowers and broccoli',
             'Chillies and peppers, green',
             'Cucumbers and gherkins', 'Eggplants (aubergines)', 'Green corn (maize)',
             'Green garlic', 'Leeks and other alliaceous vegetables', 'Lettuce and chicory',
             'Mushrooms and truffles', 'Okra', 'Onions and shallots, dry (excluding dehydrated)',
             'Onions and shallots, green', 'Other beans, green', 'Other vegetables, fresh',
             'Peas, green', 'Pumpkins, squash and gourds', 'Spinach', 'String beans', 'Tomatoes'],
    'Value': [1470332.21, 8501442.93, 1725395.71, 71707238.96, 41666714.44, 86574.72,
              25843741.37, 36286643.77, 93528796, 58646098.21, 8858138.91, 28204854.32,
              2213183.35, 27011747.55, 44207117.25, 10822248.74, 106592088.9, 4562530.02,
              23411172.66, 292200232.7, 20529759.32, 23783936.41, 32294452.3, 1310002.11, 189133955]
}

# Create a DataFrame from the data
df2 = pd.DataFrame(data2)

# Sort the DataFrame by Value in descending order
df2 = df2.sort_values(by='Value', ascending=False)

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Plot for the first data
ax1.bar(df1['Area'], df1['Value'], color='darkblue')
ax1.set_yscale('log')  # Set logarithmic scale for the y-axis
ax1.set_xlabel('Country')
ax1.set_ylabel('Vegetable Production (t)')
ax1.set_title('Top 20 countries with highest vegetable production in 2021')
ax1.yaxis.set_major_locator(LogLocator(base=10, subs=(1, 2, 5)))
ax1.tick_params(axis='x', rotation=90)

# Plot for the second data
bars2 = ax2.barh(df2['Vegetable'], df2['Value'], color='darkred')
ax2.set_xlabel('Production (t)')
ax2.set_ylabel('Vegetable')
ax2.set_title('Vegetable production by item in 2021')
ax2.tick_params(axis='y', left=False)
ax2.invert_yaxis()

# Remove the values on each bar in the second plot
for bar in bars2:
    bar_width = bar.get_width()
    ax2.annotate('', (bar_width, bar.get_y() + bar.get_height() / 2),
                 xytext=(5, 0), textcoords='offset points', va='center')

# Adjust the spacing between subplots
fig.tight_layout()

# Show the plot
plt.show()
