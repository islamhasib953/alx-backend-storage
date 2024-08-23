-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.


DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_res INT DEFAULT 0;
    DECLARE sum_weight INT DEFAULT 0;
    SELECT SUM(weight * score), SUM(weight)
    INTO avg_res, sum_weight
    FROM projects p, corrections c
    WHERE c.user_id = user_id AND c.project_id = p.id;
    
    UPDATE users
    SET average_score = IF(sum_weight = 0, 0, avg_res/sum_weight)
    WHERE users.id = user_id;
END $$

DELIMITER ;