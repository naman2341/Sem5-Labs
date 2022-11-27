#PES2UG20CS209 - NAMAN CHOUDHARY
#Q1


SELECT t1.user_id, t1.user_type, t1.fname, t1.lname FROM train_user t1, ticket WHERE t1.user_id = ticket.user_id AND ticket.departure =
'bengaluru' AND ticket.arrival = 'chennai' AND MONTH(ticket.travel_date) = 10 AND YEAR(ticket.travel_date) = 2021 AND UNION SELECT t2.user_id,
t2.user_type, t2. fname, t2.lname FROM train_user t2, ticket WHERE t2.user_id = ticket.user_id AND ticket.departure = 'bengaluru' AND
ticket.arrival='chennai' AND MONTH(ticket.travel_date) = 8 AND YEAR(ticket.travel_date) = 2022;



#PES2UG20CS209 - NAMAN CHOUDHARY
#Q2

SELECT t1.user_id, t1.user_type, t1.fname, t1.lname FROM train_user t1, ticket WHERE t1.user_id = ticket.user_id AND ticket.departure =
'bengaluru' AND ticket.arrival = 'chennai' AND MONTH(ticket.travel_date) = 10 AND YEAR(ticket.travel_date) = 2021 AND EXISTS(SELECT t2.user_id,
t2.user_type, t2.fname, t2.lname FROM train_user t2, ticket WHERE t2.user_id = ticket.user_id AND ticket.departure = 'bengaluru' AND
ticket.arrival='chennai' AND MONTH(ticket.travel_date) = 8 AND YEAR(ticket.travel_date) = 2022 AND t1.user_id = t2.user_id);


#PES2UG20CS209 - NAMAN CHOUDHARY
#Q3

SELECT t2.user_id, t2.user_type, t2.fname, t2.lname FROM train_user t2, ticket ti2 WHERE t2.user_id = ti2.user_id AND ti2.departure =
'bengaluru' AND ti2.arrival = 'chennai' AND MONTH(ti2.travel_date) = 8 AND YEAR(ti2.travel_date) = 2022 AND NOT EXISTS(SELECT t1.user_id,
t1.user_type, t1.fname, t1.lname FROM train_user t1, ticket ti1 WHERE t1.user_id = ti1.user_id AND ti1.departure = 'bengaluru' AND
ti1.arrival='chennai' AND MONTH(ti1.travel_date) = 10 AND YEAR(ti1.travel_date) = 2021 AND ti1.user_id = ti2.user_id);


#PES2UG20CS209 - NAMAN CHOUDHARY
#Q4

SELECT t2.user_id, t2.user_type, t2.fname, t2.lname FROM train_user t2, ticket ti2 WHERE t2.user_id = ti2.user_id AND ti2.departure =
'bengaluru' AND ti2.arrival = 'chennai' AND EXISTS(SELECT t1.user_id,
t1.user_type, t1.fname, t1.lname FROM train_user t1, ticket ti1 WHERE t1.user_id = ti1.user_id AND ti1.departure = 'chennai' AND
ti1.arrival='bengaluru' AND (DAY(ti1.travel_date) = DAY(ti2.travel_date) = 7 )AND ti1.user_id = ti2.user_id);


#PES2UG20CS209 - NAMAN CHOUDHARY
#Q5

SELECT t2.user_id, t2.user_type, t2.fname, t2.lname FROM train_user t2, ticket ti2 WHERE t2.user_id = ti2.user_id AND ti2.departure =
'bengaluru' AND ti2.arrival = 'chennai' AND NOT EXISTS(SELECT t1.user_id,
t1.user_type, t1.fname, t1.lname FROM train_user t1, ticket ti1 WHERE t1.user_id = ti1.user_id AND ti1.departure = 'chennai' AND
ti1.arrival='bengaluru' AND ti1.user_id = ti2.user_id);
