-- procedure to compute and store the average weighted score
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE num_rows INT;
    DECLARE idx INT;
    DECLARE w_avg INT;
    CREATE TEMPORARY TABLE weighted_avgs
    SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight) as was,
    corrections.user_id
    FROM projects
    INNER JOIN corrections
    ON corrections.project_id=projects.id
    GROUP BY corrections.user_id;
    SELECT COUNT(*) FROM users INTO num_rows;
    SET idx = 1;
    WHILE idx <= num_rows DO
        SELECT was FROM weighted_avgs WHERE user_id = idx INTO w_avg;
        UPDATE users SET average_score = w_avg
        WHERE id = idx;
        SET idx = idx + 1;
    END WHILE;
    DROP TEMPORARY TABLE weighted_avgs;
END
$$
DELIMITER ;