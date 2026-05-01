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

# Aliasing OS.system("clear") to make it easy to write
clear = lambda: OS.system('clear')

# Query models
CREATE = "INSERT INTO accounts (name, balance) VALUES (?, ?) RETURNING id"
ID = "SELECT * FROM accounts WHERE (id = ?)"
DELETE = "DELETE FROM accounts WHERE (id = ?)"
DEPOSIT = "UPDATE accounts SET Balance = ? WHERE id = ?"
WITHDRAW = "UPDATE accounts SET Balance = ? WHERE id = ?"
NAME = "SELECT * FROM accounts WHERE (Name = ?)"
BALANCE = "SELECT * FROM accounts WHERE (?)"

# Create an account
def create():
    clear()

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
    query(CREATE, (name, balance))
    
    # Returns the ID
    row = getRow()
    ID = row[0]
    print(f"The ID for your new account: {ID}")
    pause(5)
    save()
    clear()
    menu()

# Delete an account
def delete():
    clear()

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
    clear()
    menu()

# Deposit into an account
def deposit():
    clear()

    # Gets and validates user input
    while True:
        try:
            id = int(input("What is the ID of the account you wish to deposit to? "))
            deposit = float(input("How much money do you want to deposit? $"))
        
            if deposit <= 0:
                print(f"You cannot deposit ${deposit}")

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
        newBalance = row[2] + deposit
        query(DEPOSIT, (newBalance, id))
        print(f"Successfully deposited ${deposit} into Account #{id}")
        pause(1)
    save()
    clear()
    menu()

# Withdraw from an account
def withdraw():
    clear()
    
    # Gets and validates user input
    while True:
        try:
            id = int(input("What is the ID of the account you wish to withdraw from? "))
            withdrawal = float(input("How much money do you want to withdraw? $"))
    
            if withdrawal <= 0:
                print(f"You cannot withdraw ${withdrawal}")
    
        except ValueError:
            clear()
            print("Try again")
            pause(1)
            clear()
        else:
            break

    # Queries the table for the row
    query(ID, (id,))
    row = getRow()
    
    # Checks if the withdrawal is possible
    if row is None:
        print("That row doesn't exist")
    else:
        pause(1)
        balance = row[2]
    
        if withdrawal > balance:
            print(f"You only have ${balance:.1f}.")
        else:
            newBalance = balance - withdrawal
            query(WITHDRAW, (newBalance, id))
            print(f"Successfully withdrew ${withdrawal:.1f} from Account #{id}")
            pause(5)
        save()
        clear()
        menu()

# Search for an account
def search():
    clear()
    
    # Input validation
    while True:
        filter = input("What would you like to search by? ID, or name? ").lower().strip()
        
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
            query(NAME, (name, ))
            rows = getAll()
            break
    
    clear()

    # Prints the rows if exists
    if rows is None:
        print("No accounts match your search. Please try again.")
        pause(1)
        clear()
        menu()

    # If rows exist
    else:
        print("Retrieving all accounts that match the filter...")
        pause(1)
        OS.system("clear")
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Balance: ${row[2]:.2f}")
            print("------------------")
    
        pause(10)
        clear()
    menu()

# Welcome menu
def menu():
    
    while True:
        try:
            print("Welcome to your banking services! How may we help you?")
            print("1. Deposit into your account")
            print("2. Withdraw from your account")
            print("3. Create a new account")
            print("4. Delete an account")
            print("5. Filter all accounts")
            print("6. Exit")
            option = int(input("What would you like to do? "))
        except ValueError:
            clear()
        else:
            break
        
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
        clear()
    else:
        clear()
        print("That's not a valid option. ")
        pause(1)
        clear()
        menu()

clear()
print("Logging you in right now...")
pause(1)
clear()
menu()
