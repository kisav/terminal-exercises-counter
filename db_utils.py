import sqlite3


def init_db()
    conn = sqlite3.connect("exercises.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercies {                             
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        exercise TEXT NOT NULL,
        count INTEGER NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP         
    }
    """)

    conn.commit()
    conn.close()

def add_exercise(exercise, count):
    conn = sqlite3.connect("exercises.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO exercies (exercise, count)
    VALUES (?, ?),
""", (exercise, count))

    conn.commit()
    conn.close()
