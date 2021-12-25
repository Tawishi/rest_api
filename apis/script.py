# GET API request data and store in db
import requests
import sqlite3 as sql
import json

conn = sql.connect("C:/Users/Dell/Desktop/2019-2023/Github/rest_api/db.sqlite3")
curs = conn.cursor()
# curs. execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(curs. fetchall())
# curs.execute("DROP TABLE IF EXISTS restaurant_data")
# curs.execute("CREATE TABLE restaurant_data (id PRIMARY KEY, name text NOT NULL, type text, description text, hours text)")

n = 100
url = "https://random-data-api.com/api/restaurant/random_restaurant"

while n:
    data = requests.get(url)
    obj = data.json()

    rid = obj['id']
    name = obj['name']
    rtype = obj['type']
    description = obj['description']
    hours = json.dumps(obj['hours'])
    q = "INSERT INTO restaurants VALUES (?,?,?,?,?)"
    values = (rid, name, rtype, description, hours)
    curs.execute(q, values)
    conn.commit()

    n -= 1

data.close()
conn.close()