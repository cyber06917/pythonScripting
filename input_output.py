import argparse
import sys

try:

    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)


    parser = argparse.ArgumentParser()
    parser.add_argument('file')

    args = parser.parse_args()

    if not args.file.endswith(".py"):
        print("Not a python file")
        sys.exit(1)

    with open(args.file, "r") as py_file:
        count = 0
        for line in py_file:
            stripped = line.strip()
            if not stripped:
                continue
            elif stripped.startswith("#"):
                continue
            else:
                count += 1
        print(count)
    
except(FileNotFoundError):
    print("File does not exsit")


