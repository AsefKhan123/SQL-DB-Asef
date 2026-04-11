import sqlite3 as SQL

# Establishes the connection
connection = SQL.connect('accounts.db')
connector = connection.cursor()

# Aliasing the required SQLite functions
query = connector.execute
finish = connector.close
getRow = connector.fetchone

# Query models
INSERT = "INSERT INTO accounts (name, balance) VALUES (?, ?) RETURNING ID"

# Create an account
def create():
    
    # Gets and validates user input
    while True:
        try:
            name = str(input("What will be the name? "))
            balance = float(input("What is the initial balance? $"))
        except ValueError:
            print("Try again")
        else:
            break
    
    # Makes the values readable by SQLite
    VALUES = (name, balance)
    
    # Actual query
    query(INSERT, VALUES)
    
    # Returns the ID
    newRow = getRow()
    if newRow:
        ID = newRow[0]
        print(f"The ID for your new account: {ID}")

# Delete an account
def delete():

# Deposit into an account
def deposit():
    pass

# Withdraw from an account
def withdraw():
    pass

# Search for an account
def search():
    pass

"""print("Welcome to your banking services! How may we help you?")
print("1. Deposit into your account")
print("2. Withdraw from your account")
print("3. Create a new account")
print("4. Delete an account")
print("5. Exit")"""

create()
