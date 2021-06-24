file_path = "/RISHI/H2K/FileIO/demofile.txt"

# r - read only , t - text
file = open(file_path, "rt")
for eachLine in file:
    print(eachLine)

file.close()