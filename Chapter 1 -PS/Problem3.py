import os

# Specify the path to the directory
directory_path = '.'  # Current directory; you can change it to any path

# Get the list of files and directories
try:
    contents = os.listdir(directory_path)
    print(f"Contents of the directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
