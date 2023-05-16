import sqlite3


def connect_db():
    conn = sqlite3.connect("database.db", detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.executescript(open("schema.sql", "r").read())
    return conn, cur


conn, cur = connect_db()

cur.execute(
    "INSERT INTO user (username, password) VALUES (?, ?) ",
    ("AngelUnder23", "somehash292382"),
)

cur.execute(
    "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)",
    ("HeadHunter", "HeadH description", 1),
)

cur.execute(
    "SELECT u.username, p.body FROM user u LEFT JOIN post p ON p.author_id = u.id WHERE u.id=1"
)
row = cur.fetchone()

# вывод всех строк
print(dict(row))

# закрытие соединения с базой данных
conn.commit()
conn.close()
