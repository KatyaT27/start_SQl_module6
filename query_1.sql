--Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

SELECT s.student_name, AVG(sg.grade) as average_grade
FROM students s
INNER JOIN student_grades sg ON s.student_id = sg.student_id
GROUP BY s.student_name
ORDER BY average_grade DESC
LIMIT 5;
