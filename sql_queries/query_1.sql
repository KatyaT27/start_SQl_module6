SELECT s.name AS student_name, AVG(g.grade) AS average_grade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
GROUP BY s.name
ORDER BY average_grade DESC
LIMIT 5;
