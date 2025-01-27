"""
Author: Christipher Isaboke Nyangaresi
GitHub: https://github.com/chrisisaboke01
Email: isabokechris@gmail.com
Description: This script connects to a MySQL server and creates the 'alx_book_store' 
database for an online bookstore project. If the database already exists, the script 
ensures no errors occur. Error handling is included for troubleshooting.
"""

import mysql.connector
from mysql.connector import Error

def setup_bookstore_db():
    """
    This function connects to the MySQL server and creates the 'alx_book_store' database.
    """
    try:
        # Connect to MySQL server
        print("📡 Connecting to MySQL server...")
        db_connection = mysql.connector.connect(
            host="localhost",      # MySQL server host (default: localhost)
            user="root",           # Replace with your MySQL username
            password="yourpassword" # Replace with your MySQL password
        )

        if db_connection.is_connected():
            print("✅ Connection successful!")
            cursor = db_connection.cursor()

            # Create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("🎉 Database 'alx_book_store' created successfully or already exists!")

    except Error as e:
        # Print a custom error message
        print(f"🚨 Error occurred: {e}")

    finally:
        # Ensure the connection is closed
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("🔒 MySQL connection closed. Task completed!")

# Run the function
if __name__ == "__main__":
    print("✨ Starting database setup...")
    setup_bookstore_db()
