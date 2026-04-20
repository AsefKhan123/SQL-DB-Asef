import sqlite3 as SQL, os as OS
from time import sleep as pause

# Establishes the connection
connection = SQL.connect('accounts.db')
connector = connection.cursor()

# Aliasing the required SQLite functions
query = connector.execute
finish = connector.close
getRow = connector.fetchone
save = connection.commit
getAll = connector.fetchall

# Query models
ADD = "INSERT INTO accounts (name, balance) VALUES (?, ?) RETURNING id"
ID = "SELECT * FROM accounts WHERE (id = ?)"
DELETE = "DELETE FROM accounts WHERE (id = ?)"
DEPOSIT = "UPDATE accounts SET Balance = (Balance + ?) WHERE id = ?"
WITHDRAW = "UPDATE accounts SET Balance = (Balance - ?) WHERE id = ?"
NAME = "SELECT * FROM accounts WHERE (Name = ?)"

# Create an account
def create():
    OS.system("clear")

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
    query(ADD, (name, balance))
    
    # Returns the ID
    ID = getRow()[0]
    print(f"The ID for your new account: {ID}")
    save()
    OS.system("clear")
    menu()

# Delete an account
def delete():
    OS.system("clear")

    
    # Gets and validates user input
    while True:
        try:
            id = int(input("What is the ID of the account you wish to delete? "))
        except ValueError:
            print("Try again")
        else:
            break
    
    # Queries the table for the row
    query(ID, (id,))
    row = getRow()

    # Checks if the row exists
    if row is None:
        print("That row doesn't exist")
    
    # If the row does exist
    else:
        query(DELETE, (ID,))
        print("That account is now deleted.")
    
    save()
    OS.system("clear")
    menu()

# Deposit into an account
def deposit():
    OS.system("clear")

    # Gets and validates user input
    while True:
        try:
            id = int(input("What is the ID of the account you wish to deposit to? "))
            deposit = float(input("How much money do you want to deposit? $"))
        except ValueError:
            print("Try again")
        if deposit <= 0:
            print(f"You cannot deposit ${deposit}")
        else:
            break

    # Queries the table for the row
    query(ID, (id,))
    row = getRow()

    # Checks if the row exists
    if row is None:
        print("That row doesn't exist")
    
    # If the row does exist
    else:
        query(DEPOSIT, (deposit, ID))
    save()
    OS.system("clear")
    menu()

# Withdraw from an account
def withdraw():
    OS.system("clear")
    
    # Gets and validates user input
    while True:
        try:
            id = int(input("What is the ID of the account you wish to withdraw from? "))
            withdrawal = float(input("How much money do you want to withdraw? $"))
        except ValueError:
            print("Try again")
        if withdrawal <= 0:
            print(f"You cannot withdraw ${withdrawal}")
        else:
            break

    # Queries the table for the row
    query(ID, (id,))
    row = getRow()
    
    # Checks if the withdrawal is possible
    if row is None:
        print("That row doesn't exist")
    else:
        balance = row[2]
    
        if withdrawal > balance:
            print(f"You only have ${balance}.")
        else:
            query(WITHDRAW, (withdrawal, ID))
        save()
        OS.system("clear")
        menu()

# Search for an account
def search():
    OS.system("clear")
    
    # Input validation
    while True:
        filter = input("What would you like to search by? ID or name? ").lower()
        
        if filter != "name" and filter != "id":
            print("That isn't a valid filter.")

        else:
            break
    
    # Finds all rows with the matching condition
    while True:
        if filter == "id":
            try:
                id = int(input("What ID would you like to search? "))
            except ValueError:
                print("Invalid ID. Please try again.")
            else:
                query(ID, (id, ))
                rows = getAll()
                break
            
        elif filter == "name":
            name = str(input("What name would you like to search? "))
            query(NAME, (name))
            rows = getAll()
            break
    
    # Prints the rows if exists
    if rows is None:
        print("No accounts match your search. Please try again.")
    else:
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Balance: {row[2]}")
    
    OS.system("clear")
    menu()

# Welcome menu
def menu():
    print("Welcome to your banking services! How may we help you?")
    print("1. Deposit into your account")
    print("2. Withdraw from your account")
    print("3. Create a new account")
    print("4. Delete an account")
    print("5. Filter all accounts")
    print("6. Exit")
    
    option = int(input("What would you like to do? "))
    
    if option == 1:
       deposit()
    elif option == 2:
        withdraw()
    elif option == 3:
        create()
    elif option == 4:
        delete()
    elif option == 5:
        search()
    elif option == 6:
        print("Thank you for using our services. Logging you off right now!")
        save()
        finish()
        pause(1)
        OS.system("clear")
    else:
        print("That's not a valid option. ")

print("Logging you in right now...")
pause(1)
OS.system("clear")
menu()