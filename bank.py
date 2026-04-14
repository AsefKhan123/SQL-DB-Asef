import sqlite3 as SQL

# Establishes the connection
connection = SQL.connect('accounts.db')
connector = connection.cursor()

# Aliasing the required SQLite functions
query = connector.execute
finish = connector.close
getRow = connector.fetchone
save = connection.commit

# Query models
INSERT = "INSERT INTO accounts (name, balance) VALUES (?, ?) RETURNING id"
SELECT = "SELECT * FROM accounts WHERE id = ?"
DELETE = "DELETE FROM accounts WHERE id = ?"
DEPOSIT = "UPDATE accounts SET Balance = Balance + ? WHERE id = ?"
WITHDRAW = "UPDATE accounts SET Balance = Balance - ? WHERE id = ?"

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
    
    # Actual query
    query(INSERT, (name, balance))
    
    # Returns the ID
    ID = getRow()[0]
    print(f"The ID for your new account: {ID}")
    #save()

# Delete an account
def delete():
    
    # Gets and validates user input
    while True:
        try:
            ID = int(input("What is the ID of the account you wish to delete? "))
        except ValueError:
            print("Try again")
        else:
            break
    
    # Queries the table for the row
    query(SELECT, (ID,))
    row = getRow()

    # Checks if the row exists
    if row is None:
        print("That row doesn't exist")
    
    # If the row does exist
    else:
        query(DELETE, (ID))
        print("That account is now deleted.")
    
    #save()

# Deposit into an account
def deposit():

    # Gets and validates user input
    while True:
        try:
            ID = int(input("What is the ID of the account you wish to deposit to? "))
            deposit = float(input("How much money do you want to deposit? $"))
        except ValueError:
            print("Try again")
        if deposit <= 0:
            print(f"You cannot deposit ${deposit}")
        else:
            break

    # Queries the table for the row
    query(SELECT, (ID,))
    row = getRow()

    # Checks if the row exists
    if row is None:
        print("That row doesn't exist")
    
    # If the row does exist
    else:
        query(DEPOSIT, (deposit, ID))
    

# Withdraw from an account
def withdraw():
    
    # Gets and validates user input
    while True:
        try:
            ID = int(input("What is the ID of the account you wish to withdraw to? "))
            deposit = float(input("How much money do you want to withdraw? $"))
        except ValueError:
            print("Try again")
        if deposit <= 0:
            print(f"You cannot deposit ${deposit}")
        else:
            break

    # Queries the table for the row
    query(SELECT, (ID,))
    row = getRow()

    # Checks if the row exists
    if row is None:
        print("That row doesn't exist")
    
    # If the row does exist
    else:
        query(WITHDRAW, (deposit, ID))

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
save()
withdraw()
save()