# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# LOGIN
import sqlite3
import getpass
import time
import datetime
attempt = 1
conn = sqlite3.connect('setup.db')
c = conn.cursor()
unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%M-%d %H:%M:%S'))
#user input
user = input ("User: ")

passwordio = getpass.getpass(prompt='Password: ', stream=None)
#read from users table and ensures that user and password matches with information on database
#when using different tables ensure that Email  and password matches the table selected (users) and only selecting users who have under 3 incorrect attempts
c.execute('SELECT * from users WHERE Email="%s" AND password="%s" AND unattempt<3' % (user, passwordio))
if c.fetchone() is not None:
    print ("Welcome")
    c.execute("INSERT INTO userlog(Attempt, Email, datestamp,sucessful)VALUES(?,?,?,?)",(attempt,user,date,True))
    conn.commit()
else:
    attempt=attempt+1
    print ("Login failed, please ensure you have typed your details correctly.")
    c.execute("INSERT INTO userlog(Attempt, Email, datestamp,sucessful)VALUES(?,?,?,?)",(attempt,user,date,False))
    c.execute('UPDATE users SET unattempt = unattempt+1 WHERE Email= ?',(user,))
    conn.commit()
