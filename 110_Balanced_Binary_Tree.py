# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        @logit: 
        	1. traditional way
        """
    	if root == None:
       		return True

        left_depth = self.getDepth(root.left) # call function cannot having self as input
        right_depth = self.getDepth(root.right)

        if abs(left_depth - right_depth) <= 1:
        	return self.isBalanced(root.left) and self.isBalanced(root.right) 
        else:
        	return False

    def getDepth(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.getDepth(root.left), self.getDepth(root.right))
            
