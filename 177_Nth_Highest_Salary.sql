# 177. Nth Highest Salary

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
set M = N-1;
  RETURN (
      select distinct Salary
      from Employee
      order by Salary desc
      limit M,1
  );
END

'''
P.s
1. after declare, set, and return, there must be ';', otherewise will be runtime error. 
'''