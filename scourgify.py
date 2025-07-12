import argparse
import sys
import csv

try:



    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            print("Too few command-line arguments")
        else:
            print("Too many command-line arguments")
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

    remain_data = []
    for  line in lines[1:]:
        data = line.replace('"','').strip().split(",")
        data = [field.strip() for field in data]
        data[0], data[1] = data[1], data[0]
        remain_data.append(data)

    with open(args.output_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['first', 'last', 'house'])
        writer.writerows(remain_data)
    
except(FileNotFoundError):
    print("File does not exsit")


