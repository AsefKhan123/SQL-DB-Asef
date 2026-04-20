# Initializes and updates the table
import sqlite3

DB_NAME = 'accounts.db'

def initialize_database():

    # Connecting to the database
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE accounts
                ''')

    # Create the table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts
            (id integer primary key, 
            Name text, 
            Balance real)
''')

    # Commit the changes and end the connection
    connection.commit()
    connection.close()


initialize_database()
