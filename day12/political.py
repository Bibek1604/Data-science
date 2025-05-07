import matplotlib.pyplot as plt

# Data for good and bad aspects
categories = ['Peace & Stability', 'Constitutional Amendments', 'Economic Growth', 'Democratic Elections', 
              'Human Rights Progress', 'International Relations', 'Social Development', 
              'Political Instability', 'Corruption', 'Federalism Challenges', 'Political Polarization', 
              'Youth Emigration', 'Maoist Influence', 'Weak Political Parties', 'Natural Disasters']

good_aspects = [0, 1, 1, 1, 0, 2, 1, 1, 0, 0, 1, 0, 0, 2, 2]
bad_aspects = [1, 1, 1, 1, 0, 2, 0, 2, 1, 1, 2, 1, 2, 0, 0]

# Create a new type of plot: Horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.4
index = range(len(categories))

# Plotting the good and bad aspects horizontally
bar1 = ax.barh(index, good_aspects, bar_width, label='Good Aspects', color='seagreen')
bar2 = ax.barh([i + bar_width for i in index], bad_aspects, bar_width, label='Bad Aspects', color='tomato')

# Adding labels and title
ax.set_ylabel('Categories')
ax.set_xlabel('Impact Level (0=Absent, 1=Medium, 2=High)')
ax.set_title('Political Landscape of Nepal (2080-2081) - Horizontal View')
ax.set_yticks([i + bar_width / 2 for i in index])
ax.set_yticklabels(categories)
ax.invert_yaxis()  # Highest impact on top
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()

