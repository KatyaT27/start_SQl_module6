SELECT grp.name AS group_name, s.name AS student_name, g.grade, g.date
FROM students AS s
JOIN groups AS grp ON s.group_id = grp.id
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
WHERE sub.name = ?
ORDER BY g.date;