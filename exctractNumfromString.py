import sqlite3
import re

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("select quantity from orderan where noTransaksi=4")

quantity = str(cursor.fetchall())

listq = quantity.split()
num = 2

test = re.findall(r'\d+', quantity)

print(list(map(int, test)))

