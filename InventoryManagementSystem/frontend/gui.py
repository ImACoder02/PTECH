import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from backend.db import Database


class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.db = Database()

        # UI Components
        self.product_name_label = tk.Label(root, text="Product Name:")
        self.product_name_label.grid(row=0, column=0)
        self.product_name_entry = tk.Entry(root)
        self.product_name_entry.grid(row=0, column=1)

        self.category_label = tk.Label(root, text="Category:")
        self.category_label.grid(row=1, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1)

        self.price_label = tk.Label(root, text="Price:")
        self.price_label.grid(row=2, column=0)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=2, column=1)

        self.stock_quantity_label = tk.Label(root, text="Stock Quantity:")
        self.stock_quantity_label.grid(row=3, column=0)
        self.stock_quantity_entry = tk.Entry(root)
        self.stock_quantity_entry.grid(row=3, column=1)

        # Buttons
        self.add_button = tk.Button(root, text="Add Product", command=self.add_product)
        self.add_button.grid(row=4, column=0)

        self.update_button = tk.Button(root, text="Update Product", command=self.update_product)
        self.update_button.grid(row=4, column=1)

        self.delete_button = tk.Button(root, text="Delete Product", command=self.delete_product)
        self.delete_button.grid(row=5, column=0)

        self.view_button = tk.Button(root, text="View Inventory", command=self.view_inventory)
        self.view_button.grid(row=5, column=1)

        # Listbox to display products
        self.product_listbox = tk.Listbox(root, height=10, width=50)
        self.product_listbox.grid(row=6, column=0, columnspan=2)

    def add_product(self):
        product_name = self.product_name_entry.get()
        category = self.category_entry.get()
        try:
            price = float(self.price_entry.get())
            stock_quantity = int(self.stock_quantity_entry.get())
            self.db.add_product(product_name, category, price, stock_quantity)
            messagebox.showinfo("Success", "Product added successfully!")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid price and quantity.")

    def update_product(self):
        try:
            selected_item = self.product_listbox.curselection()
            if selected_item:
                product_id = self.product_listbox.get(selected_item)[0]  # Get product id from listbox item
                product_name = self.product_name_entry.get()
                category = self.category_entry.get()
                price = float(self.price_entry.get())
                stock_quantity = int(self.stock_quantity_entry.get())
                self.db.update_product(product_id, product_name, category, price, stock_quantity)
                messagebox.showinfo("Success", "Product updated successfully!")
            else:
                messagebox.showerror("No Selection", "Please select a product to update.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid price and quantity.")

    def delete_product(self):
        try:
            selected_item = self.product_listbox.curselection()
            if selected_item:
                product_id = self.product_listbox.get(selected_item)[0]  # Get product id from listbox item
                self.db.delete_product(product_id)
                messagebox.showinfo("Success", "Product deleted successfully!")
            else:
                messagebox.showerror("No Selection", "Please select a product to delete.")
        except ValueError:
            messagebox.showerror("Error", "An error occurred during deletion.")

    def view_inventory(self):
        inventory = self.db.fetch_products()
        self.product_listbox.delete(0, tk.END)  # Clear previous list
        for product in inventory:
            self.product_listbox.insert(tk.END, f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Price: ${product[3]:.2f}, Stock: {product[4]}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
