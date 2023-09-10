SELECT g.name AS group_name, GROUP_CONCAT(s.name, ', ') AS students_in_group
FROM groups AS g
JOIN students AS s ON g.id = s.group_id
GROUP BY g.name;