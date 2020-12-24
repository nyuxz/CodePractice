# 197. Rising Temperature

select w2.Id 
from Weather w2, Weather w1
where w2.Temperature > w1.Temperature 
and datediff(w2.Date, w1.Date) = 1
'''
P.s.
1. w2.Date greater than w1.data, pay attention to args order of datediff()
'''

#--------------------------------------------------------------------------------

select W2.Id
from Weather W1, Weather W2
where to_days(W1.Date)+1 = to_days(W2.Date) and W1.Temperature < W2.Temperature
'''
P.s.
1. we are not using '==' in where clause 
2. to_days function change date to day
'''



'''
# not work
select Cast(W2.Id as int)
from Weather as W1, Weather as W2
where Cast(W2.Id as int) = Cast(W1.Id as int) +1  and W1.Temperature < W2.Temperature
'''