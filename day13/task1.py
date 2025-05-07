import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

# Plotting the two data ranges
plt.plot([2016,2017,2018,2019,2020],[753, 940, 1174, 1197 ,230 ], color='red', marker='o', label='2016–2020', linewidth=3)
plt.plot([2021,2022,2023,2024,2025],[150 ,614 ,936 ,1100 ,1250 ], color='green', marker='s', label='2021–2025', linewidth=3)

# Adding text annotations
plt.text(2018, 1100, 'Before COVID', fontsize=12, color='red', ha='center')
plt.text(2023, 1100, 'After COVID', fontsize=12, color='green', ha='center')

# Rotating x-ticks and adding grid
plt.xticks(rotation=90)
plt.grid(True)

# Adding title and labels
plt.title("Tourist Visited in Nepal")
plt.xlabel("Year")
plt.ylabel("Growth in Thousand")

# Displaying the legend
plt.legend()

# Showing the plot
plt.show()
