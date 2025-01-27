import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",      # Change this if your MySQL server is on another host
            user="root",           # Replace with your MySQL username
            password="yourpassword" # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Ensure the connection is closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Run the function to create the database
if __name__ == "__main__":
    create_database()
