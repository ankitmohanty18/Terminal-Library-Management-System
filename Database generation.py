import sqlite3

conn = sqlite3.connect("test1.db")
c = conn.cursor()

c.execute('''CREATE TABLE Librarian
        (Name TEXT NOT NULL, 
        Address TEXT, 
        Contact INT)''')
print("Table Librarian created successfully.")
c.execute('''CREATE TABLE User
        (Name TEXT NOT NULL, 
        Address TEXT, 
        Contact INT, 
        Registered_name TEXT, 
        Password TEXT)''')
print("Table User created successfully.")
c.execute('''CREATE TABLE Books
        (Name TEXT NOT NULL, 
        Author TEXT,
        Publishing_Company TEXT,
        Rented_date TEXT,
        Rented_User TEXT)''')
print("Table Books created successfully.")

c.close()
conn.close()


