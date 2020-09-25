from helpers.connect_db import get_db_connection


def create_table(cur):
    sql = """
        CREATE TABLE student (
            id serial primary key,
            name varchar,
            email varchar unique,            
            password varchar
        )
        """
    cur.execute(sql)


def run():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        create_table(cur)
        conn.commit()

        cur.close()
        conn.close()
        print("Connection Closed")
    except (Exception) as error:
        print("Connection Failed", error)


if __name__ == "__main__":
    run()
