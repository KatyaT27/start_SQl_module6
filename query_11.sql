--Середній бал, який певний викладач ставить певному студентові.

SELECT AVG(grade) AS average_grade
FROM student_grades
WHERE student_id = X  -- Replace X with the student_id
  AND subject_id IN (SELECT subject_id FROM subjects WHERE teacher_id = Y);  -- Replace Y with the teacher_id
