CREATE OR REPLACE
PROCEDURE ADD_DRUG_TO_ORDER
(
order_id IN INT,
drug_name IN CHAR(255),
quantity IN INT )
AS
drug MEDICINE%ROWTYPE;
insufficient_quantity EXCEPTION;
BEGIN
SELECT * INTO drug
FROM MEDICINE
WHERE 'drug_name' = drug_name;
IF drug.quantity < quantity THEN
RAISE insufficient_quantity;
ELSE
INSERT INTO ORDERED_DRUGS
VALUES (order_id, drug.drug_name, drug.batch_number, quantity, drug.price);
DBMS_OUTPUT.PUT_LINE("Drug added successfully to the order");
END IF;
EXCEPTION
WHEN insufficient_quantity THEN DBMS_OUTPUT.PUT_LINE(
"Request drug " || drug_name || " is not available. Maximum order possible is " || drug.quantity );
END;