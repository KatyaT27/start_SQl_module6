SELECT s.name AS student_name, AVG(g.grade) AS average_grade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
WHERE sub.name = ?
GROUP BY s.name
ORDER BY average_grade DESC
LIMIT 1;