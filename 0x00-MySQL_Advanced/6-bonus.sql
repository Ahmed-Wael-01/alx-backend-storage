-- adds bonus for a student
DELIMITER &&
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
    IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0
    THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    INSERT INTO corrections (user_int, project_id, score) VALUES (user_id, (SELECT id FROM projects WHERE name = project_name LIMIT 1), score);
END &&
DELIMITER;
