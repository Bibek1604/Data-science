import os
import shutil

# Define original image folder
image_folder = "images"

# Define target base folder for sorted images
sorted_base_folder = os.path.join(image_folder, "wsmaq")

# Step 1: Clean the wsmaq folder if it already exists
if os.path.exists(sorted_base_folder):
    shutil.rmtree(sorted_base_folder)
os.makedirs(sorted_base_folder)

# Step 2: Get all image files in the root of image_folder (exclude subfolders like wsmaq)
image_files = [
    f for f in os.listdir(image_folder)
    if os.path.isfile(os.path.join(image_folder, f)) and f.lower().endswith('.jpg')
]

# Step 3: Move images into sorted folders under wsmaq
for file in image_files:
    # Extract prefix (e.g., 'cat' from 'cat_01.jpg')
    if '_' in file:
        prefix = file.split('_')[0]
    else:
        continue  # Skip files without underscore

    # Create target folder inside wsmaq
    target_folder = os.path.join(sorted_base_folder, prefix)
    os.makedirs(target_folder, exist_ok=True)

    # Move image
    src = os.path.join(image_folder, file)
    dst = os.path.join(target_folder, file)
    shutil.move(src, dst)

print("✅ All images moved cleanly to wsmaq/<prefix> folders with previous data cleared.")


import os
import matplotlib.pyplot as plt

# Set the path to your "images" directory
image_folder = "images"

# Create a dictionary to store {folder_name: number_of_files}
folder_file_counts = {}

# Loop through each item in the images folder
for folder_name in os.listdir(image_folder):
    folder_path = os.path.join(image_folder, folder_name)
    if os.path.isdir(folder_path):
        # Count the number of files in the subfolder
        file_count = len([
            f for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ])
        folder_file_counts[folder_name] = file_count

# Sort the dictionary by folder name (optional)
sorted_counts = dict(sorted(folder_file_counts.items()))

# Plotting
plt.figure(figsize=(14, 7))
plt.bar(sorted_counts.keys(), sorted_counts.values(), color='teal')
plt.xlabel('Folder Name (Date)')
plt.ylabel('Number of Files')
plt.title('Number of Files per Date Folder in "images"')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
