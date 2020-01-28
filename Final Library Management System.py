dimport sqlite3
from datetime import datetime
from datetime import date

conn = sqlite3.connect("test1.db")
c = conn.cursor()


def insert_book(name, author, pub, rentdate, rentuser):
    c.execute(''' INSERT INTO Books (Name, Author, Publishing_company, Rented_date, Rented_user)
                    VALUES(?,?,?,?,?)''', (name, author, pub, rentdate, rentuser))
    conn.commit()
    print(name, "added successfully.")


def insert_user(name, add, cont, reg_name, pw):
    c.execute(''' INSERT INTO User (Name, Address, Contact, Registered_name, Password)
                    VALUES(?,?,?,?,?)''', (name, add, cont, reg_name, pw))
    conn.commit()
    print(name, "added successfully.")


def insert_lib(name, add, contact):
    c.execute(''' INSERT INTO Librarian (Name, Address, Contact)
                        VALUES(?,?,?)''', (name, add, contact))
    conn.commit()
    print(name, "added successfully.")


def rent_book(new_date,new_user,ch_bookname):
    # print(new_date)
    c.execute('''UPDATE Books SET Rented_date = (?), Rented_User = (?) 
            WHERE Name = (?) ''', (new_date,new_user, ch_bookname))
    conn.commit()
    print("Book details updated successfully")


def update_book(new_name,new_author, new_pub,ch_bookname):
    c.execute('''UPDATE Books SET Name = (?), Author = (?), Publishing_Company = (?)
            WHERE Name = (?) ''', (new_name,new_author, new_pub, ch_bookname))
    conn.commit()
    print("Book details updated successfully")

def update_user(new_add,new_contact,ch_name):
    # print(new_date)
    c.execute('''UPDATE User SET Address = (?), Contact = (?) 
            WHERE Name = (?) ''', (new_add,new_contact,ch_name))
    conn.commit()
    print("User details updated successfully")


def del_book(del_name):
    c.execute('''DELETE FROM Books WHERE Name = (?) ''', (del_name,))
    conn.commit()
    print(del_name, "deleted successfully.")


def del_user(del_name):
    c.execute('''DELETE FROM User WHERE Name = (?) ''', (del_name,))
    conn.commit()
    print(del_name, "deleted successfully.")


def username_from_db(arg):
    c.execute("SELECT Registered_name FROM User")
    g = c.fetchall()
    list_username = []
    for i in g:
        for j in i:
            list_username.append(j)
    if arg in list_username:
        return True
    else:
        return False


def password_from_db(arg):
    c.execute("SELECT Password FROM User")
    g = c.fetchall()
    list_password = []
    for i in g:
        for j in i:
            list_password.append(j)
    if arg in list_password:
        return True
    else:
        return False


# Subtracting dates
def count_amount(number):
    k = 0
    if number > 20:
        k += 20
        if number > 20 and number < 25:
            k += 0
        if number > 24 and number < 30:
            k += 25
        if number > 29 and number < 35:
            k += 30 + 25
        if number > 34 and number < 40:
            k += 30 + 25 + 35
        if number > 39 and number < 45:
            k += 30 + 25 + 35 + 40
    elif number < 20:
        print("NO DUES")
    elif number > 44:
        k = k-20
        print("Contact Librarian")

    print("You have to pay", k, "Rupees")


## START OF VIEW.........................................................
print('''
Hello, Welcome to the library management system.
If you are a user, Enter 1
If you are a librarian, Enter 2''')
p0 = int(input(">"))
if p0 == 1:
    username = input("Username:")
    pw = input("Password:")

    check_username = username_from_db(username)
    check_pw = password_from_db(pw)
    if check_username and check_pw == True:
        print('''You are logged in :)
        Enter 1 for renting books
        Enter 2 for returning books''')
        q1 = int(input(">"))
        Exit = False
        if q1 == 1:
            while Exit == False:
                to_be_rented = input("Which book do you want to rent?")
                n_date = input("Enter the date(dd/mm/yyyy):")
                n_user = input("Enter your username:")
                rent_book(n_date, n_user, to_be_rented)
                print("Do you wish to rent another?")
                a1 = input("Enter Yes/No").lower()
                if a1 == "no":
                    Exit = True
                else:
                    continue
        elif q1 == 2:
            while Exit == False:
                rentedbookname = input("Which book do you wish to return?")
                d_borrow = c.execute('''SELECT Rented_date FROM Books WHERE Name = (?)''', (rentedbookname,))
                et = str(d_borrow.fetchall()[0][0])
                # print(et)
                T = date.today()
                T2 = str(T)
                e = datetime.strptime(T2, "%Y-%m-%d")
                d = datetime.strptime(et, "%d/%m/%Y")
                t = str(e - d)
                y = t[0:-14]    #no of days rented
                y_int = int(y)
                print("Number of days rented:", y , "days")
                count_amount(y_int)


                Exit = True
    elif check_pw == False:
        print("Incorrect password!")
    elif check_username == False:
        print("Incorrect username!")
    else:
        print("Invalid values")

elif p0 == 2:
    print('''
    Enter 1 for adding user/librarian/books
    Enter 2 for updating user/book details
    Enter 3 for deleting users/books
    Enter 4 for viewing the details of books
    ''')
    p1 = int(input(">"))
    if p1 == 1:
        print('''
        Enter 1 for adding users,
        Enter 2 for adding librarians,
        Enter 3 for adding books''')
        pp1 = int(input(">"))
        Exit = False
        while Exit == False:
            if pp1 == 1:
                #Adding users
                user_name = input("Name:")
                address = input("Address:")
                phone = input("Phone number:")
                reg_n = input("Registration Name:")
                password = input("Password:")
                insert_user(user_name, address, phone, reg_n, password)
                print("Do you wish to add another?")
                a1 = input("Enter Yes/No").lower()
                if a1 == "no":
                    Exit = True
                else:
                    continue


            elif pp1 == 2:
                # Adding librarians
                lib_name = input("Enter name:")
                lib_add = input("Address:")
                lib_contact = input("Phone number:")
                insert_lib(lib_name, lib_add, lib_contact)
                print("Do you wish to add another?")
                a1 = input("Enter Yes/No").lower()
                if a1 == "no":
                    Exit = True
                else:
                    continue

            elif pp1 == 3:
                # Adding books
                book_name = input("Enter the name:")
                author_name = input("Author name:")
                pub_name = input("Publisher:")
                rented_date = input("Rent Date(date/month/year):")
                rented_user = input('User name:')
                insert_book(book_name, author_name, pub_name, rented_date, rented_user)
                print("Do you wish to add another?")
                a1 = input("Enter Yes/No").lower()
                if a1 == "no":
                    Exit = True
                else:
                    continue

            else:
                print("Enter a valid value")

    elif p1 == 2:
        print('''
        Enter 1 for updating books
        Enter 2 for updating users''')
        pp2 = int(input(">"))
        Exit = False
        while Exit == False:
            if pp2 == 1:
                #updating books
                ch_bookname = input("Enter the name of book to be updated:")
                n_name = input("Enter the new name:")
                n_author = input("Enter the new author:")
                n_pub = input("Enter the new publishing company:")
                update_book(n_name,n_author, n_pub,ch_bookname)
                print("Do you wish to update another?")
                a1 = input("Enter Yes/No").lower()
                if a1 == "no":
                    Exit = True
                else:
                    continue

            elif pp2 == 2:
                #updating user details
                ch_name = input("Enter the name to be updated:")
                n_addr = input("Enter the new address:")
                n_cont = int(input("Enter the new contact number:"))
                update_user(n_addr, n_cont, ch_name)
                print("Do you wish to update another?")
                a1 = input("Enter Yes/No").lower()
                if a1 == "no":
                    Exit = True
                else:
                    continue

            else:
                print("Please enter valid values")

    elif p1 == 3:
        print("Enter 1 for deleting users and 2 for deleting books")
        pp3 = int(input(">"))
        if pp3 == 1:
            #for deleting users
            uname_del = input("Enter the name of the user to be deleted:")
            del_user(uname_del)
        elif pp3 == 2:
            name_del = input("Enter the name of the book to be deleted:")
            del_book(name_del)
        else:
            print("Please enter valid values")

    elif p1 == 4:
        print("The following are a list of books available:")
        c.execute('''SELECT Name FROM Books''')
        r = c.fetchall()
        k = 1
        for i in r:
            print(k,".", i[0])
            k+=1

        e1 = input("Enter the name of the book for viewing the details:")
        c.execute("SELECT Name, Author, Publishing_Company, Rented_date, Rented_User FROM Books WHERE Name = (?)", (e1,))
        r2 = c.fetchall()
        for j in r2:
            print("Name=" ,j[0])
            print("Author=", j[1])
            print("Publishing company=", j[2])
            print("Rented date=", j[3])
            print("Rented by=", j[4])

    else:
        print("Please enter valid values")
else:
    print("Please enter valid values")
c.close()
conn.close()

input('Press ENTER to exit')



