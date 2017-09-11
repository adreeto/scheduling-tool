import sqlite3

import time
import datetime
import random

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
	c.execute("INSERT INTO stuffToPlot VALUES(1234321, '2016-01-03', 'python', 8)")
	conn.commit()
	c.close()
	conn.close()

def dyn_data_entry():
	unix = time.time()

#create_table()
data_entry()