-- Insertion

-- Normal Insert into all Columns

INSERT INTO Customer(Aadhaar,first_name,last_name,phone,gender,address,date_of_birth,insurance_id)
VALUES
(784526471835,'Shyam','Bhat',7648964389,'M',"Hosa Road,Electronic City",'2002-09-03',55446677),
(6489075453,'Ravi','Singh',8976785649,'M',"Nice Road,Electronic City",'2002-02-13',66554433),
(546790987890,'Reha','Lal',9966442211,'F',"Sarjapur Road,Whitefield",'2002-10-17',99006655)

INSERT INTO Insurance(insurance_id,company_name,start_date,end_date,co_insurance)
VALUES
(55446677,"Adani Insurance",'2002-09-03','2102-09-03',9804),
(66554433,"Reliance Insurance",'2002-02-13','2102-02-13',7593),(99006655,"Big Insurance",'2002-10-17','2102-10-17',8694)



-- Insert into specific columns

INSERT INTO Employee(ID,Aadhaar,License,first_name,last_name,start_date,role,salary,phone_number,date_of_birth)
VALUES
(732,658361987523,9875,'Rahul','Gupta','2021-09-24','intern',60000,8899786432,'1992-06-19'),
(758,658361985378,8295,'Veer','Das','2015-09-24','pharmacist',70000,8899786432,'1992-06-19')

-- UI based insert - depecited in image



-- Medicine table

INSERT INTO Medicine(drug_name,batch_number,MedicineType,Manufacturer,stock_quantity,expiry_date,Price)
VALUES
('Dolo-650',788907,'Paracetamol','Micro Labs',800,'2023-02-12',31),
('Crocin',893145,'Targetted Pain','GSK',800,'2022-01-02',20)