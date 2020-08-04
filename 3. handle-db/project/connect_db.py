import psycopg2 as pg

# default postgres settings
db_connection_info = {"host": "localhost", "user": "postgres", "dbname": "postgres", "port": 5432}

# TODO: Override connection info
# when postgres runs on docker container
db_connection_info["host"] = "host.docker.internal"
db_connection_info["port"] = 54320
db_connection_info["password"] = 1234

db_connection_str = "host={host} user={user} dbname={dbname} password={password} port={port}".format(
    **db_connection_info
)


def get_db_connection():
    print("Connecting To: ", db_connection_str)
    conn = pg.connect(db_connection_str)
    return conn
