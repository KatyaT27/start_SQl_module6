-- Оцінки студентів у певній групі з певного предмета на останньому занятті.
WITH LastClassGrades AS (
  SELECT
    s.student_name,
    sg.grade
  FROM
    student_grades sg
    JOIN students s ON sg.student_id = s.student_id
  WHERE
    sg.subject_id = X  -- Replace X with the subject_id
    AND sg.date_received = (
      SELECT MAX(date_received)
      FROM student_grades
      WHERE subject_id = X  -- Replace X with the subject_id
        AND student_id IN (SELECT student_id FROM students WHERE group_id = Y)  -- Replace Y with the group_id
    )
)
SELECT * FROM LastClassGrades;
