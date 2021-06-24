file_path = "/RISHI/H2K/FileIO/demofile.txt"

# r - read only , t - text
file = open(file_path, "rt")
# print(file.read())
# print(file.read(5))
# print(file.read(5))

print(file.readline())
print(file.readline())


file.close()