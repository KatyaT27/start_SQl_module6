--Знайти студента із найвищим середнім балом з певного предмета.

SELECT s.student_id, AVG(sg.grade) AS average_grade
FROM students s
INNER JOIN student_grades sg ON s.student_id = sg.student_id
WHERE sg.subject_id = ?
GROUP BY s.student_id
ORDER BY average_grade DESC
LIMIT 1;


