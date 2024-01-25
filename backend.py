import sqlite3

def connect():
    # Create a database file
    with sqlite3.connect("app.db") as conn:
        cur = conn.cursor()
        # Create a table to store data
        cur.execute("CREATE TABLE IF NOT EXISTS food(id INTEGER PRIMARY KEY, name TEXT NOT NULL, price INTEGER NOT NULL, image BLOB)")

def insert(name, price, image_path):
    with sqlite3.connect("app.db") as conn:
        cur = conn.cursor()
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        cur.execute("INSERT INTO food(name, price, image) VALUES(?, ?, ?)", (name, price, image_data))
        conn.commit()

def view():
    with sqlite3.connect("app.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT name, price FROM food")
        rows = cur.fetchall()
        return rows

image_path = "OIP.jpeg"
# insert(name="Chicken", price=129, image_path=image_path)

connect()
print(view())
