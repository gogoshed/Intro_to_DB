# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    """Creates the alx_book_store database safely."""
    try:
        # Connect to MySQL server (no specific database)
        connection = mysql.connector.connect(
            host='localhost',        # MySQL host
            user='root',             # Your MySQL username
            password='Edekodov1@' # Your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database only if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close cursor and connection properly
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
