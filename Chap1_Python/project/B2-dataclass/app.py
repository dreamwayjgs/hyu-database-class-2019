from csv_helper import read_csv
import argparse
from models import Bank, Customer


def create_table(filename, Cls):
    data = read_csv(filename)
    header = data[0]
    table = []
    for item in data[1:]:
        table.append(Cls(*item))
    return header, table


def find_bank(code, banktable):
    for bank in banktable:
        if bank.code == code:
            return bank
    return {}


def find_customer(code, account_num, customertable):
    for customer in customertable:
        if customer.bankid == code and customer.accountnum == account_num:
            return customer
    return {}


def find_customer_info(code, account_num, db):
    banktable, customertable = db
    bank = find_bank(code, banktable)
    if not bank:
        return f"ERROR: No such bank code: {code}"

    customer = find_customer(code, account_num, customertable)
    if not customer:
        return f"ERROR: No such customer having {code}, {account_num}"

    return f"{customer}, bank_name: {bank.name}"


def main(args):
    code = int(args.bank_code)
    account_num = args.account_num

    _, banktable = create_table("data/bank.csv", Bank)
    _, customertable = create_table("data/customers.csv", Customer)
    customer = find_customer_info(code, account_num, (banktable, customertable))
    print(customer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bank_code", help="Bank code")
    parser.add_argument("account_num", help="Account number")
    args = parser.parse_args()
    print("ARGS: ", args)
    main(args)
