file_patha = "/RISHI/H2K/FileIO/demofile_new_a.txt"
file_pathx = "/RISHI/H2K/FileIO/demofile_new_x.txt"
file_pathw = "/RISHI/H2K/FileIO/demofile_new_w.txt"

file1 = open(file_pathx, "x")
file1.write("Can we write with x")
file1.close()

file2 = open(file_patha, 'a')
file2.write("Append can write")
file2.close()

file3 = open(file_pathw, 'w')
file3.write("This can also be written")
file3.close()