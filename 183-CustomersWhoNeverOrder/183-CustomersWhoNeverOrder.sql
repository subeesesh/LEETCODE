-- Last updated: 5/29/2026, 11:57:34 AM
# Write your MySQL query statement below
select c.name as Customers from Customers c 
left join Orders o on c.id=o.customerid 
where o.id is null;