import csv
from unipath import Path

# absolute_path = Path('src/POM/Files/input.csv').absolute()  # To run from command line


absolute_path = Path("../Files/input.csv").absolute()  # To run from local machine, Main class = 'src/POM/Tests/MainParse.py'


def csvReader():
    try:
        with open(absolute_path) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')

            count = 0
            date = []

            for row in reader:
                date.append(row[0])
                count += 1

            print("Total test dates in csv :\t" + str(count - 1))
            print(date)
            csvfile.close()
            return date

    except FileNotFoundError:
        print("File not found. Check the path variable and filename")
        exit()
