import sqlite3

con = sqlite3.connect('sample.db')


table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, surname TEXT)'
cursor = con.cursor()
cursor.execute(table)
con.commit()
