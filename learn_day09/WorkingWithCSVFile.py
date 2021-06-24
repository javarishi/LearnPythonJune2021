import csv

# Project LINK: https://www.youtube.com/watch?v=S0aSa0XmkkM

csv_file_path = "/RISHI/H2K/FileIO/CSVFilesteachers.csv"
file = open(csv_file_path)
csv_data = csv.reader(file)

for eachDataLine in csv_data:
    print(eachDataLine, type(eachDataLine))

file.close()

file = open(csv_file_path, mode="a")
data = csv.writer(file)
data.writerow(['Byron', ' Card Magic', ' 4'])

file.close()
