-- compute average score via a procedure
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE mean_score FLOAT;
    SET mean_score = (SELECT AVG(score) FROM corrections AS C
                      WHERE C.user_id = user_id);
    UPDATE users SET average_score = mean_score
    WHERE id = user_id;
END
$$
DELIMITER ;