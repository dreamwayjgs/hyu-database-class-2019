from csv_helper import read_csv, write_csv
import argparse
from pprint import pprint
from models import Bank, Customer


def create_bankdb():
    banks = read_csv("data/bank.csv")
    banktable = []
    for bank in banks[1:]:
        banktable.append(Bank(*bank))
    return banktable


def create_customerdb():
    customers = read_csv("data/customers.csv")
    customertable = []
    for customer in customers[1:]:
        customertable.append(Customer(*customer))
    return customertable


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

    return bank, customer


def transfer(code, account_num, amount, db):
    bank, customer = find_customer_info(code, account_num, db)
    if not bank:
        return f"ERROR: No such bank code: {code}"
    if not customer:
        return f"ERROR: No such customer having {code}, {account_num}"

    customer.balance += amount
    print("after", customer)
    pprint(db[1])
    # write_csv("data/customers.csv", customers)


def main(args):
    code = int(args.bank_code)
    account_num = args.account_num
    amount = int(args.amount) if args.amount else 0

    banktable = create_bankdb()
    customertable = create_customerdb()

    if amount == 0:
        _, customer = find_customer_info(code, account_num, (banktable, customertable))
        print(customer)
    else:
        transfer(code, account_num, amount, (banktable, customertable))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bank_code", help="Bank code")
    parser.add_argument("account_num", help="Account number")
    parser.add_argument("-a", "--amount", help="Wire transfer amount")
    args = parser.parse_args()
    print("ARGS: ", args)
    main(args)
