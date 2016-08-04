# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# Setup
# Potentially try or give option to use sqlite or MYSQL in future iterations
import sqlite3
import runpy
#define main setup
def Main():
        try:
# Initialisation/connection
                conn = sqlite3.connect('setup.db')
# prepare a cursor object using cursor() method
                c = conn.cursor()

#table setup for login and items
                #create login table priv stands for privleges unattempt stands for 
                c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, Email TEXT,password TEXT,priv BOOL,unattempt INT)')
                #create item table of ID, ItemName, Category, Quanitty, notes, value, total)
                c.execute('CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY AUTOINCREMENT, serial KEY,barcode INT, ItemName TEXT, Category TEXT, Quantity INT, Notes TEXT, Borrower TEXT, Booker TEXT)')
                #create user log time table
                c.execute('CREATE TABLE IF NOT EXISTS userlog(id INTEGER PRIMARY KEY AUTOINCREMENT, Attempt KEY, Email TEXT,datestamp TEXT,sucessful BOOL)')
                #create item log time table
                c.execute('CREATE TABLE IF NOT EXISTS itemlog(id INTEGER PRIMARY KEY AUTOINCREMENT, Email TEXT,datestamp TEXT,ItemName TEXT,serial TEXT,borrowing BOOL)')
                print('tablecreationdone')
# inserting test data, add # to start when done testing
                #c.execute("INSERT INTO users(Email,password,priv,unattempt) VALUES('admin@albertparkcollege.vic.edu.au', 'APc00000',1,0)")
                print('tablecreationdone')
                #c.execute("INSERT INTO users(Email,password,priv,unattempt)  VALUES('user@albertparkcollege.vic.edu.au','APc00000',0,0)")
                #c.execute("INSERT INTO items(serial,barcode,ItemName,Category,Quantity,Notes,Borrower,Booker) VALUES(123,456, 'GoSlow','Camera',1,null,'admin@albertparkcollege.vic.edu.au',null)")
                #c.execute("INSERT INTO items(serial,barcode,ItemName,Category,Quantity,Notes,Borrower,Booker) VALUES(111,222, 'Canon 700E','Camera',1,null,null,'user@albertparkcollege.vic.edu.au')")
                print('tablecreationdone')
# grabbing and checking data
                c.execute("SELECT * FROM users")
               
                data = c.fetchall()

                for row in data:
                        print (row)
# If error occurs, print notice
        except sqlite3.Error:
                if conn:
                        conn.rollback()
                        print ("There was a problem with the SQL")
# disconnect from server
        finally:
                if conn:
                        conn.commit()
                        conn.close()
                        runpy.run_path('loading.py')
# execute 
if __name__ == '__main__':
	Main()
