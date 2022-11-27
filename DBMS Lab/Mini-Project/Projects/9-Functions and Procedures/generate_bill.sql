CREATE PROCEDURE `GENERATE_BILL`(IN `order_id` BIGINT, IN `aadhaar` BIGINT, IN `insurance_id` BIGINT) NOT DETERMINISTIC CONTAINS SQL SQL SECURITY DEFINER BEGIN
DECLARE total_amount BIGINT;
DECLARE copayment_percentage BIGINT;
DECLARE copayment_amount BIGINT; -- this is the amount insurance company pays
DECLARE customer_payment BIGINT; -- this is the amount customer pays
-- do a total of all orders
SELECT SUM('price')
INTO total_amount
FROM ORDERED_DRUGS
WHERE 'order_id' = order_id;
-- get insurance details
SELECT co_insurance
INTO copayment_percentage
FROM INSURANCE
WHERE 'insurance_id' = insurance_id;
-- the insurance company will pay this amount
SET copayment_amount = total_amount * copayment_percentage;
-- the customer will pay this amount
SET customer_payment = total_amount * (1 - copayment_percentage);
-- Insert data
INSERT INTO BILL VALUES (order_id, aadhaar, total_amount, customer_payment, copayment_amount);
END;