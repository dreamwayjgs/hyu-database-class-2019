from .connect_db import get_db_connection


def insert(name, email, password):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        print("INSERT QUERY", name, email, password)
        sql = "INSERT INTO student (name, email, password) VALUES (%s, %s, %s)"
        cur.execute(sql, (name, email, password))
        conn.commit()
    except (Exception) as error:
        print("Connection Failed", error)
    finally:
        cur.close()
        conn.close()
        print("Connection Closed")


def select():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        print("SELECT QUERY")
        sql = "SELECT * FROM student"
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)
        return rows
    except (Exception) as error:
        print("Connection Failed", error)
    finally:
        cur.close()
        conn.close()
        print("Connection Closed")
