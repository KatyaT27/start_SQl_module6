--Знайти оцінки студентів в окремій групі з певного предмета.

SELECT students.student_name, student_grades.grade
FROM students
JOIN student_grades ON students.student_id = student_grades.student_id
WHERE students.group_id = X AND student_grades.subject_id = Y;
