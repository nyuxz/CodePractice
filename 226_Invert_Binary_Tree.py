# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/#/description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        @logic: Recursion 
        """
        if root == None:
            return root
        
        tmp = root.left
        
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        
        return root