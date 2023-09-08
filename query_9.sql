--Знайти список курсів, які відвідує студент.

SELECT subjects.subject_name
FROM subjects
JOIN student_grades ON subjects.subject_id = student_grades.subject_id
WHERE student_grades.student_id = X;
