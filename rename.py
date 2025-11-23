import os

folder_path = "E:/Subitise/Images/SubitiseImages/Images"

for filename in os.listdir(folder_path):
    if not os.path.isfile(os.path.join(folder_path, filename)):
        continue  # skip subfolders

    if "_" in filename:
        # Keep only the part before the first underscore
        new_name = filename.split("_", 1)[0] + ".png"
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        
        if os.path.exists(new_file):
            print(f"Skipping {filename}, {new_name} already exists.")
            continue
        
        print(f"Renaming {filename} -> {new_name}")
        os.rename(old_file, new_file)
