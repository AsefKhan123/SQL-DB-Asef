# Code2College Elite 102 Banking Project

## Intro
This project showcases a mockup of a bank application. It allows the user to create accounts, delete them, withdraw from and deposit to them, and search through them for a given condition. It allows the user to do all of these in a simple, easy-to-use menu with pleasing UI.

## Tools and Modules
I used the sqlite3 module for this project, which is the most important module because it's the way I used to make Python communicate with the database. 
In addition, I also used the time module's .sleep() function and the os module's .system("clear") to make the UX more pleasing and easy-to-understand, as they let the user see the information the program created given their inputs before clearing the screen and reprinting the menu. Otherwise, the terminal would've been very messy as previous menu() calls would stay and confuse the user on where to look.

## How to Run
To run the project, simply click Run and wait for the menu to print. Then, enter the number corresponding to the desired option in the field, which will then clear the function and trigger the desired function, which will then take any neccessary inputs the user will provide and use it to perform the desired operation. After that, it will take you back to the menu, where the cycle repeats itself with a new option.

## Overview of the functions
The five functions and their purposes go as follows:
1. deposit(): Lets the user deposit money into an account given its ID
2. withdraw(): Lets the user withdraw money from an account given its ID
3. create(): Lets the user create an account given their name and initial balance
4. delete(): Lets the user delete an account given its ID
5. search(): Lets the user see all accounts based on a certain ID or name

The next five sections will delve deeper into how each function runs.

### deposit()
The deposit() function begins by asking the user for the ID of the account they wish to deposit to as an integer and how much they want to deposit as a float. If the user enters values that cannot be cast as an integer and float respectively, the function will reprompt the user for the correct input.
After the user has entered an ID and a dollar amount, the function will SELECT for all acccounts (rows) in the database using the ID query and the given ID. If no row exists with that ID, the function says so before returning the user back to the menu. 
If the row does exist, the function wlll perform the DEPOSIT query, which will UPDATE the Balance column with the sum of the current value and the deposit, save it and return the user back to the menu.

### withdraw()
The withdraw() function begins by asking the user for the ID of the account they wish to withdraw from as an integer and how much they want to withdraw as a float. If the user enters values that cannot be cast as an integer and float respectively, the function will reprompt the user for the correct input.
After the user has entered an ID and a dollar amount, the function will SELECT for all acccounts (rows) in the database using the ID query and the given ID. If no row exists with that ID, the function says so before returning the user back to the menu. 
If the row does exist, the function wlll perform the WITHDRAW query, which will UPDATE the Balance column with the diiference of the current value and the withdrawal, save it and return the user back to the menu.

### create()
The create() function begins by asking the user for their name as a string and the initial deposit as a float. If the user enters values that cannot be cast as a string and float respectively, the function will reprompt the user for the correct input.
After the user has entered their name and initial deposit, the function will run the CREATE query, which will INSERT a new account (row) in the database. The function then prints the account's ID for future reference and returns the user back to the menu.

### delete()
The delete() function starts by asking the user for the ID of the account they wish to delete as an integer. If the user enters a value that cannot be cast as an integer, the function will reprompt the user for the correct input.
After the user has entered the ID, the function will SELECT the account (row) with the given ID. If the row doesn't exist, the function will print so and return the user back to the menu. Otherwise, the function will run the DELETE query, which will DELETE the row whose ID matches with the user-given ID and return the user back to the menu.

### search()
The search() function begins by asking whether the user will search by ID or name of the holder. If the user enters anything but "name" and "id" after lowercasing the enterred input, the function will reprompt the user for the correct keyword.
After the user enters the correct keyword, the function will which keyword is entered. If "id" was entered, the function will run the ID query, which will SELECT all accounts (rows) in the database with the matching ID, display it to the user and return them back to the menu.
However, if the user entered "name", the function will run the NAME query, which will SELECT all accounts (rows) in the database, display them to the user and return them back to the menu.

## Future Extensions
I plan on extending the search() function so it also allows the user to search for all accounts (rows) given a balance and whether the function should SELECT all accounts with balances less than, greater than, or equal to the given balance.
