import argparse
import sys
from tabulate import tabulate

try:

    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)


    parser = argparse.ArgumentParser()
    parser.add_argument('file')

    args = parser.parse_args()

    if not args.file.endswith(".csv"):
        print("Not a csv file")
        sys.exit(1)

    with open(args.file, "r") as csv_file:
        lines = csv_file.readlines()

    header = lines[0].strip().split(",")
    
    remain_data = []
    for  line in lines[1:]:
        data = line.strip().split(",")
        remain_data.append(data)

    print(tabulate(remain_data, headers=header, tablefmt="grid"))

except(FileNotFoundError):
    print("File does not exsit")


