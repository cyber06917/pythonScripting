import argparse
import sys
from tabulate import tabulate

try:

    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)


    parser = argparse.ArgumentParser()

    #arguments
    parser.add_argument('input_file')
    parser.add_argument('output_file')

    args = parser.parse_args()

    if not args.input_file.endswith(".csv"):
        print("Not a csv file")
        sys.exit(1)

    with open(args.input_file, "r") as csv_file:
        lines = csv_file.readlines()

    header = ['first name', 'last name', 'house']
    
    remain_data = []
    for  line in lines[1:]:
        data = line.strip().split(",")
        data[0], data[1] = data[1], data[0]
        remain_data.append(data)

    csv_file = tabulate(remain_data, headers=header, tablefmt="csv")  
    print(csv_file)

    with open("output.csv", "w") as f:
        f.write(csv_file)

except(FileNotFoundError):
    print("File does not exsit")


