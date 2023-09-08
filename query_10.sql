--Список курсів, які певному студенту читає певний викладач.

SELECT subjects.subject_name
FROM subjects
WHERE subjects.teacher_id = Y
  AND subjects.subject_id IN (SELECT subject_id FROM student_grades WHERE student_id = X);
