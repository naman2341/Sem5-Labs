#PES2UG20CS209 - NAMAN CHOUDHARY
#Q1

SELECT from_station_name, to_station_name, AVG(distance) distance FROM `route_info` GROUP BY from_station_name, to_station_name;


#PES2UG20CS209 - NAMAN CHOUDHARY
#Q2

SELECT from_station_name, to_station_name, AVG(distance) distance FROM `route_info` GROUP BY from_station_name, to_station_name ORDER BY AVG(distance) DESC;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q3

SELECT Train_No, AVG(distance) distance FROM `route_info` GROUP BY Train_No ORDER BY AVG(distance) DESC;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q4

SELECT train.Train_name, MIN(capacity) FROM `train`, `compartment` WHERE train.Train_no=compartment.train_number GROUP BY (compartment.train_number) LIMIT 1;


#PES2UG20CS209 - NAMAN CHOUDHARY
#Q5

SELECT passenger.phone, User_ID from `passenger` where User_ID='ADM_001' or User_ID='USR_006' or User_ID='USR_010'

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q6 

SELECT AVG(fare_per_km) as AVG_FARE, train_type FROM `fare` GROUP BY train_type;


#PES2UG20CS209 - NAMAN CHOUDHARY
#Q7

SELECT * from `passenger` WHERE age=(SELECT MAX(age) FROM `passenger`);


#PES2UG20CS209 - NAMAN CHOUDHARY
#Q8

SELECT COUNT(*) FROM `ticket_passenger` WHERE Name LIKE '%Ullal';
