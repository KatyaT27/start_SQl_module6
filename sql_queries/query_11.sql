SELECT AVG(g.grade) AS average_grade
FROM grades AS g
JOIN students AS s ON g.student_id = s.id
JOIN subjects AS sub ON g.subject_id = sub.id
JOIN teachers AS t ON sub.teacher_id = t.id
WHERE t.name = @TeacherName
  AND s.name = @StudentName;
