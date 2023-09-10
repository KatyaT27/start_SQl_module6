SELECT s.name AS student_name, GROUP_CONCAT(sub.name, ', ') AS courses_attended
FROM students AS s
LEFT JOIN grades AS g ON s.id = g.student_id
LEFT JOIN subjects AS sub ON g.subject_id = sub.id
GROUP BY s.name;