import itertools
from faker import Faker
import sqlite3
import random

fake = Faker()


def create_db():
    conn = sqlite3.connect('university.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS students
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    group_id INTEGER NOT NULL,
                    birthdate DATE NOT NULL);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS groups
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    course INTEGER NOT NULL);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS teachers
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS subjects
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    teacher_id INTEGER NOT NULL,
                    FOREIGN KEY (teacher_id) REFERENCES teachers(id));''')

    cur.execute('''CREATE TABLE IF NOT EXISTS grades
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER NOT NULL,
                    subject_id INTEGER NOT NULL,
                    grade REAL NOT NULL,
                    date DATE NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES students(id),
                    FOREIGN KEY (subject_id) REFERENCES subjects(id));''')

    cur.execute('''CREATE TABLE IF NOT EXISTS courses
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    teacher_id INTEGER NOT NULL,
                    FOREIGN KEY (teacher_id) REFERENCES teachers(id));''')

    conn.commit()
    conn.close()


def populate_db():
    conn = sqlite3.connect('university.db')
    cur = conn.cursor()

    for _ in range(30):
        cur.execute("INSERT INTO students (name, group_id, birthdate) VALUES (?, ?, ?)",
                    (fake.unique.first_name(), random.randint(1, 3), fake.date_of_birth(minimum_age=18, maximum_age=30)))

    for _ in range(3):
        cur.execute("INSERT INTO groups (name, course) VALUES (?, ?)",
                    (fake.unique.word(ext_word_list=None), random.randint(1, 4)))

    for _ in range(5):
        cur.execute("INSERT INTO teachers (name) VALUES (?)",
                    (fake.unique.first_name(),))

    for _ in range(8):
        cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)",
                    (fake.unique.word(ext_word_list=None), random.randint(1, 5)))

    for _ in range(10):  # You can adjust the number of courses to populate
        cur.execute("INSERT INTO courses (name, teacher_id) VALUES (?, ?)",
                    (fake.unique.word(ext_word_list=None), random.randint(1, 5)))

    for student_id, subject_id in itertools.product(range(1, 31), range(1, 9)):
        cur.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                    (student_id, subject_id, round(random.uniform(2, 5), 2), fake.date_between(start_date='-1y', end_date='today')))

    conn.commit()
    conn.close()


def check_db():
    conn = sqlite3.connect('university.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    print(cur.fetchall())

    cur.execute("SELECT * FROM groups")
    print(cur.fetchall())

    cur.execute("SELECT * FROM teachers")
    print(cur.fetchall())

    cur.execute("SELECT * FROM subjects")
    print(cur.fetchall())

    cur.execute("SELECT * FROM grades LIMIT 2")
    print(cur.fetchall())

    cur.execute("SELECT * FROM courses LIMIT 2")
    print(cur.fetchall())

    conn.close()

if __name__ == "__main__":
    create_db()
    populate_db()
    check_db()
