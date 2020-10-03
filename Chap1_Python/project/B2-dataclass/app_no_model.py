from csv_helper import read_csv
import argparse


def find_bank(code):
    banks = read_csv("data/bank.csv")
    for bank in banks[1:]:
        if code == bank[1]:
            return bank[2]
    return ""


def find_customer(code, account_num):
    customers = read_csv("data/customers.csv")
    for customer in customers[1:]:
        c_code = customer[5]
        c_acc_num = customer[6]
        if c_code == code and c_acc_num == account_num:
            return customer, customers
    return {}, []


def find_customer_info(code, account_num):
    bank_name = find_bank(code)
    customer, customers = find_customer(code, account_num)
    return bank_name, customer, customers


def show_customer_info(code, account_num):
    bank_name, customer, _ = find_customer_info(code, account_num)
    if not bank_name:
        return f"ERROR: No such bank code: {code}"
    if not customer:
        return f"ERROR: No such customer having {code}, {account_num}"
    return f"name: {customer[0]}, phone: {customer[1]}, email: {customer[2]}@{customer[3]}, bank_name: {bank_name}, balance: {customer[7]}"


def main(args):
    code = args.bank_code
    account_num = args.account_num
    print(show_customer_info(code, account_num))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bank_code", help="Bank code")
    parser.add_argument("account_num", help="Account number")
    args = parser.parse_args()
    print("ARGS: ", args)
    main(args)
