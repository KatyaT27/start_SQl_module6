import os
import sqlite3
from generate_data import create_db, populate_db, check_db

# Function to execute SQL queries from a file
def execute_sql_from_file(file_path, conn, params=None):
    with open(file_path, 'r') as query_file:
        query = query_file.read()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()

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
    else:
        return None  # Return None for other tasks

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
            "10. Список курсів, якому студенту читає який викладач"
        ]

        while True:
            print("Оберіть номер завдання ('q' для виходу):")
            print("\n".join(task_names))
            choice = input("Номер завдання: ")

            if choice.lower() == 'q':
                break

            try:
                task_number = int(choice)
                if 1 <= task_number <= 10:
                    query_file_path = os.path.join(sql_queries_directory, f'query_{task_number}.sql')
                    print("=" * 40)
                    print(f"Завдання {task_number}: {task_names[task_number - 1]}")

                    with open(query_file_path, 'r') as query_file:
                        print("Запит:")
                        print(query_file.read())

                    with sqlite3.connect('university.db') as con:
                        if subject_or_group := choose_subject_or_group(con, task_number):
                            params = (subject_or_group,)
                            results = execute_sql_from_file(query_file_path, con, params)
                            print("Результат:")
                            for result in results:
                                print(result)
                elif task_number == 1:
                    # Add code to execute and print task 1 results here
                    with sqlite3.connect('university.db') as con:
                        query_file_path = os.path.join(sql_queries_directory, 'query_1.sql')
                        results = execute_sql_from_file(query_file_path, con)
                        print("Результат:")
                        for result in results:
                            print(result)
                elif task_number == 4:
                    # Add code to execute and print task 4 results here
                    with sqlite3.connect('university.db') as con:
                        query_file_path = os.path.join(sql_queries_directory, 'query_4.sql')
                        results = execute_sql_from_file(query_file_path, con)
                        print("Результат:")
                        for result in results:
                            print(result)
                elif task_number == 5:
                    # Add code to execute and print task 5 results here
                    with sqlite3.connect('university.db') as con:
                        query_file_path = os.path.join(sql_queries_directory, 'query_5.sql')
                        results = execute_sql_from_file(query_file_path, con)
                        print("Результат:")
                        for result in results:
                            print(result)
                elif task_number == 6:
                    # Add code to execute and print task 6 results here
                    with sqlite3.connect('university.db') as con:
                        query_file_path = os.path.join(sql_queries_directory, 'query_6.sql')
                        results = execute_sql_from_file(query_file_path, con)
                        print("Результат:")
                        for result in results:
                            print(result)
                elif task_number == 8:
                    # Add code to execute and print task 8 results here
                    with sqlite3.connect('university.db') as con:
                        query_file_path = os.path.join(sql_queries_directory, 'query_8.sql')
                        results = execute_sql_from_file(query_file_path, con)
                        print("Результат:")
                        for result in results:
                            print(result)
                elif task_number == 9:
                    # Add code to execute and print task 9 results here
                    with sqlite3.connect('university.db') as con:
                        query_file_path = os.path.join(sql_queries_directory, 'query_9.sql')
                        results = execute_sql_from_file(query_file_path, con)
                        print("Результат:")
                        for result in results:
                            print(result)
                elif task_number == 10:
                    # Add code to execute and print task 10 results here
                    with sqlite3.connect('university.db') as con:
                        query_file_path = os.path.join(sql_queries_directory, 'query_10.sql')
                        results = execute_sql_from_file(query_file_path, con)
                        print("Результат:")
                        for result in results:
                            print(result)
                else:
                    print("Невірний номер завдання. Будь ласка, введіть номер від 1 до 10.")
            except ValueError:
                print("Невірний ввід. Будь ласка, введіть правильний номер / 'q', щоб вийти.")

    except sqlite3.Error as e:
        print("Помилка SQLite:", e)
    except Exception as ex:
        print("Сталася помилка:", ex)
