# 183. Customers Who Never Order

select Name as Customers
from Customers as A
left join Orders as B
on A.Id = B.CustomerId
where B.CustomerId is null

