-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE sum_score INT DEFAULT = 0;
    DECLARE total_count INT DEFAULT = 0;
    SELECT SUM(score) INTO sum_score FROM corrections WHERE corrections.user_id = user_id;
    SELECT COUNT(*) INTO total_count FROM corrections WHERE corrections.user_id = user_id;
    UPDATE users
        SET users.average_score = (sum_score /

total_count) WHERE users.id = user_id;

END $$

DELIMITER;