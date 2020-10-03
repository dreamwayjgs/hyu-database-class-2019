import csv  # CSV https://docs.python.org/ko/3/library/csv.html?highlight=csv
import os


def read_csv(filename):
    rows = []
    print(f"Reading: {os.getcwd()}/{filename}")
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    return rows


def write_csv(filename, write_rows):
    print(f"Writing: {os.getcwd()}/{filename}")
    with open(filename, "w") as csvfile:
        writer = csv.writer(csvfile)
        for row in write_rows:
            writer.writerow(row)
