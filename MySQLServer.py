import mysql.connector

try:
    # Replace 'your_username' and 'your_password' with your MySQL credentials
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password"
    )
    cursor = connection.cursor()

    # Create the database if it does not exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")

finally:
    # Close cursor and connection if they exist
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
