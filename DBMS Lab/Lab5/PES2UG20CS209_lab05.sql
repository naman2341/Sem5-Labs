#PES2UG20CS209 - NAMAN CHOUDHARY
#Q1 a)

CREATE VIEW compute_ticket_price AS
SELECT Ticket.PNR,ticket.Train_No,ticket.Departure,ticket.Arrival, route_info.Distance,fare_table.Fare_Per_Km
FROM ticket,route_info,fare_table WHERE(ticket.Train_No=route_info.Train_No AND
ticket.Departure=route_info.From_Station_name AND ticket.Arrival=route_info.To_Station_Name AND fare_table.Train_Type=ticket.Train_Type AND fare_table.Compartment_Type=ticket.Compartment_Type);

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q1 b)

CREATE VIEW passenger_num AS
SELECT PNR, COUNT(PNR) AS
numbers from Ticket_passenger group by PNR;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q1 c)

UPDATE payment_info AS
Payment INNER JOIN compute_ticket_price AS ComputePrice ON Payment.PNR = ComputePrice.PNR
INNER JOIN passenger_num AS PassengerNum
ON ComputePrice.PNR = PassengerNum.PNR
SET Payment.Price = ComputePrice.Distance * ComputePrice.Fare_Per_Km * PassengerNum.numbers;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q2

SELECT
train.Train_No,train.Train_Name,route_info.From_Station_No,route_info.From_Station_name, route_info.To_Station_No,route_info.To_Station_Name,route_info.Distance
FROM train NATURAL JOIN route_info;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q3

SELECT DISTINCT train.Train_No,train.Train_Name
FROM train INNER JOIN compartment
WHERE train.Source='Bengaluru' AND train.Destination='Chennai' AND compartment.Availability>10;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q4

SELECT train_user.firstName,train_user.lastName FROM train_user INNER JOIN ticket INNER JOIN payment_info
WHERE train_user.User_ID=ticket.passenger_id AND payment_info.PNR=ticket.PNR AND payment_info.Price >500;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q5

SELECT DISTINCT train_user.firstname,train_user.lastname,train_user.dob,ticket.pnr FROM train_user
LEFT OUTER JOIN ticket ON train_user.user_id=ticket.passenger_id WHERE ticket.pnr IS NOT NULL;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q6

select train_user.firstname, train_user.lastname
from train_user left outer join ticket on train_user.user_id = ticket.passenger_id
where ticket.pnr is not null;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q7

SELECT
ticket.pnr,ticket.train_No,ticket.travel_Date,train_user.firstname,train_user. lastname
FROM ticket RIGHT OUTER JOIN train_user ON ticket.passenger_id = train_user.user_id;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q8

SELECT ticket.passenger_id ,train.train_No,train.train_name FROM ticket RIGHT OUTER JOIN train
ON train.train_no = ticket.train_no;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q9

select mang.train_no, mang.train_name from (
select train.train_no, train.train_name from train natural join ticket where ticket.departure_time != "8:30")
as mang where mang.train_no not in (select train.train_no from train join route_info on train.train_no = route_info.train_no
where destination ="Mangaluru" and distance < 100);

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q10

ect temp.passenger_id from (
select sum(price) as total_price, ticket.passenger_id from ticket natural join payment_info group by passenger_id)
as temp where total_price > (select avg(payment_info.price) from payment_info);
