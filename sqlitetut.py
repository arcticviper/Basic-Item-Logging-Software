import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table(): #making table
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry(): #insert data
    c.execute("INSERT INTO stuffToPlot VALUES(145125552, '2016-01-02', 'Python', 8)")
    conn.commit() #committing data

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%M-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot(unix, datestamp, keyword, value) VALUES (?,?,?,?)",(unix, date, keyword, value))
    conn.commit()

create_table()
data_entry()
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)

c.close()
conn.close()
