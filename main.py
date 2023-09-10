import os
import sqlite3
from generate_data import create_db, populate_db, check_db

def execute_sql_from_file(file_path, conn, params=None):
    try:
        with open(file_path, 'r') as query_file:
            return _execute_sql_from_file(query_file, conn, params)
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

def _execute_sql_from_file(query_file, conn, params):
    query = query_file.read()
    print("Executing query:")
    print(query)
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    results = cursor.fetchall()
    print("Query executed successfully.")
    return results

# Function to choose subject or group based on the task number
def choose_subject_or_group(con, task_number):
    if task_number in [2, 3, 7]:
        # Fetch available subjects from the database
        cur = con.cursor()
        query = "SELECT DISTINCT sub.name FROM subjects AS sub"
        cur.execute(query)
        choices = cur.fetchall()

        print("Доступні предмети:")
        for i, choice in enumerate(choices, start=1):
            print(f"{i}. {choice[0]}")

        choice = input("Оберіть номер предмету (1-8): ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(choices):
                return choices[choice - 1][0]
            else:
                print("Невірний ввід.")
        except ValueError:
            print("Невірний ввід для вибору.")
    elif task_number == 12:
        # Fetch available groups from the database
        cur = con.cursor()
        query = "SELECT DISTINCT grp.name FROM groups AS grp"
        cur.execute(query)
        group_choices = cur.fetchall()

        print("Доступні групи:")
        for i, choice in enumerate(group_choices, start=1):
            print(f"{i}. {choice[0]}")

        choice = input("Оберіть номер групи (1-8): ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(group_choices):
                return group_choices[choice - 1][0]
            else:
                print("Невірний ввід.")
        except ValueError:
            print("Невірний ввід для вибору.")
    else:
        return None  # Return None for other tasks

# Function to choose a group for Task 12
def choose_group(con):
    cur = con.cursor()
    query = "SELECT DISTINCT grp.name FROM groups AS grp"
    cur.execute(query)
    group_choices = cur.fetchall()

    print("Доступні групи:")
    for i, choice in enumerate(group_choices, start=1):
        print(f"{i}. {choice[0]}")

    choice = input("Оберіть номер групи (1-8): ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(group_choices):
            return group_choices[choice - 1][0]
        else:
            print("Невірний ввід.")
    except ValueError:
        print("Невірний ввід для вибору.")
    return None

# Function to choose a subject for Task 12
def choose_subject(con):
    cur = con.cursor()
    query = "SELECT DISTINCT sub.name FROM subjects AS sub"
    cur.execute(query)
    subject_choices = cur.fetchall()

    print("Доступні предмети:")
    for i, choice in enumerate(subject_choices, start=1):
        print(f"{i}. {choice[0]}")

    choice = input("Оберіть номер предмету (1-8): ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(subject_choices):
            return subject_choices[choice - 1][0]
        else:
            print("Невірний ввід.")
    except ValueError:
        print("Невірний ввід для вибору.")
    return None

if __name__ == "__main__":
    try:
        # Database setup and other tasks go here
        # You can create and populate the database using functions from the generate_data module
        create_db()
        populate_db()
        check_db()

        # Get the directory of your main script (main.py)
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Specify the path to the 'sql_queries' directory
        sql_queries_directory = os.path.join(current_directory, 'sql_queries')

        task_names = [
            "1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів",
            "2. Знаходить студента із найвищим середнім балом з предмета",
            "3. Знаходить середній бал у групах з предмета",
            "4. Знайти середній бал на потоці (по всій таблиці оцінок)",
            "5. Знайти, які курси читає кожен викладач",
            "6. Знайти список студентів в кожній групі",
            "7. Знаходить оцінки студентів в кожній групі з предмета",
            "8. Знаходить середній бал, який ставить кожен викладач зі своїх предметів",
            "9. Знайти список курсів, які відвідує кожен студент",
            "10. Список курсів, якому студенту читає який викладач",
            "11. Середній бал, який певний викладач ставить певному студентові",  # Task 11
            "12. Оцінки студентів у певній групі з певного предмета на останньому занятті"  # Task 12
        ]

        while True:
            print("Оберіть номер завдання ('q' для виходу):")
            print("\n".join(task_names))
            choice = input("Номер завдання: ")

            if choice.lower() == 'q':
                break

            try:
                task_number = int(choice)
                if 1 <= task_number <= 12:
                    query_file_path = os.path.join(sql_queries_directory, f'query_{task_number}.sql')
                    print("=" * 40)
                    print(f"Завдання {task_number}: {task_names[task_number - 1]}")

                    with open(query_file_path, 'r') as query_file:
                        print("Запит:")
                        print(query_file.read())

                    with sqlite3.connect('university.db') as con:
                        if task_number == 11:
                            # Additional Task 1: Choose a teacher and a student
                            cur = con.cursor()
                            cur.execute("SELECT DISTINCT name FROM teachers")
                            teacher_choices = cur.fetchall()
                            print("Оберіть викладача:")
                            for i, teacher in enumerate(teacher_choices, start=1):
                                print(f"{i}. {teacher[0]}")
                            teacher_choice = int(input("Номер викладача: "))

                            cur.execute("SELECT DISTINCT name FROM students")
                            student_choices = cur.fetchall()
                            print("Оберіть студента:")
                            for i, student in enumerate(student_choices, start=1):
                                print(f"{i}. {student[0]}")
                            student_choice = int(input("Номер студента: "))

                            # Execute the query with teacher and student
                            params = (teacher_choices[teacher_choice - 1][0], student_choices[student_choice - 1][0])
                        elif task_number == 12:
                            # Task 12: Choose a group and a subject
                            group_name = choose_group(con)
                            subject_name = choose_subject(con)
                            params = (group_name, subject_name) if group_name and subject_name else None
                        else:
                            # For other tasks, choose subject or group
                            subject_or_group = choose_subject_or_group(con, task_number)
                            params = (subject_or_group,) if subject_or_group is not None else None

                        results = execute_sql_from_file(query_file_path, con, params)
                        print("Результат:")
                        for result in results:
                            print(result)
                else:
                    print("Невірний номер завдання. Будь ласка, введіть номер від 1 до 12.")
            except ValueError:
                print("Невірний ввід. Будь ласка, введіть правильний номер / 'q', щоб вийти.")

    except sqlite3.Error as e:
        print("Помилка SQLite:", e)
    except Exception as ex:
        print("Сталася помилка:", ex)