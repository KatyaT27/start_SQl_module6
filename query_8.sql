--Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT AVG(grade) AS average_grade
FROM student_grades
WHERE student_grades.subject_id IN (SELECT subject_id FROM subjects WHERE teacher_id = X);
