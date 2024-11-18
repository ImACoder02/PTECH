import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',  # Change as needed
                user='root',       # Your database username
                password='',       # Your database password
                database='inventory_management'  # Database name
            )
            if self.connection.is_connected():
                print("Connected to MySQL Database")
        except Error as e:
            print(f"Error: {e}")
            raise

    def add_product(self, product_name, category, price, stock_quantity):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO products (product_name, category, price, stock_quantity) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (product_name, category, price, stock_quantity))
            self.connection.commit()
        except Error as e:
            print(f"Error: {e}")
            raise

    def fetch_products(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM products"
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
            raise

    def update_product(self, product_id, product_name, category, price, stock_quantity):
        try:
            cursor = self.connection.cursor()
            query = """UPDATE products SET product_name=%s, category=%s, price=%s, stock_quantity=%s WHERE id=%s"""
            cursor.execute(query, (product_name, category, price, stock_quantity, product_id))
            self.connection.commit()
        except Error as e:
            print(f"Error: {e}")
            raise
    
    def delete_product(self, product_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM products WHERE id=%s"
            cursor.execute(query, (product_id,))
            self.connection.commit()
        except Error as e:
            print(f"Error: {e}")
            raise
