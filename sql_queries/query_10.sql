SELECT t.name AS teacher_name, s.name AS student_name, GROUP_CONCAT(sub.name, ', ') AS courses_taught
FROM teachers AS t
JOIN subjects AS sub ON t.id = sub.teacher_id
JOIN grades AS g ON sub.id = g.subject_id
JOIN students AS s ON g.student_id = s.id
GROUP BY t.name, s.name;