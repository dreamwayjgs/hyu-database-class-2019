from connect_db import get_db_connection
import sys


def insert():
    pass


def select():
    pass


def update():
    pass


def delete():
    pass


def main():
    if len(sys.argv) < 2:
        print("A command argument required.")
        return
    command = sys.argv[1]
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Read db lists
        if command == "insert":
            get_db_list(cur)

        # Read table list in db
        elif command == "select":
            get_table_list(cur)

        # Create table
        elif command == "update":
            print("Create table: 'example'")
            create_table(cur)
            conn.commit()

        # Drop table
        elif command == "drop":
            print("drop table: 'example'")
            drop_table(cur)
            conn.commit()

        else:
            print("Wrong command")

    except (Exception) as error:
        print("Connection Failed", error)
    finally:
        cur.close()
        conn.close()
        print("Connection Closed")


if __name__ == "__main__":
    main()
