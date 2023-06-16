import sqlite3


def setup_db():
    conn = sqlite3.connect('database.db')
    print("Connected to database successfully")

    with open('schema.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    conn.cursor()
    conn.executescript(sql_script)
    print("Initialized database successfully!")


def get_total():
    conn = sqlite3.connect('database.db')
    conn.cursor()

    total = conn.execute("SELECT COUNT(*) FROM counter;")

    conn.commit()
    conn.close()

    return total


def get_count_per_function():
    conn = sqlite3.connect('database.db')
    conn.cursor()

    counts = conn.execute("SELECT COUNT(*) FROM counter GROUP BY name;")

    conn.commit()
    conn.close()

    return counts


def insert_counter(name):
    conn = sqlite3.connect('database.db')
    conn.cursor()

    conn.execute("INSERT INTO counter (name) VALUES (?);", (name,))

    conn.commit()
    conn.close()
