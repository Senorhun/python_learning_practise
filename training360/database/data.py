import sqlite3 as lite

con = lite.connect("test.db")

with con:
    cur = con.cursor()

    cur.execute("SELECT SQLITE_VERSION()")

    data = cur.fetchall()[0]

    print(f"SQLite version: {data}")

    cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
    cur.execute("INSERT INTO cars VALUES(1, 'Audi', 52642)")
    cur.execute("INSERT INTO cars VALUES(2, 'Mercedes', 57127)")
    cur.execute("INSERT INTO cars VALUES(3, 'Skoda', 9000)")

    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()

    for row in rows:
        print(row)
