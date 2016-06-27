# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# Setup
import sqlite3
def Setup():
        cur.excute("INSERT INTO users VALUES()
        con.commit()

def Main():

        try:
                con = sqlite3.connect('test.db')
                cur = con.cursor()
                cur.execute('CREATE TABLE users(User TEXT, Pass INT)')
#                cur.execute("INSERT INTO Pets VALUES(1, 'Cat', 400)")
#                cur.execute("INSERT INTO Pets VALUES(2, 'Cog', 600)")

                con.commit()
                
                cur.execute("SELECT * FROM Users")
                
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
db_ip = ""
if len(db_ip) < 8 or len(db_ip) > 15:
	print ("The IP adress is invalid")
