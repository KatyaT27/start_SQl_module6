import sqlite3
from generate_data import create_db, populate_db, check_db

# Define a function to execute a single query and print the results


def execute_query(query_file_path, conn, args=None):
    with open(query_file_path, 'r') as query_file:
        query = query_file.read()
        cursor = conn.cursor()
        if args is not None:
            cursor.execute(query, args)
        else:
            cursor.execute(query)
        return cursor.fetchall()

# Define a function to execute multiple queries and print their results


def execute_queries(queries, conn):
    for query_file, args in queries:
        result = execute_query(query_file, conn, args)
        # Extract the query name from the filename
        query_name = query_file.split('.')[0]
        print(f"{query_name} Result:")
        print(result)


if __name__ == "__main__":
    # Define the subject_id, group_id, and student_id you want to use
    subject_id = 8
    group_id = 3
    student_id = 50
    teacher_id = 5

    # Create and populate the database
    create_db()
    populate_db()

    # Check the database content
    check_db()

    # Connect to the database
    conn = sqlite3.connect('university.db')

    # List of query files to execute with their arguments (if any)
    query_files = [
        ('query_1.sql', None),
        ('query_2.sql', (subject_id,)),
        ('query_3.sql', (group_id,)),
        ('query_4.sql', None),
        ('query_5.sql', None),
        ('query_6.sql', (student_id,)),
        ('query_7.sql', None),
        ('query_8.sql', (teacher_id,)),
        ('query_9.sql', (teacher_id,)),
        ('query_10.sql', None),
        ('query_11.sql', (student_id,)),
        ('query_12.sql', None),
    ]

    # Execute the queries
    execute_queries(query_files, conn)

    # Close the database connection
    conn.close()
