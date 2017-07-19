# 202. Happy Number

class Solution(object):
  def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    @logit:
      1. create list to record the sum result. 
      2. if new result is in this dict, return False
      3. % - take remainder
      4. / - division
    """

    sum_dict = []

    while True:

      sum_dict.append(n)

      sum = 0

      while n > 0:
        sum += (n%10)**2
        n = n/10
      if sum == 1: 
        return True
      elif sum in sum_dict:
        return False
      else:
        n = sum