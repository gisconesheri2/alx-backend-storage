-- create a new view
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name FROM students WHERE score < 80
&& ISNULL(last_meeting) = 1 ||
DATEDIFF(CURDATE(), last_meeting) > 30;