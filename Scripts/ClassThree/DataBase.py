import sqlite3 as sql

conn = sql.connect('aulaDB.db')
print(type(conn))