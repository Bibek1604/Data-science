import os
import shutil

# Path to the folder where original images are stored
image_folder = "images"

# Path to the folder where sorted folders should go
sorted_base_folder = os.path.join(image_folder, "F:\Datascience\DataScience\day23")

# Make sure the base sorted folder exists
os.makedirs(sorted_base_folder, exist_ok=True)

# Get list of all image files in the image folder
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith('.jpg')]

for file in image_files:
    src = os.path.join(image_folder, file)

    if os.path.isdir(src) or file.startswith("F:\Datascience\DataScience\day23"):
        continue

    if '_' in file:
        prefix = file.split('_')[0]
    else:
        continue  

    destination_folder = os.path.join(sorted_base_folder, prefix)
    os.makedirs(destination_folder, exist_ok=True)

    dst = os.path.join(destination_folder, file)

    shutil.move(src, dst)

print("✅ Images sorted into 'F:\Datascience\DataScience\day23' folders!")
