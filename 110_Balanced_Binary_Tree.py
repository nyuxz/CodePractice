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
        	2. inefficient, coz need to calculate the depth of some sub-nodes multiple times.
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
            

class Solution_2(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        @logit: 
        	1. much efficient than the solution 1,
        	coz for each node, we only calculate the depth once, no repeat extra calculations.
        	2. define the function to get the depth of all nodes in one times, and save the depth into .val
        """
    	if root == None:
       		return True
	
		# get the depth of all nodes and save the values
        self.getAllDepth(root) 

        left_depth = root.left.val if root.left else 0 # should give None type a value of 0
        right_depth = root.right.val if root.right else 0 

        if abs(left_depth - right_depth) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def getAllDepth(self, root):
        if root == None:
            return 0 # if [root.val = 0] will have error: 'NoneType' object has no attribute 'val'
        else: 
            root.val = 1 + max(self.getAllDepth(root.left), self.getAllDepth(root.right))
        
        return root.val

class Solution_3(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        @logit: 
        	1. DFS traversal the tree, and just record if the tree is balance or not, save the space without record depth
            2. using -1 to indicate the tree is unbalance
  
        """
        return self.dfs(root) != -1
    
    def dfs(self, root):
        
    	if root == None:
       		return True
        
        left_depth = self.dfs(root.left)
        if left_depth == -1:
            return -1
        
        right_depth = self.dfs(root.right)
        if right_depth == -1:
            return -1
        
        if abs(left_depth - right_depth) <= 1:
            return 1 + max(left_depth, right_depth)
        else:
            return -1


