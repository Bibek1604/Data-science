import matplotlib.pyplot as plt


# fig ,ab = plt.subplots()

# ###x axis , y axis
# ab.plot([1,2,3], [2,1,2])
# plt.show()

plt.figure(figsize=(10,6))
plt.plot([2016,2017,2018,2019,2020],[ 753, 940, 1174, 1197 ,230 ],color='red', marker='o', label='2016–2020', linewidth=2)
plt.plot([2021,2022,2023,2024,2025],[150 ,614 ,936 ,1100 ,1250 ],color='green', marker='s', label='2021–2025', linewidth=2)
plt.xticks(rotation=90)
plt.grid(True)
plt.title("Tourist Visited in nepal")
plt.xlabel("Year")
plt.ylabel("growth in thousand")
plt.show() 