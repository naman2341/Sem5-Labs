CREATE TABLE PAYMENT_BACKUP ( Transaction_ID bigint(30) PRIMARY KEY,
							Bank varchar(255),
                            Card_No bigint,
                            Price int,
                            PNR varchar(255) NOT NULL);
                            
DELIMITER $$
CREATE TRIGGER deletebackup 
BEFORE DELETE 
ON ticket FOR EACH ROW  
BEGIN 
	Insert into Payment_backup  select * from payment_info where pnr = old.pnr; 
	delete from payment_info where pnr = old.pnr;
    delete from ticket_passenger where pnr = old.pnr;
END $$   
DELIMITER ;

delete from ticket where pnr = 'PNR001';
SELECT * FROM railway2.payment_backup;