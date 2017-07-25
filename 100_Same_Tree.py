# 100. Same Tree
# https://leetcode.com/problems/same-tree/#/description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        @logic: Recurrsion, DFS
        """
        
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(q.right, p.right)

        return p == q 

    def isSameTree_2(self, p, q):
    	return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q


class Solution_2(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        @logic: Stack(Alternative way of recurrsion)
        """
        stack = [(p,q)]
        
        while stack:
            p, q = stack.pop()
            
            if p == None and q == None: # condition on node
                continue
            if p == None or q == None:
                return False
            
            if p.val == q.val: # condition on node.val
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
            else:
                return False
        
        return True

'''
P.s.
p.val == None will raise error: 'NoneType' object has no attribute 'val'
node can be None, but node's value cannot be None

[if p == q] will raise error, [if p is q] will work
node cannot compare, we can only compare its value (node.val)
'''

#```````````````````````````````````````````
# ToDo
class Solution_3(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        @logic: Queue, BFS

        @note: Not AC -> Time Limit Exceeded
        """
        queue = [(p, q)]
        
        while len(queue) != 0:
            p, q = queue[0]
            
            if p == None and q == None: 
                continue
            if p == None or q == None:
                return False
            
            if p.val == q.val:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))

                del queue[0]
            else:
                return False
        
        return True