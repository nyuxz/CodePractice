# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        parentheses_map = {')': '(', '}': '{', ']': '['}
        
        paren_stack = [None] #initialize stack as None, otherwise if empty will raise error: cannot pop up
        
        for i in s:
            
            # check if i is the key of parentheses_map such as ),},]
            if i in parentheses_map:
                if parentheses_map[i] != paren_stack.pop():
                    return False
            else:
                # [,{,( will be at the end of hte stack
                paren_stack.append(i)
                
        return len(paren_stack) == 1