import csv  # CSV https://docs.python.org/ko/3/library/csv.html?highlight=csv
from pprint import pprint  # PrettyPrinter https://docs.python.org/ko/3/library/pprint.html


def read_csv(filename):
    rows = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    return rows


def write_csv(filename, write_rows):
    with open(filename, "w") as csvfile:
        writer = csv.writer(csvfile)
        for row in write_rows:
            writer.writerow(row)


def main():
    read_filename = "bank.csv"
    rows = read_csv(read_filename)
    pprint(rows)
    print(type(rows))
    print(type(rows[0]))

    write_filename = "hello.csv"
    write_rows = [["1", "hello", "world"], ["2", "안녕", "세상"]]
    write_csv(write_filename, write_rows)


if __name__ == "__main__":
    main()
