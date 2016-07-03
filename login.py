# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# LOGIN
import sqlite3
import getpass
database = sqlite3.connect("setup.db")
c = database.cursor()
#user input
user = input ("Username/Full Email: ")
passwordio = getpass.getpass(prompt='Password: ', stream=None)
#read from users table and ensures that user and password matches with information on database
#when using different tables ensure that Email  and password matches the table selected (users)
c.execute('SELECT * from users WHERE Email="%s" AND password="%s"' % (user, passwordio))
if c.fetchone() is not None:
    print ("Welcome")
    
else:
    print ("Login failed, please ensure you have opened the program correctly")
