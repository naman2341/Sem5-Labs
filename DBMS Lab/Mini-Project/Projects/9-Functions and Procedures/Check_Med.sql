CREATE FUNCTION Check_Med(batch_number BIGINT)
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
declare Return_val varchar(50)
IF batch_number > 100000 THEN
SET Return_val = 'Authentic';
ELSE
SET Return_val='Possible Fake';
END IF;
RETURN Return_val; 
END;