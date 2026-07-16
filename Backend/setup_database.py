import mysql.connector

from db_config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER


def setup_database():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
    )
    cursor = conn.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ml (
            id INT AUTO_INCREMENT PRIMARY KEY,
            company_id VARCHAR(50) UNIQUE,
            company_name VARCHAR(100),
            roe FLOAT,
            roce FLOAT,
            net_profit FLOAT,
            pros TEXT,
            cons TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ON UPDATE CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    cursor.close()
    conn.close()
    print("Database table is ready.")


if __name__ == "__main__":
    setup_database()
