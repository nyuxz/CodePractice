# 184. Department Highest Salary

select d.name as Department, e.name as Employee, e.Salary as Salary
from Employee as e, Department as d
where e.DepartmentId = d.Id
and (DepartmentId,Salary) in 
(select e2.DepartmentId, max(e2.Salary)
from Employee e2 
GROUP BY e2.DepartmentId);