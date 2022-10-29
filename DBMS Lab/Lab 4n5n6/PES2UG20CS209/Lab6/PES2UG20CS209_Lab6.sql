#PES2UG20CS209 - NAMAN CHOUDHARY
#Q1

select train.t_name as "TRAIN NAME", avg(v.dist) AS "AVERAGE DISTANCE BETWEEN SUBSEQUENT STATIONS" from train, 
(select * from route_info as ri where ri.TSNum = ri.FSNum+1) as v
where train.train_num=v.t_num
group by v.t_num;


#PES2UG20CS209 - NAMAN CHOUDHARY
#Q2

select train.t_name as "TRAIN NAME", avg(v.dist) AS "AVERAGE DISTANCE BETWEEN SUBSEQUENT STATIONS" from train, 
(select * from route_info as ri where ri.TSNum = ri.FSNum+1) as v
where train.train_num=v.t_num
group by v.t_num
ORDER BY avg(v.dist) DESC ;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q3
select ri.t_num AS "TRAIN NUMBER",
sum(ri.dist) AS  "DISTANCE TRAVELLED" 
from route_info as ri
group by ri.t_num
order by sum(ri.dist) desc;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q4
create view C as
select train.t_name AS TNAME, count(comp.c_num) as num 
from train,comp 
where train.train_num=comp.t_num
group by t_num;

select C.TNAME as "TRAIN",C.num  as "COUNT" FROM C
where C.num = (select MAX(C.num) from C)
union
select C.TNAME as "TRAIN",C.num  as "COUNT" FROM C
where C.num = (select MIN(C.num) from C);

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q5

select uid, count(phone) from phone
where uid="ADM_001" OR uid="USR_006" OR uid="USR_010"
GROUP BY uid;

#PES2UG20CS209 - NAMAN CHOUDHARY
#Q6 
select t_type, avg(farePKM) as "Avg_Fare" 
from faretable 
group by t_type
order by avg(farePKM) DESC;



#PES2UG20CS209 - NAMAN CHOUDHARY
#Q7 - Retrieve all details of the oldest passenger.

SELECT * FROM user where age = (select max(age) from user) ;


#PES2UG20CS209 - NAMAN CHOUDHARY
#Q8 - Count the number of passengers whose name consists of ‘Ullal’. (Hint: Use the LIKE operator)

select count(u.name)as Frequency 
from 
(select * , concat(fname,lname) as name from user) as u
where u.name like "%Ullal%" ;


