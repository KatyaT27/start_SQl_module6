SELECT t.name AS teacher_name, GROUP_CONCAT(c.name, ', ') AS courses_taught
FROM teachers AS t
JOIN courses AS c ON t.id = c.teacher_id
GROUP BY t.name;