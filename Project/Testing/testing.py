import sqlite3
from datetime import datetime


class Billy:
    def _init_(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS invoices (
                              invoice_no INTEGER PRIMARY KEY,
                              company_name TEXT,
                              product_sold TEXT,
                              amount REAL,
                              gst REAL,
                              date DATE)''')
                              
        self.conn.commit()

    def create_invoice(self, company_name, product_sold, amount, gst):
        date = datetime.now().strftime('%Y-%m-%d')
        sql = "INSERT INTO invoices (company_name, product_sold, amount, gst, date) VALUES (?, ?, ?, ?, ?)"
        val = (company_name, product_sold, amount, gst, date)
        try:
            self.cur.execute(sql, val)
            self.conn.commit()
            print("Invoice created successfully!")
        except sqlite3.Error as err:
            print("Error:", err)

    def display_invoices(self):
        self.cur.execute("SELECT * FROM invoices")
        invoices = self.cur.fetchall()
        if not invoices:
            print("No invoices found.")
        else:
            for invoice in invoices:
                print("Invoice No:", invoice[0])
                print("Company Name:", invoice[1])
                print("Product Sold:", invoice[2])
                print("Amount:", invoice[3])
                print("GST:", invoice[4])
                print("Date:", invoice[5])
                print("-------------------------")

    def close_connection(self):
        self.conn.close()


if _name_ == "_main_":
    db_file = "invoices.db"
    system = Billy(db_file)

    while True:
        print("\n1. Create Invoice")
        print("2. Display Invoices")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            company_name = input("Enter Company Name: ")
            product_sold = input("Enter Product Sold: ")

            while True:
                try:
                    amount = float(input("Enter Amount: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for amount.")

            while True:
                try:
                    gst = float(input("Enter GST: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for GST.")

            system.create_invoice(company_name, product_sold, amount, gst)
        elif choice == '2':
            system.display_invoices()
        elif choice == '3':
            system.close_connection()
            break
        else:
            print("Invalid choice. Please try again.")