-- Create the students table
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(255) NOT NULL,
    group_id INTEGER, -- Add the group_id column as a foreign key
    FOREIGN KEY (group_id) REFERENCES groups (group_id)
);

-- Create the groups table
CREATE TABLE IF NOT EXISTS groups (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(255) NOT NULL
);

-- Create the teachers table
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_name VARCHAR(255) NOT NULL
);

-- Create the subjects table with foreign key constraint
CREATE TABLE IF NOT EXISTS subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(255) NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
);

-- Create the student_grades table with foreign key constraints
CREATE TABLE IF NOT EXISTS student_grades (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER NOT NULL,
    date_received DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
);
