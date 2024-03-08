import os

def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def list_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def list_all(path):
    all_items = os.listdir(path)
    directories = [d for d in all_items if os.path.isdir(os.path.join(path, d))]
    files = [f for f in all_items if os.path.isfile(os.path.join(path, f))]
    return directories, files

specified_path = r"C:\Users\NEO\Desktop\lab6"  
directories_only = list_directories(specified_path)
files_only = list_files(specified_path)
all_items = list_all(specified_path)

print(f"Directories only: {directories_only}")
print(f"Files only: {files_only}")
print(f"All Directories and Files: {all_items}")
