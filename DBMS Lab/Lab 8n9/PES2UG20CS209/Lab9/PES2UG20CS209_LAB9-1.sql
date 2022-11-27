DELIMITER $$
CREATE TRIGGER compcheck  
BEFORE INSERT 
ON compartment FOR EACH ROW  
BEGIN  
    DECLARE error_msg VARCHAR(255);  
    declare count int;
    SET error_msg = ('Cannot have more than four compartment');  
    IF (select count(*) from compartment where train_no = new.train_no)>4 THEN  
    SIGNAL SQLSTATE '45000'   
    SET MESSAGE_TEXT = error_msg;  
    END IF;  
END $$   
DELIMITER ;

insert into railway2.compartment values ( 'A01', 'I class',23,8,6260);
SELECT * FROM railway2.compartment;
insert into railway2.compartment values ('A02','II class',15,7,58450);

