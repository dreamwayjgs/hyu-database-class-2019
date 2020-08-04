from connect_db import get_db_connection
import sys


def insert(cur):
    sql = "INSERT INTO example (id, name) VALUES (1, 'sample')"
    cur.execute(sql)


def insert_with_parameters(cur, id, name):
    sql = "INSERT INTO example (id, name) VALUES (%s, %s)"
    cur.execute(sql, (id, name))


def select(cur):
    sql = "SELECT * FROM example"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def update(cur):
    sql = "UPDATE example SET name = 'updated sample' where id = 1"
    cur.execute(sql)


def update_with_parameters(cur, id, name):
    sql = "UPDATE example SET name = %s where id = %s"
    cur.execute(sql, (name, id))


def delete(cur):
    sql = "DELETE FROM example WHERE id = 1"
    cur.execute(sql)


def delete_with_parameters(cur, id):
    sql = "DELETE FROM example WHERE id = %s"
    cur.execute(sql, [id])


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
            if len(sys.argv) == 4:
                id = sys.argv[2]
                name = sys.argv[3]
                insert_with_parameters(cur, id, name)
            else:
                insert(cur)
            conn.commit()

        # Read table list in db
        elif command == "select":
            select(cur)

        # Create table
        elif command == "update":
            if len(sys.argv) == 4:
                id = sys.argv[2]
                name = sys.argv[3]
                update_with_parameters(cur, id, name)
            else:
                update(cur)
            conn.commit()

        # Drop table
        elif command == "delete":
            if len(sys.argv) == 3:
                id = sys.argv[2]
                delete_with_parameters(cur, id)
            else:
                delete(cur)
            conn.commit()

        else:
            print("Wrong command")

        print("Job's done")
    except (Exception) as error:
        print("Connection Failed", error)
    finally:
        cur.close()
        conn.close()
        print("Connection Closed")


if __name__ == "__main__":
    main()
