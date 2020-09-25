from connect_db import get_db_connection
import sys


def get_db_list(cur):
    sql = "SELECT datname FROM pg_database"
    cur.execute(sql)
    print("=== DB LIST ===")
    for rows in cur.fetchall():
        print(rows)


def get_table_list(cur):
    sql = """
        SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """
    cur.execute(sql)
    print("=== TABLE LIST ===")
    for rows in cur.fetchall():
        print(rows)


def create_table(cur):
    sql = """
        CREATE TABLE example (
            id integer primary key,
            name varchar
        )
    """
    cur.execute(sql)


def drop_table(cur):
    sql = "DROP TABLE example"
    cur.execute(sql)


def main():
    if len(sys.argv) < 2:
        print("A command argument required.")
        return
    command = sys.argv[1]
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Read db lists
        if command == "dbs":
            get_db_list(cur)

        # Read table list in db
        elif command == "tables":
            get_table_list(cur)

        # Create table
        elif command == "create":
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

        print("Job's done")
        cur.close()
        conn.close()
        print("Connection Closed")
    except (Exception) as error:
        print("Connection Failed", error)


if __name__ == "__main__":
    main()
