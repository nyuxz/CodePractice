# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode  
        @logic:
            1. if p and q are both greater than root then LCA must at right subtree
            2. if p and q are both less than root then LCA must at left subtree
            3. other cases, LCA must be root itself
        """
        pointer = root
        
        while pointer:
            if p.val > pointer.val and q.val > pointer.val:
                pointer = pointer.right
            
            if p.val < pointer.val and q.val < pointer.val:
                pointer = pointer.left
                
            else:
                return pointer

class Solution_2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        @logic: Recursion
        	1. Same logic with first solution
        """
        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

class Solution_3(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode  
        @logic:
            1. find path from root->p and root->q
            2. find LCA from two path
            3. No need BFS or DFS
        """
        
        path_p = self.findPath(root, p)
        path_q = self.findPath(root, q)
        
        result = root
        for i in range(1, min(len(path_p), len(path_q))):
            if path_p[i] == path_q[i]:
                result = path_p[i]
        return result
    
    def findPath(self, root, node):
        path = []
        while root.val != node.val:
            path.append(root)
            if node.val > root.val:
                root = root.right
            elif node.val < root.val:
                root = root.left
        path.append(node)
        return path
