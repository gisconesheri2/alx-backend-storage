-- create a procedure to add a new correction for a student
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT)
BEGIN
    DECLARE proj_n VARCHAR(255);
    DECLARE proj_id INT;
    SET proj_n = (SELECT name FROM projects WHERE name = project_name);
    IF ISNULL(proj_n)
    THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    SET proj_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, proj_id, score);
END
$$
DELIMITER ;