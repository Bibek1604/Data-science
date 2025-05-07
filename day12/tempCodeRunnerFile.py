import matplotlib.pyplot as plt

categories = ['Peace & Stability', 'Constitutional Amendments', 'Economic Growth', 'Democratic Elections', 
              'Human Rights Progress', 'International Relations', 'Social Development', 
              'Political Instability', 'Corruption', 'Federalism Challenges', 'Political Polarization', 
              'Youth Emigration', 'Maoist Influence', 'Weak Political Parties', 'Natural Disasters']

goodactions = [1, 2, 3, 4, 125, 6, 7, 8, 1, 10, 11, 12, 23, 13, 214, 15]
badactions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

fig,ax=plt.subplots(figsize=(10, 8))
ax.barh(categories, goodactions, color='green', label='Good Actions')
ax.barh(categories, badactions, color='red', label='Bad Actions')
ax.set_xlabel('Actions')

ax.set_title('Political Actions in Nepal')
ax.legend()
plt.show()
