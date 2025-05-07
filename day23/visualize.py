# # # # # # # import os
# # # # # # # import matplotlib.pyplot as plt

# # # # # # # # Path to your images directory
# # # # # # # image_folder = "images"

# # # # # # # # Dictionary to hold folder name and file count
# # # # # # # folder_file_counts = {}

# # # # # # # # Read each subfolder and count the number of files inside
# # # # # # # for folder_name in os.listdir(image_folder):
# # # # # # #     folder_path = os.path.join(image_folder, folder_name)
# # # # # # #     if os.path.isdir(folder_path):
# # # # # # #         file_count = len([
# # # # # # #             f for f in os.listdir(folder_path)
# # # # # # #             if os.path.isfile(os.path.join(folder_path, f))
# # # # # # #         ])
# # # # # # #         folder_file_counts[folder_name] = file_count

# # # # # # # # Sort the folders by name
# # # # # # # sorted_counts = dict(sorted(folder_file_counts.items()))

# # # # # # # # Extract names and values
# # # # # # # folder_names = list(sorted_counts.keys())
# # # # # # # file_counts = list(sorted_counts.values())

# # # # # # # # Identify min and max values
# # # # # # # max_count = max(file_counts)
# # # # # # # min_count = min(file_counts)

# # # # # # # # Assign colors based on count
# # # # # # # bar_colors = [
# # # # # # #     'green' if count == max_count else
# # # # # # #     'red' if count == min_count else
# # # # # # #     'skyblue'
# # # # # # #     for count in file_counts
# # # # # # # ]

# # # # # # # # Plotting
# # # # # # # plt.figure(figsize=(16, 8))
# # # # # # # bars = plt.bar(folder_names, file_counts, color=bar_colors)

# # # # # # # # Add text labels above bars
# # # # # # # for bar, count in zip(bars, file_counts):
# # # # # # #     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
# # # # # # #              str(count), ha='center', va='bottom', fontsize=9)

# # # # # # # # Labels and title
# # # # # # # plt.xlabel("Folder Name (Date)")
# # # # # # # plt.ylabel("Number of Files")
# # # # # # # plt.title("📦 Number of Files per Folder in 'images'\n✅ Green: Max | ❌ Red: Min")
# # # # # # # plt.xticks(rotation=90)
# # # # # # # plt.tight_layout()
# # # # # # # plt.show()


# # # # # # #@##pie chart

# # # # # # # import os
# # # # # # # import matplotlib.pyplot as plt

# # # # # # # # Path to your images directory
# # # # # # # image_folder = "images"

# # # # # # # # Dictionary to hold folder name and file count
# # # # # # # folder_file_counts = {}

# # # # # # # # Read each subfolder and count the number of files inside
# # # # # # # for folder_name in os.listdir(image_folder):
# # # # # # #     folder_path = os.path.join(image_folder, folder_name)
# # # # # # #     if os.path.isdir(folder_path):
# # # # # # #         file_count = len([
# # # # # # #             f for f in os.listdir(folder_path)
# # # # # # #             if os.path.isfile(os.path.join(folder_path, f))
# # # # # # #         ])
# # # # # # #         folder_file_counts[folder_name] = file_count

# # # # # # # # Sort the folders by name
# # # # # # # sorted_counts = dict(sorted(folder_file_counts.items()))

# # # # # # # # Extract names and values
# # # # # # # folder_names = list(sorted_counts.keys())
# # # # # # # file_counts = list(sorted_counts.values())

# # # # # # # # Calculate total number of files
# # # # # # # total_files = sum(file_counts)

# # # # # # # # Calculate percentages
# # # # # # # percentages = [(count / total_files) * 100 for count in file_counts]

# # # # # # # # Plotting pie chart
# # # # # # # plt.figure(figsize=(8, 8))
# # # # # # # plt.pie(percentages, labels=folder_names, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)

# # # # # # # # Title
# # # # # # # plt.title("📦 Percentage of Files per Folder in 'images'")

# # # # # # # # Display the chart
# # # # # # # plt.show()



# # # # # # ###defferentiate with embosed number [palte only;]

# # # # # # # import os
# # # # # # # import matplotlib.pyplot as plt

# # # # # # # # Path to your images directory
# # # # # # # image_folder = "images"

# # # # # # # # Dictionary to hold folder name and file count
# # # # # # # folder_file_counts = {}

# # # # # # # # Read each subfolder and count the number of files inside
# # # # # # # for folder_name in os.listdir(image_folder):
# # # # # # #     folder_path = os.path.join(image_folder, folder_name)
# # # # # # #     if os.path.isdir(folder_path):
# # # # # # #         file_count = len([
# # # # # # #             f for f in os.listdir(folder_path)
# # # # # # #             if os.path.isfile(os.path.join(folder_path, f))
# # # # # # #         ])
# # # # # # #         folder_file_counts[folder_name] = file_count

# # # # # # # # Sort the folders by name
# # # # # # # sorted_counts = dict(sorted(folder_file_counts.items()))

# # # # # # # # Extract names and values
# # # # # # # folder_names = list(sorted_counts.keys())
# # # # # # # file_counts = list(sorted_counts.values())

# # # # # # # # Identify the folder with the maximum count
# # # # # # # max_count = max(file_counts)
# # # # # # # max_folder = folder_names[file_counts.index(max_count)]

# # # # # # # # Plotting
# # # # # # # plt.figure(figsize=(16, 8))
# # # # # # # bars = plt.bar(folder_names, file_counts, color='skyblue')

# # # # # # # # Add text labels above bars with embossed effect
# # # # # # # for bar, count, folder_name in zip(bars, file_counts, folder_names):
# # # # # # #     # Regular label
# # # # # # #     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
# # # # # # #              str(count), ha='center', va='bottom', fontsize=9, color='black')

# # # # # # #     # Embossed effect for the folder with the max count
# # # # # # #     if folder_name == max_folder:
# # # # # # #         plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
# # # # # # #                  str(count), ha='center', va='bottom', fontsize=9, color='gray', fontweight='bold')

# # # # # # # # Labels and title
# # # # # # # plt.xlabel("Number plate tyeps")
# # # # # # # plt.ylabel("Number of Files")
# # # # # # # plt.title("📦 Number of Files per Folder in 'images'\nMax Folder Highlighted with Embossed Count")
# # # # # # # plt.xticks(rotation=90)
# # # # # # # plt.tight_layout()
# # # # # # # plt.show()



# # # # # # # import os
# # # # # # # import matplotlib.pyplot as plt

# # # # # # # # Path to your images directory
# # # # # # # image_folder = "images"

# # # # # # # # Dictionary to hold folder name and file count
# # # # # # # folder_file_counts = {}

# # # # # # # # Read each subfolder and count the number of files inside
# # # # # # # for folder_name in os.listdir(image_folder):
# # # # # # #     folder_path = os.path.join(image_folder, folder_name)
# # # # # # #     if os.path.isdir(folder_path):
# # # # # # #         file_count = len([
# # # # # # #             f for f in os.listdir(folder_path)
# # # # # # #             if os.path.isfile(os.path.join(folder_path, f))
# # # # # # #         ])
# # # # # # #         folder_file_counts[folder_name] = file_count

# # # # # # # # Sort the folders by name
# # # # # # # sorted_counts = dict(sorted(folder_file_counts.items()))

# # # # # # # # Extract names and values
# # # # # # # folder_names = list(sorted_counts.keys())
# # # # # # # file_counts = list(sorted_counts.values())

# # # # # # # # Identify the folder with the maximum count
# # # # # # # max_count = max(file_counts)
# # # # # # # max_folder = folder_names[file_counts.index(max_count)]

# # # # # # # # Plotting
# # # # # # # plt.figure(figsize=(16, 8))
# # # # # # # bars = plt.bar(folder_names, file_counts, color='skyblue')

# # # # # # # # Add text labels above bars with embossed effect
# # # # # # # for bar, count, folder_name in zip(bars, file_counts, folder_names):
# # # # # # #     # Regular label for all folders
# # # # # # #     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
# # # # # # #              str(count), ha='center', va='bottom', fontsize=9, color='black')

# # # # # # #     # Embossed effect for the folder with the max count
# # # # # # #     if folder_name == max_folder:
# # # # # # #         plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
# # # # # # #                  str(count), ha='center', va='bottom', fontsize=9, color='gray', fontweight='bold')

# # # # # # # # Add title and labels
# # # # # # # plt.xlabel("Folder Name (Date)")
# # # # # # # plt.ylabel("Number of Files")
# # # # # # # plt.title("📦 Number of Files per Folder in 'images'\nMax Folder Highlighted with Embossed Count")
# # # # # # # plt.xticks(rotation=90)
# # # # # # # plt.tight_layout()

# # # # # # # # Show the plot
# # # # # # # plt.show()


# # # # # # # import os
# # # # # # # import matplotlib.pyplot as plt

# # # # # # # # Path to your images directory
# # # # # # # image_folder = "images"

# # # # # # # # Dictionary to hold folder name and file count
# # # # # # # folder_file_counts = {}

# # # # # # # # Read each subfolder and count the number of files inside
# # # # # # # for folder_name in os.listdir(image_folder):
# # # # # # #     folder_path = os.path.join(image_folder, folder_name)
# # # # # # #     if os.path.isdir(folder_path):
# # # # # # #         file_count = len([
# # # # # # #             f for f in os.listdir(folder_path)
# # # # # # #             if os.path.isfile(os.path.join(folder_path, f))
# # # # # # #         ])
# # # # # # #         folder_file_counts[folder_name] = file_count

# # # # # # # # Sort the folders by name
# # # # # # # sorted_counts = dict(sorted(folder_file_counts.items()))

# # # # # # # # Extract names and values
# # # # # # # folder_names = list(sorted_counts.keys())
# # # # # # # file_counts = list(sorted_counts.values())

# # # # # # # # Plotting
# # # # # # # plt.figure(figsize=(16, 8))
# # # # # # # bars = plt.bar(folder_names, file_counts, color='skyblue')

# # # # # # # # Add embossed text labels above bars for all folders
# # # # # # # for bar, count, folder_name in zip(bars, file_counts, folder_names):
# # # # # # #     # Embossed label effect for every folder
# # # # # # #     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
# # # # # # #              str(count), ha='center', va='bottom', fontsize=9, color='gray', fontweight='bold')

# # # # # # # # Labels and title
# # # # # # # plt.xlabel("Folder Name (Date)")
# # # # # # # plt.ylabel("Number of Files")
# # # # # # # plt.title("📦 Comparison of Files per Folder in 'images'\nAll Folders with Embossed Count")
# # # # # # # plt.xticks(rotation=90)
# # # # # # # plt.tight_layout()

# # # # # # # # Show the plot
# # # # # # # plt.show()
# # # # # # # import os
# # # # # # # import shutil
# # # # # # # import matplotlib.pyplot as plt

# # # # # # # # Path to your images directory
# # # # # # # image_folder = "images"

# # # # # # # # Dictionary to hold folder name and file count
# # # # # # # folder_file_counts = {}

# # # # # # # # Read each subfolder and count the number of files inside
# # # # # # # for folder_name in os.listdir(image_folder):
# # # # # # #     folder_path = os.path.join(image_folder, folder_name)
# # # # # # #     if os.path.isdir(folder_path):
# # # # # # #         file_count = len([
# # # # # # #             f for f in os.listdir(folder_path)
# # # # # # #             if os.path.isfile(os.path.join(folder_path, f))
# # # # # # #         ])
# # # # # # #         folder_file_counts[folder_name] = file_count

# # # # # # # # Sort the folders by name
# # # # # # # sorted_counts = dict(sorted(folder_file_counts.items()))

# # # # # # # # Extract names and values
# # # # # # # folder_names = list(sorted_counts.keys())
# # # # # # # file_counts = list(sorted_counts.values())

# # # # # # # # Identify the folder with the maximum count
# # # # # # # max_count = max(file_counts)
# # # # # # # max_folder = folder_names[file_counts.index(max_count)]

# # # # # # # # Create a new folder for the merged files
# # # # # # # merged_folder = os.path.join(image_folder, "merged_folder")
# # # # # # # if not os.path.exists(merged_folder):
# # # # # # #     os.makedirs(merged_folder)

# # # # # # # # Merge all folders' files (except the max folder) into the new folder
# # # # # # # for folder_name in folder_names:
# # # # # # #     if folder_name != max_folder:
# # # # # # #         folder_path = os.path.join(image_folder, folder_name)
# # # # # # #         for file_name in os.listdir(folder_path):
# # # # # # #             file_path = os.path.join(folder_path, file_name)
# # # # # # #             if os.path.isfile(file_path):
# # # # # # #                 shutil.copy(file_path, os.path.join(merged_folder, file_name))

# # # # # # # # Recalculate the file counts for the max folder and the merged folder
# # # # # # # new_folder_count = len([f for f in os.listdir(merged_folder) if os.path.isfile(os.path.join(merged_folder, f))])

# # # # # # # # Prepare data for plotting
# # # # # # # folder_names.append("Merged Folder")
# # # # # # # file_counts.append(new_folder_count)

# # # # # # # # Plotting
# # # # # # # plt.figure(figsize=(16, 8))
# # # # # # # bars = plt.bar(folder_names, file_counts, color='skyblue')

# # # # # # # # Add embossed text labels above bars for all folders
# # # # # # # for bar, count, folder_name in zip(bars, file_counts, folder_names):
# # # # # # #     # Embossed label effect for the folders
# # # # # # #     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
# # # # # # #              str(count), ha='center', va='bottom', fontsize=9, color='gray', fontweight='bold')

# # # # # # # # Labels and title
# # # # # # # plt.xlabel("Folder Name")
# # # # # # # plt.ylabel("Number of Files")
# # # # # # # plt.title("📦 Comparison of Files per Folder in 'images'\nMax Folder and Merged Folder with Embossed Count")
# # # # # # # plt.xticks(rotation=90)
# # # # # # # plt.tight_layout()

# # # # # # # # Show the plot
# # # # # # # # plt.show()
# # # # # # # import os
# # # # # # # import shutil
# # # # # # # import matplotlib.pyplot as plt

# # # # # # # # Path to your images directory
# # # # # # # image_folder = "images"

# # # # # # # # Dictionary to hold folder name and file count
# # # # # # # folder_file_counts = {}

# # # # # # # # Read each subfolder and count the number of files inside
# # # # # # # for folder_name in os.listdir(image_folder):
# # # # # # #     folder_path = os.path.join(image_folder, folder_name)
# # # # # # #     if os.path.isdir(folder_path):
# # # # # # #         file_count = len([
# # # # # # #             f for f in os.listdir(folder_path)
# # # # # # #             if os.path.isfile(os.path.join(folder_path, f))
# # # # # # #         ])
# # # # # # #         folder_file_counts[folder_name] = file_count

# # # # # # # # Sort the folders by name
# # # # # # # sorted_counts = dict(sorted(folder_file_counts.items()))

# # # # # # # # Extract names and values
# # # # # # # folder_names = list(sorted_counts.keys())
# # # # # # # file_counts = list(sorted_counts.values())

# # # # # # # # Identify the folder with the maximum count
# # # # # # # max_count = max(file_counts)
# # # # # # # max_folder = folder_names[file_counts.index(max_count)]

# # # # # # # # Create a new folder for the merged files
# # # # # # # merged_folder = os.path.join(image_folder, "merged_folder")
# # # # # # # if not os.path.exists(merged_folder):
# # # # # # #     os.makedirs(merged_folder)

# # # # # # # # Merge all folders' files (except the max folder) into the new folder
# # # # # # # for folder_name in folder_names:
# # # # # # #     if folder_name != max_folder:
# # # # # # #         folder_path = os.path.join(image_folder, folder_name)
# # # # # # #         for file_name in os.listdir(folder_path):
# # # # # # #             file_path = os.path.join(folder_path, file_name)
# # # # # # #             if os.path.isfile(file_path):
# # # # # # #                 shutil.copy(file_path, os.path.join(merged_folder, file_name))

# # # # # # # # Recalculate the file count for the merged folder
# # # # # # # new_folder_count = len([f for f in os.listdir(merged_folder) if os.path.isfile(os.path.join(merged_folder, f))])

# # # # # # # # Prepare data for plotting (Only show merged folder with embossed count)
# # # # # # # folder_names = ["Merged Folder"]
# # # # # # # file_counts = [new_folder_count]

# # # # # # # # Plotting
# # # # # # # plt.figure(figsize=(8, 6))
# # # # # # # bars = plt.bar(folder_names, file_counts, color='skyblue')

# # # # # # # # Add embossed text label above the bar for the merged folder
# # # # # # # for bar, count, folder_name in zip(bars, file_counts, folder_names):
# # # # # # #     # Embossed label effect for the merged folder
# # # # # # #     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
# # # # # # #              str(count), ha='center', va='bottom', fontsize=9, color='gray', fontweight='bold')

# # # # # # # # Labels and title
# # # # # # # plt.xlabel("Folder Name")
# # # # # # # plt.ylabel("Number of Files")
# # # # # # # plt.title("📦 Comparison of Files per Folder\nMerged Folder with Embossed Count")
# # # # # # # plt.tight_layout()

# # # # # # # # Show the plot
# # # # # # # plt.show()

# # # # # # import os
# # # # # # import shutil
# # # # # # import matplotlib.pyplot as plt

# # # # # # # Path to your images directory
# # # # # # image_folder = "images"

# # # # # # # Dictionary to hold folder name and file count
# # # # # # folder_file_counts = {}

# # # # # # # Read each subfolder and count the number of files inside
# # # # # # for folder_name in os.listdir(image_folder):
# # # # # #     folder_path = os.path.join(image_folder, folder_name)
# # # # # #     if os.path.isdir(folder_path):
# # # # # #         file_count = len([
# # # # # #             f for f in os.listdir(folder_path)
# # # # # #             if os.path.isfile(os.path.join(folder_path, f))
# # # # # #         ])
# # # # # #         folder_file_counts[folder_name] = file_count

# # # # # # # Sort the folders by name
# # # # # # sorted_counts = dict(sorted(folder_file_counts.items()))

# # # # # # # Extract names and values
# # # # # # folder_names = list(sorted_counts.keys())
# # # # # # file_counts = list(sorted_counts.values())

# # # # # # # Identify the folder with the maximum count (Embossed Folder)
# # # # # # max_count = max(file_counts)
# # # # # # max_folder = folder_names[file_counts.index(max_count)]

# # # # # # # Create a new folder for the merged files
# # # # # # merged_folder = os.path.join(image_folder, "merged_folder")
# # # # # # if not os.path.exists(merged_folder):
# # # # # #     os.makedirs(merged_folder)

# # # # # # # Merge all folders' files (except the max folder) into the new folder
# # # # # # for folder_name in folder_names:
# # # # # #     if folder_name != max_folder:
# # # # # #         folder_path = os.path.join(image_folder, folder_name)
# # # # # #         for file_name in os.listdir(folder_path):
# # # # # #             file_path = os.path.join(folder_path, file_name)
# # # # # #             if os.path.isfile(file_path):
# # # # # #                 shutil.copy(file_path, os.path.join(merged_folder, file_name))

# # # # # # # Recalculate the file counts for the max folder and the merged folder
# # # # # # max_folder_count = len([f for f in os.listdir(os.path.join(image_folder, max_folder)) if os.path.isfile(os.path.join(image_folder, max_folder, f))])
# # # # # # merged_folder_count = len([f for f in os.listdir(merged_folder) if os.path.isfile(os.path.join(merged_folder, f))])

# # # # # # # Prepare data for plotting (Only show the embossed folder and merged folder)
# # # # # # folder_names = [max_folder, "Merged Folder"]
# # # # # # file_counts = [max_folder_count, merged_folder_count]

# # # # # # # Plotting
# # # # # # plt.figure(figsize=(8, 6))
# # # # # # bars = plt.bar(folder_names, file_counts, color=['green', 'skyblue'])

# # # # # # # Add embossed text labels above the bars for both folders
# # # # # # for bar, count, folder_name in zip(bars, file_counts, folder_names):
# # # # # #     # Embossed label effect for both folders
# # # # # #     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
# # # # # #              str(count), ha='center', va='bottom', fontsize=9, color='gray', fontweight='bold')

# # # # # # # Labels and title
# # # # # # plt.xlabel("Folder Name")
# # # # # # plt.ylabel("Number of Files")
# # # # # # plt.title("📦 Comparison of Merged Folder and Embossed Folder\nWith Embossed Count")
# # # # # # plt.tight_layout()

# # # # # # # Show the plot
# # # # # # plt.show()

# # # # # import os
# # # # # import shutil
# # # # # import matplotlib.pyplot as plt

# # # # # # Path to your images directory
# # # # # image_folder = "images"

# # # # # # Dictionary to hold folder name and file count
# # # # # folder_file_counts = {}

# # # # # # Read each subfolder and count the number of files inside
# # # # # for folder_name in os.listdir(image_folder):
# # # # #     folder_path = os.path.join(image_folder, folder_name)
# # # # #     if os.path.isdir(folder_path):
# # # # #         file_count = len([
# # # # #             f for f in os.listdir(folder_path)
# # # # #             if os.path.isfile(os.path.join(folder_path, f))
# # # # #         ])
# # # # #         folder_file_counts[folder_name] = file_count

# # # # # # Sort the folders by name
# # # # # sorted_counts = dict(sorted(folder_file_counts.items()))

# # # # # # Extract names and values
# # # # # folder_names = list(sorted_counts.keys())
# # # # # file_counts = list(sorted_counts.values())

# # # # # # Identify the folder with the maximum count (Embossed Folder)
# # # # # max_count = max(file_counts)
# # # # # max_folder = folder_names[file_counts.index(max_count)]

# # # # # # Create a new folder for the merged files
# # # # # merged_folder = os.path.join(image_folder, "merged_folder")
# # # # # if not os.path.exists(merged_folder):
# # # # #     os.makedirs(merged_folder)

# # # # # # Merge all folders' files (except the embossed folder) into the new folder
# # # # # for folder_name in folder_names:
# # # # #     if folder_name != max_folder:
# # # # #         folder_path = os.path.join(image_folder, folder_name)
# # # # #         for file_name in os.listdir(folder_path):
# # # # #             file_path = os.path.join(folder_path, file_name)
# # # # #             if os.path.isfile(file_path):
# # # # #                 shutil.copy(file_path, os.path.join(merged_folder, file_name))

# # # # # # Recalculate the file counts for the max folder and the merged folder
# # # # # max_folder_count = len([f for f in os.listdir(os.path.join(image_folder, max_folder)) if os.path.isfile(os.path.join(image_folder, max_folder, f))])
# # # # # merged_folder_count = len([f for f in os.listdir(merged_folder) if os.path.isfile(os.path.join(merged_folder, f))])

# # # # # # Prepare data for plotting (Only show the embossed folder and merged folder)
# # # # # folder_names = [max_folder, "Merged Folder"]
# # # # # file_counts = [max_folder_count, merged_folder_count]

# # # # # # Plotting
# # # # # plt.figure(figsize=(8, 6))
# # # # # bars = plt.bar(folder_names, file_counts, color=['green', 'skyblue'])

# # # # # # Add embossed text labels above the bars for both folders
# # # # # for bar, count, folder_name in zip(bars, file_counts, folder_names):
# # # # #     # Embossed label effect for both folders
# # # # #     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
# # # # #              str(count), ha='center', va='bottom', fontsize=9, color='gray', fontweight='bold')

# # # # # # Labels and title
# # # # # plt.xlabel("Folder Name")
# # # # # plt.ylabel("Number of Files")
# # # # # plt.title("📦 Comparison of Merged Folder and Embossed Folder\nWith Embossed Count")
# # # # # plt.tight_layout()

# # # # # # Show the plot
# # # # # plt.show()
# # # # import os
# # # # import shutil
# # # # import matplotlib.pyplot as plt

# # # # # Path to your images directory
# # # # image_folder = "images"

# # # # # Dictionary to hold folder name and file count
# # # # folder_file_counts = {}

# # # # # Read each subfolder and count the number of files inside
# # # # for folder_name in os.listdir(image_folder):
# # # #     folder_path = os.path.join(image_folder, folder_name)
# # # #     if os.path.isdir(folder_path):
# # # #         file_count = len([
# # # #             f for f in os.listdir(folder_path)
# # # #             if os.path.isfile(os.path.join(folder_path, f))
# # # #         ])
# # # #         folder_file_counts[folder_name] = file_count

# # # # # Sort the folders by file count (ascending) to find the embossed folder (smallest count)
# # # # sorted_counts = dict(sorted(folder_file_counts.items(), key=lambda item: item[1]))

# # # # # Extract names and values
# # # # folder_names = list(sorted_counts.keys())
# # # # file_counts = list(sorted_counts.values())

# # # # # Identify the embossed folder (folder with the smallest file count)
# # # # embossed_folder = folder_names[0]  # The folder with the smallest file count
# # # # embossed_folder_count = file_counts[0]

# # # # # Create a new folder for the merged files (excluding the embossed folder)
# # # # merged_folder = os.path.join(image_folder, "merged_folder")
# # # # if not os.path.exists(merged_folder):
# # # #     os.makedirs(merged_folder)

# # # # # Merge all folders' files (except the embossed folder) into the new folder
# # # # for folder_name in folder_names[1:]:
# # # #     folder_path = os.path.join(image_folder, folder_name)
# # # #     for file_name in os.listdir(folder_path):
# # # #         file_path = os.path.join(folder_path, file_name)
# # # #         if os.path.isfile(file_path):
# # # #             shutil.copy(file_path, os.path.join(merged_folder, file_name))

# # # # # Recalculate the file counts for the embossed folder and the merged folder
# # # # merged_folder_count = len([f for f in os.listdir(merged_folder) if os.path.isfile(os.path.join(merged_folder, f))])

# # # # # Data to visualize (embossed folder vs merged folder)
# # # # categories = ['Embossed Folder', 'Merged Folder']
# # # # counts = [embossed_folder_count, merged_folder_count]

# # # # # Plotting - Bar Chart
# # # # plt.figure(figsize=(8, 6))
# # # # bars = plt.bar(categories, counts, color=['green', 'skyblue'])

# # # # # Add labels above bars for file counts
# # # # for bar, count in zip(bars, counts):
# # # #     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
# # # #              str(count), ha='center', va='bottom', fontsize=9, color='gray', fontweight='bold')

# # # # # Labels and title
# # # # plt.xlabel("Folder Name")
# # # # plt.ylabel("Number of Files")
# # # # plt.title("📦 Comparison of Embossed Folder and Merged Folder\nWith File Counts")
# # # # plt.tight_layout()

# # # # # Show the plot
# # # # plt.show()

# # # # # Plotting - Pie Chart
# # # # plt.figure(figsize=(8, 6))
# # # # plt.pie(counts, labels=categories, autopct='%1.1f%%', colors=['green', 'skyblue'], startangle=90, explode=(0.1, 0))
# # # # plt.title("📊 Comparison of Embossed Folder and Merged Folder\nWith File Percentages")
# # # # plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.

# # # # # Show the plot
# # # # plt.show()


# # # import os
# # # import shutil
# # # import matplotlib.pyplot as plt

# # # # Path to your images directory
# # # image_folder = "images"

# # # # Path to the merged folder containing "embossed" and "merged_folder" subfolders
# # # merged_folder_path = os.path.join(image_folder, "merged_folder")

# # # # Initialize file counts
# # # embossed_folder_count = 0
# # # merged_subfolder_count = 0

# # # # Check if "merged_folder" exists
# # # if os.path.exists(merged_folder_path):
# # #     # Count files inside the "embossed" folder
# # #     embossed_folder_path = os.path.join(merged_folder_path, "embossed")
# # #     if os.path.exists(embossed_folder_path):
# # #         embossed_folder_count = len([f for f in os.listdir(embossed_folder_path) if os.path.isfile(os.path.join(embossed_folder_path, f))])

# # #     # Count files inside the "merged_folder" subfolder
# # #     merged_subfolder_path = os.path.join(merged_folder_path, "merged_folder")
# # #     if os.path.exists(merged_subfolder_path):
# # #         merged_subfolder_count = len([f for f in os.listdir(merged_subfolder_path) if os.path.isfile(os.path.join(merged_subfolder_path, f))])

# # # # Data for comparison
# # # categories = ['Embossed Folder', 'Merged Folder']
# # # counts = [embossed_folder_count, merged_subfolder_count]

# # # # Plotting - Bar Chart
# # # plt.figure(figsize=(8, 6))
# # # bars = plt.bar(categories, counts, color=['green', 'skyblue'])

# # # # Add labels above bars for file counts
# # # for bar, count in zip(bars, counts):
# # #     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
# # #              str(count), ha='center', va='bottom', fontsize=9, color='gray', fontweight='bold')

# # # # Labels and title
# # # plt.xlabel("Folder Name")
# # # plt.ylabel("Number of Files")
# # # plt.title("📦 Comparison of Embossed Folder vs Merged Folder\nWith File Counts")
# # # plt.tight_layout()

# # # # Show the plot
# # # plt.show()

# # # # Plotting - Pie Chart
# # # plt.figure(figsize=(8, 6))
# # # plt.pie(counts, labels=categories, autopct='%1.1f%%', colors=['green', 'skyblue'], startangle=90, explode=(0.1, 0))
# # # plt.title("📊 Comparison of Embossed Folder vs Merged Folder\nWith File Percentages")
# # # plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.

# # # # Show the plot
# # # plt.show()
# # import os
# # import matplotlib.pyplot as plt

# # # Path to your images directory
# # image_folder = r"F:\Datascience\DataScience\images"

# # # Path to the merged folder containing "embossed" and "merged_folder" subfolders
# # merged_folder_path = os.path.join(image_folder, "merged_folder")

# # # Initialize file counts
# # embossed_folder_count = 0
# # merged_subfolder_count = 0

# # # Check if "merged_folder" exists
# # if os.path.exists(merged_folder_path):
# #     print(f"Found 'merged_folder' at: {merged_folder_path}")
    
# #     # Count files inside the "embossed" folder
# #     embossed_folder_path = os.path.join(merged_folder_path, "embossed")
# #     if os.path.exists(embossed_folder_path):
# #         print(f"Found 'embossed' folder at: {embossed_folder_path}")
# #         embossed_folder_count = len([f for f in os.listdir(embossed_folder_path) if os.path.isfile(os.path.join(embossed_folder_path, f))])
# #         print(f"Embossed folder file count: {embossed_folder_count}")
# #     else:
# #         print(f"'Embossed' folder not found in {merged_folder_path}")

# #     # Count files inside the "merged_folder" subfolder
# #     merged_subfolder_path = os.path.join(merged_folder_path, "merged_folder")
# #     if os.path.exists(merged_subfolder_path):
# #         print(f"Found 'merged_folder' subfolder at: {merged_subfolder_path}")
# #         merged_subfolder_count = len([f for f in os.listdir(merged_subfolder_path) if os.path.isfile(os.path.join(merged_subfolder_path, f))])
# #         print(f"Merged folder file count: {merged_subfolder_count}")
# #     else:
# #         print(f"'Merged_folder' subfolder not found in {merged_folder_path}")

# # else:
# #     print(f"'{merged_folder_path}' does not exist")

# # # Data for comparison
# # categories = ['Embossed Folder', 'Merged Folder']
# # counts = [embossed_folder_count, merged_subfolder_count]

# # # Print out the counts before plotting
# # print(f"Comparison Data: {dict(zip(categories, counts))}")

# # # If both counts are zero, print a warning
# # if all(count == 0 for count in counts):
# #     print("Warning: Both folders are empty or not found. No data to display.")

# # # Plotting - Bar Chart
# # if any(count > 0 for count in counts):
# #     plt.figure(figsize=(8, 6))
# #     bars = plt.bar(categories, counts, color=['green', 'skyblue'])

# #     # Add labels above bars for file counts
# #     for bar, count in zip(bars, counts):
# #         plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
# #                  str(count), ha='center', va='bottom', fontsize=9, color='gray', fontweight='bold')

# #     # Labels and title
# #     plt.xlabel("Folder Name")
# #     plt.ylabel("Number of Files")
# #     plt.title("📦 Comparison of Embossed Folder vs Merged Folder\nWith File Counts")
# #     plt.tight_layout()

# #     # Show the plot
# #     plt.show()

# #     # Plotting - Pie Chart
# #     plt.figure(figsize=(8, 6))
# #     plt.pie(counts, labels=categories, autopct='%1.1f%%', colors=['green', 'skyblue'], startangle=90, explode=(0.1, 0))
# #     plt.title("📊 Comparison of Embossed Folder vs Merged Folder\nWith File Percentages")
# #     plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.

# #     # Show the plot
# #     plt.show()
# # else:
# #     print("No valid data to plot.")
# import os
# import matplotlib.pyplot as plt

# # Path to your images directory
# image_folder = r"F:\Datascience\DataScience\images"

# # Path to the merged folder containing "embossed" and "merged_folder" subfolders
# merged_folder_path = os.path.join(image_folder, "merged_folder")

# # Initialize file counts
# embossed_folder_count = 0
# merged_subfolder_count = 0

# # Check if "merged_folder" exists
# if os.path.exists(merged_folder_path):
#     print(f"Found 'merged_folder' at: {merged_folder_path}")
    
#     # Count files inside the "embossed" folder
#     embossed_folder_path = os.path.join(merged_folder_path, "embossed")
#     if os.path.exists(embossed_folder_path):
#         print(f"Found 'embossed' folder at: {embossed_folder_path}")
#         # Check the files in the embossed folder
#         embossed_files = [f for f in os.listdir(embossed_folder_path) if os.path.isfile(os.path.join(embossed_folder_path, f))]
#         embossed_folder_count = len(embossed_files)
#         print(f"Embossed folder file count: {embossed_folder_count} files")
#         print(f"Files in embossed folder: {embossed_files}")
#     else:
#         print(f"'Embossed' folder not found in {merged_folder_path}")

#     # Count files inside the "merged_folder" subfolder
#     merged_subfolder_path = os.path.join(merged_folder_path, "merged_folder")
#     if os.path.exists(merged_subfolder_path):
#         print(f"Found 'merged_folder' subfolder at: {merged_subfolder_path}")
#         # Check the files in the merged folder
#         merged_files = [f for f in os.listdir(merged_subfolder_path) if os.path.isfile(os.path.join(merged_subfolder_path, f))]
#         merged_subfolder_count = len(merged_files)
#         print(f"Merged folder file count: {merged_subfolder_count} files")
#         print(f"Files in merged folder: {merged_files}")
#     else:
#         print(f"'Merged_folder' subfolder not found in {merged_folder_path}")

# else:
#     print(f"'{merged_folder_path}' does not exist")

# # Data for comparison
# categories = ['Embossed Folder', 'Merged Folder']
# counts = [embossed_folder_count, merged_subfolder_count]

# # Print out the counts before plotting
# print(f"Comparison Data: {dict(zip(categories, counts))}")

# # If both counts are zero, print a warning
# if all(count == 0 for count in counts):
#     print("Warning: Both folders are empty or not found. No data to display.")
# else:
#     # Plotting - Bar Chart
#     plt.figure(figsize=(8, 6))
#     bars = plt.bar(categories, counts, color=['green', 'skyblue'])

#     # Add labels above bars for file counts
#     for bar, count in zip(bars, counts):
#         plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
#                  str(count), ha='center', va='bottom', fontsize=9, color='gray', fontweight='bold')

#     # Labels and title
#     plt.xlabel("Folder Name")
#     plt.ylabel("Number of Files")
#     plt.title("📦 Comparison of Embossed Folder vs Merged Folder\nWith File Counts")
#     plt.tight_layout()

#     # Show the plot
#     plt.show()

#     # Plotting - Pie Chart
#     plt.figure(figsize=(8, 6))
#     plt.pie(counts, labels=categories, autopct='%1.1f%%', colors=['green', 'skyblue'], startangle=90, explode=(0.1, 0))
#     plt.title("📊 Comparison of Embossed Folder vs Merged Folder\nWith File Percentages")
#     plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.

#     # Show the plot
#     plt.show()
import os
import matplotlib.pyplot as plt

# Path to your images directory
image_folder = r"F:\Datascience\DataScience\images"

# Initialize file counts for both embossed and merged_folder
embossed_folder_count = 0
merged_folder_count = 0

# Define paths for embossed and merged_folder
embossed_folder_path = os.path.join(image_folder, "embossed")
merged_folder_path = os.path.join(image_folder, "merged_folder")

# Check if 'embossed' folder exists and count files
if os.path.exists(embossed_folder_path):
    print(f"Found 'embossed' folder at: {embossed_folder_path}")
    embossed_files = [f for f in os.listdir(embossed_folder_path) if os.path.isfile(os.path.join(embossed_folder_path, f))]
    embossed_folder_count = len(embossed_files)
    print(f"Embossed folder file count: {embossed_folder_count} files")
else:
    print(f"'Embossed' folder not found in {image_folder}")

# Check if 'merged_folder' exists and count files
if os.path.exists(merged_folder_path):
    print(f"Found 'merged_folder' at: {merged_folder_path}")
    merged_files = [f for f in os.listdir(merged_folder_path) if os.path.isfile(os.path.join(merged_folder_path, f))]
    merged_folder_count = len(merged_files)
    print(f"Merged folder file count: {merged_folder_count} files")
else:
    print(f"'Merged_folder' not found in {image_folder}")

# Data for comparison
categories = ['Embossed Folder', 'Merged Folder']
counts = [embossed_folder_count, merged_folder_count]

# Print out the counts before plotting
print(f"Comparison Data: {dict(zip(categories, counts))}")

# If both counts are zero, print a warning
if all(count == 0 for count in counts):
    print("Warning: Both folders are empty or not found. No data to display.")
else:
    # Plotting - Bar Chart
    plt.figure(figsize=(8, 6))
    bars = plt.bar(categories, counts, color=['green', 'skyblue'])

    # Add labels above bars for file counts
    for bar, count in zip(bars, counts):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 str(count), ha='center', va='bottom', fontsize=9, color='gray', fontweight='bold')

    # Labels and title
    plt.xlabel("Folder Name")
    plt.ylabel("Number of Files")
    plt.title("📦 Comparison of Embossed Folder vs Merged Folder\nWith File Counts")
    plt.tight_layout()

    # Show the plot
    plt.show()

    # Plotting - Pie Chart
    plt.figure(figsize=(8, 6))
    plt.pie(counts, labels=categories, autopct='%1.1f%%', colors=['green', 'skyblue'], startangle=90, explode=(0.1, 0))
    plt.title(" Comparison of Embossed numberplate vs Normal numberplate")
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.

    # Show the plot
    plt.show()
