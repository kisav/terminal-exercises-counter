import sqlite3


def init_db():
    conn = sqlite3.connect("exercises.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercies (                             
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        exercise TEXT NOT NULL,
        count INTEGER NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP         
    )
    """)

    conn.commit()
    conn.close()

def add_exercise(exercise, count):
    conn = sqlite3.connect("exercises.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO exercies (exercise, count)
    VALUES (?, ?)
""", (exercise, count))

    conn.commit()
    conn.close()

def show_stats():
    conn = sqlite3.connect("exercises.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT SUM(count)
    FROM exercies
    WHERE exercise = "приседаний"
    """)

    squats = cursor.fetchone()[0] or 0

    cursor.execute("""
    SELECT SUM(count)
    FROM exercies
    WHERE exercise = "отжиманий"
    """)

    pushups = cursor.fetchone()[0] or 0

    cursor.execute("""
    SELECT SUM(count)
    FROM exercies
    WHERE exercise = "пресса"
    """)

    pullups = cursor.fetchone()[0] or 0

    return f"Отжимания: {pushups} \n Приседания: {squats} \n Пресс: {pullups} \n"