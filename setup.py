# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# Setup
# Potentially try or give option to use sqlite or MYSQL in future iterations
import sqlite3
#define main setup
def Main():
        try:
# Initialisation/connection
                conn = sqlite3.connect('setup.db')
# prepare a cursor object using cursor() method
                c = conn.cursor()

#table setup for login and items
                #create login table email+password, priv stands for privleges
                c.execute('CREATE TABLE IF NOT EXISTS users(ID KEY, Email TEXT,password TEXT,priv BOOL,unattempt INT)')
                #create item table of ID, ItemName, Category, Quanitty, notes, value, total)
                c.execute('CREATE TABLE IF NOT EXISTS items(serial KEY, ItemName TEXT, Category TEXT, Quantity INT, Notes TEXT, Borrower TEXT,Booker TEXT)')
                #create user log time table
                c.execute('CREATE TABLE IF NOT EXISTS userlog(Attempt KEY, Email TEXT,datestamp TEXT,sucessful BOOL)')
                #create item log time table
                c.execute('CREATE TABLE IF NOT EXISTS itemlog(ID KEY, Email TEXT,datestamp TEXT,ItemName TEXT,serial KEY)')
# inserting test data, add # to start when done testing
                c.execute("INSERT INTO users VALUES(123, 'admin@albertparkcollege.vic.edu.au', 'APc00000',1,0)")
                c.execute("INSERT INTO users VALUES(456, 'user@albertparkcollege.vic.edu.au','APc00000',0,0)")
                
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
# execute 
if __name__ == '__main__':
	Main()
