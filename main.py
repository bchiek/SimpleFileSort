import os
import shutil

# Get the directory from the user
directory = input("Enter directory path: ")

# Check if the directory exists
if os.path.exists(directory):
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        # Get the file extension
        file_type = os.path.splitext(file)[1][1:]

        # Create a new directory for this file type, if it doesn't already exist
        new_dir = os.path.join(directory, file_type)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        # Define the source and destination paths
        src_path = os.path.join(directory, file)
        dst_path = os.path.join(new_dir, file)

        # Move the file into the new directory, if the file doesn't already exist there
        if not os.path.exists(dst_path):
            shutil.move(src_path, dst_path)
else:
    print("The directory does not exist.")