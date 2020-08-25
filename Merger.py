import os
import glob
import csv

os.chdir("./Files")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

fileLenght = len(all_filenames)
count = 0
percentageAnt = 0

print("Starting merge of", fileLenght, "files")

for f in all_filenames:

    #Progress percentage show
    count += 1
    percentage = round((count/fileLenght)*100)
    if(percentage!=percentageAnt):
        print("Merging", round(percentage), "%", end="\r")
    percentageAnt = percentage

    with open(f) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            with open('../Result/Combined.csv', 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(row)

print("Merging 100 %")
print("Success")