#176.Second Highest Salary

# this solution correct but having runtime error
select max(Salary) as SecondHighestSalary
from Employee as E1
where E1.SecondHighestSalary < (select max(Salary) from Employee);

#---------------------------------------------------------------
# the alternative way
select 
(select distinct Salary 
	from Employee 
	order by Salary Desc 
	limit 1 offset 1) as SecondHighestSalary

# P.s.
# offset by 1, which means you skip the first 1 record
# limit by 1, which means only show 1 record 

