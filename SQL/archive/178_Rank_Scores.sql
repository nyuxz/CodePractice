# 178. Rank Scores

select DISTINCT a.Num as ConsecutiveNums
from Logs a, Logs b, Logs c
where a.Num = b.Num and b.Num = c.Num and a.Id = b.Id - 1 and b.Id = c.Id - 1