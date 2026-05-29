-- Last updated: 5/29/2026, 11:57:45 AM
# Write your MySQL query statement below
select p.firstName,p.lastName,a.city,a.state from Person p left join  Address a on p.personId=a.personId;   