import mysql.connector

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "bluestocks"


def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,        # change if needed
        password=DB_PASSWORD,    # change if needed
        database=DB_NAME
    )
