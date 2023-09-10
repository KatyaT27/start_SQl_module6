SELECT grp.name AS group_name, AVG(g.grade) AS average_grade
FROM groups AS grp
JOIN students AS s ON grp.id = s.group_id
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
WHERE sub.name = ?
GROUP BY grp.name
ORDER BY average_grade DESC;