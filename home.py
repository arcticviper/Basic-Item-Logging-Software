# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# Setup
import sqlite3
def Setup():
        cur.excute("INSERT INTO users VALUES()")
        con.commit()

# Open database connection
db = conn.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()

try:
        con = sqlite3.connect('setup.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE users(Email TEXT,password TEXT)') #create login table email+password
        cur.execute('CREATE TABLE items(ID KEY, ItemName TEXT, Category TEXT, Quantity INT, Notes TEXT, Value INT, Total REAL)') #create item table of ID, ItemName, Category, Quanitty, notes, value, total)
        cur.execute("INSERT INTO users VALUES('FirstnameLastname', 'APC00000')")#intesting test data

        con.commit() #save changes
                
        cur.execute("SELECT * FROM Users") #
                
        data = cur.fetchall()

        for row in data:
                print (row)

except sqlite3.Error:
        if con:
                con.rollback()
                print ("There was a problem with the SQL")
finally:
        if con:
                con.close()
if __name__ == '__main__':
	Main()
