import os

folder_path = "~/ASL_Gally/videos"

# Get the list of files in the folder
file_list = os.listdir(folder_path)

# Iterate over each file
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)

    # Check if the path is a file (not a directory)
    if os.path.isfile(file_path):
        # Append "-YES" to the file name
        new_file_name = file_name[:-4] + "-YES" + file_name[-4:]  # Assuming file extension is 3 characters

        # Construct the new file path
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(file_path, new_file_path)

        print(f"Renamed: {file_name} -> {new_file_name}")

print("File renaming complete.")
