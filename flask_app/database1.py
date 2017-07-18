import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute('CREATE TABLE table1 (name TEXT, phone TEXT)')
print "Table created successfully";
conn.close()
