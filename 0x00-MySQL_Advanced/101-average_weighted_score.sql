-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- تحديث المتوسط المرجح للدرجات لكل مستخدم مباشرة
    UPDATE users u
    JOIN (
        SELECT c.user_id, SUM(p.weight * c.score) /

SUM(p.weight) AS avg_weighted_score
        FROM projects p
        JOIN corrections c ON c.project_id = p.id
        GROUP BY c.user_id
    ) avg_scores ON u.id = avg_scores.user_id
    SET u.average_score = avg_scores.avg_weighted_score;

END $$

DELIMITER ;