import matplotlib.pyplot as plt

# Data for the bars
y = [2, 4, 6]  # Y-axis positions for the bars
heights = [3, 5, 2]  # Heights (length) of the bars

# Set the figure size
plt.figure(figsize=(8, 6))

# Create horizontal bars
plt.barh(y=2, width=3, color='red', linestyle='-', height=0.8)  # Red bar
plt.barh(y=4, width=5, color='blue', linestyle='--', height=0.8)  # Blue dashed bar
plt.barh(y=6, width=2, color='green', linestyle=':', height=0.8)  # Green dotted bar

# Add title and labels
plt.title("Horizontal Bar Chart")
plt.xlabel("X Axis (Bar Width)")
plt.ylabel("Y Axis (Positions)")

# Add grid
plt.grid(True)

# Show the plot
plt.show()
