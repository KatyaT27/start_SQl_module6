SELECT t.name AS teacher_name, AVG(g.grade) AS average_grade
FROM teachers AS t
JOIN subjects AS sub ON t.id = sub.teacher_id
JOIN grades AS g ON sub.id = g.subject_id
GROUP BY t.name;