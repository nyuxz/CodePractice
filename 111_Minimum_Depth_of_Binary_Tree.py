# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/#/description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        @logic: DFS
        """
        if root == None:
            return 0
        
        if root.left == None: # if left child is None, then only count for right sub-tree
            depth = 1 + self.minDepth(root.right)
            
        elif not root.right: # if right child is None, then only count for left sub-tree
            depth = 1 + self.minDepth(root.left)
            
        else: # if both side child is not None, count for smaller one
            depth = 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
        return depth

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        @logic: BFS
			1. using queue, return when any of the root in the first of the queue do not have child.
			2. there is only one difference comparing with maxDepth problem
        """
        if root == None:
            return 0
        
        depth = 0
        queue = [root]
        
        while len(queue) != 0:
            depth += 1
            
            for i in range (0, len(queue)):

            	# this is the only difference comparing with count for maximun depth
                if not queue[0].left and not queue[0].right:
                    return depth

                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                
                del queue[0] 
        return depth

