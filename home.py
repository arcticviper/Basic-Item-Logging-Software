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
                c.execute('CREATE TABLE IF NOT EXISTS users(ID KEY, Email TEXT,password TEXT)') #create login table email+password
                c.execute('CREATE TABLE IF NOT EXISTS users(ID KEY, ItemName TEXT, Category TEXT, Quantity INT, Notes TEXT, Value INT, Total REAL)') #create item table of ID, ItemName, Category, Quanitty, notes, value, total)

# inserting test data, add # when done testing
                c.execute("INSERT INTO users VALUES(2, 'name@albertparkcollege.vic.edu.au', 'APC00000')")

# grabbing and checking data
                c.execute("SELECT * FROM Users")
               
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
