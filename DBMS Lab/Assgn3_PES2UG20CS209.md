# Database Management System

<table style="width:100%">
  <tr>
    <th align="left">Name</th>
    <td>Naman Choudhary</td>
  </tr>
  <tr>
    <th align="left">SRN</th>
    <td>PES2UG20CS209</td>
  </tr>
  <tr>
    <th align="left">Section</th>
    <td>D</td>
  </tr>
</table>

# Unit 3 - Assignment

### A)
1. Select all boxes with a value larger than $150

**Answer:**

```Select * from Boxes where value > 150```

2. Select only those warehouses where the average value of the boxes is greater than 150

**Answer:** 

```Select Warehouse, Avg(value) from Boxes Group By warehouse having avg(value) > 150```

3.	Select the codes of all the boxes.  located in Chicago. Use Right Join

**Answer:**

```Boxes.code from warehouses right join boxes on warehouses.code = boxes.warehouse where location = 'Chicago'```

### B) Consider the following schema

Highschooler(ID int, name text, grade int);

Friend(ID1 int, ID2 int);

Likes(ID1 int, ID2 int)

Write a trigger that automatically deletes students when they graduate, i.e., when their grade is updated to exceed 12

**Answer:**

```
new.grade > 12

 begin
     DELETE from Highschooler
     WHERE ID = New.ID
 end
```
