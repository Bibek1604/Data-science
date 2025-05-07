import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

plt.bar(labels, values)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
import matplotlib.pyplot as plt

sizes = [25, 30, 20, 25]
labels = ['Python', 'Java', 'C++', 'JavaScript']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 4, 7, 6, 9]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
import matplotlib.pyplot as plt

data = [22, 55, 62, 45, 21, 22, 34, 42, 42, 44, 55, 62]

plt.hist(data, bins=5)
plt.title("Histogram")
plt.xlabel("Value Ranges")
plt.ylabel("Frequency")
plt.show()
