import sqlite3
from faker import Faker
import random
import datetime

fake = Faker()


def create_db():
    with open('init_db.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.executescript(sql)


def populate_db():
    # Create students
    student_data = [(fake.name(),) for _ in range(30)]
    group_data = [(fake.unique.random_number(digits=4),)
                  for _ in range(3)]  # Generate unique group IDs
    teacher_data = [(fake.name(),) for _ in range(3)]

    # Create subjects with random teacher assignments
    subject_data = [(fake.word(), random.randint(1, 3)) for _ in range(5)]

    with sqlite3.connect('university.db') as con:
        cur = con.cursor()

        # Create students
        cur.executemany(
            "INSERT INTO students (student_name) VALUES (?);", student_data)

        # Create groups
        cur.executemany(
            "INSERT INTO groups (group_name) VALUES (?);", group_data)

        # Create teachers
        cur.executemany(
            "INSERT INTO teachers (teacher_name) VALUES (?);", teacher_data)

        # Create subjects with random teacher assignments
        cur.executemany(
            "INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?);", subject_data)

        # Create student grades for each student and subject
        for student_id in range(1, 31):
            for subject_id in range(1, 6):
                grades = [(student_id, subject_id, random.randint(1, 5), fake.date_between(
                    start_date='-1y', end_date='today')) for _ in range(20)]
                cur.executemany(
                    "INSERT INTO student_grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?);", grades)


def check_db():
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        _extracted_from_check_db_4(cur, "SELECT * FROM students;", "Students:")
        _extracted_from_check_db_4(cur, "SELECT * FROM groups;", "\nGroups:")
        _extracted_from_check_db_4(
            cur, "SELECT * FROM teachers;", "\nTeachers:")
        _extracted_from_check_db_4(
            cur, "SELECT * FROM subjects;", "\nSubjects:")
        _extracted_from_check_db_4(
            cur, "SELECT * FROM student_grades;", "\nGrades:")


def _extracted_from_check_db_4(cur, arg1, arg2):
    cur.execute(arg1)
    students = cur.fetchall()
    print(arg2)
    for student in students:
        print(student)


if __name__ == "__main__":
    create_db()
    populate_db()
    check_db()
