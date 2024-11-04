from gettext import install
from turtle import pd
import pandas
import pip
#importing libraries 

pip; install; pandas

#Installing Pandas extention

import sqlite3
# Making the database file
def create_database():
    conn = sqlite3.connect('finance_manager.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE transactions
                 (id INTEGER PRIMARY KEY, 
                 date TEXT, 
                 description TEXT, 
                 amount REAL, 
                 category TEXT)''')
    conn.commit()
    conn.close()

create_database()
#creating the table of each expense
def add_transaction(date, description, amount, category):
    conn = sqlite3.connect('finance_manager.db')
    c = conn.cursor()
    c.execute("INSERT INTO transactions (date, description, amount, category) VALUES (?, ?, ?, ?)",
              (date, description, amount, category))
    conn.commit()
    conn.close()
#viewing individual transactions in each category 
def view_transactions():

    conn = sqlite3.connect('finance_manager.db')
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    rows = c.fetchall()
    conn.close()
    for row in rows:
        print(row)
#categorizing expenses
def create_categories():
    categories = ['Food', 'Housing', 'Transportation', 'Utilities', 'Entertainment', 'Savings', 'Debt', 'Healthcare', 'Personal', 'Miscellaneous']
    conn = sqlite3.connect('finance_manager.db')
    c = conn.cursor()
    for category in categories:
        c.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (category,))
    conn.commit()
    conn.close()

    import pandas as pd
#creating a basic UI to recieve inputs
def menu():
    while True:
        print("\n1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_transaction(date, description, amount, category)
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

def generate_report():      # report generation
    conn = sqlite3.connect('finance_manager.db')
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    print(df.groupby('category').sum()['amount'])
    conn.close()

if __name__ == "__main__":
    create_categories()  # Only run once
    menu()
