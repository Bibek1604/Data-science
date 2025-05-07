import seaborn as sns 
import matplotlib.pyplot as plt
import random

height = [random.randint(20, 250) for _ in range(100)] 
weight = [random.randint(100, 600) for _ in range(100)]  

sns.scatterplot(x=height, y=weight)
plt.title("Random value between 20-250")
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

gender=['male','male','female','male','female','male']
sns.countplot(y=gender)
plt.title("Chart Based on Population of male and female")
plt.show()