# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# LOGIN
import sqlite3
user = input ("User: ")
password = getpass.getpass("Password: ")

db = sqlite3.connect('setup.db')
c = db.cursor()
c.execute('SELECT * from sabb WHERE usuario="%s" AND senha="%s"' % (user, pswd))
if c.fetchone() is not None:
    print "Welcome"
else:
    print "Login failed"
