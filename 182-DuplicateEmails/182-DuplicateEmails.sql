-- Last updated: 5/29/2026, 11:57:38 AM
# Write your MySQL query statement below
SELECT email 
FROM Person 
GROUP BY email 
HAVING COUNT(email)>1;