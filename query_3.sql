--Знайти середній бал у групах з певного предмета.

SELECT g.group_name, AVG(sg.grade) AS average_grade
FROM groups g
INNER JOIN students s ON g.group_id = s.group_id
INNER JOIN student_grades sg ON s.student_id = sg.student_id
WHERE sg.subject_id = 'subject_id'
GROUP BY g.group_name;





