import os

file_pathw = "/RISHI/H2K/FileIO/demofile_new_w.txt"

if os.path.exists(file_pathw):
    os.remove(file_pathw)
    print("File is removed ", file_pathw)
else:
    print("File is already removed")

file_dir = "/RISHI/H2K/FileIO/"
file_dir_new = "/RISHI/H2K/FileIO/H2KJune21"

file_list = os.listdir(file_dir)
print(file_list)


if os.path.exists(file_dir_new):
    print("Directory already exists")
else:
    os.mkdir(file_dir_new)
    print("Directory is created")