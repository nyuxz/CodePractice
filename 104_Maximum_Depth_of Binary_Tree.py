# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/#/description


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        @logic: DFS
        """
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution_2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        @logic: BFS
       		1. each time add the child of queue's first node(root) into the queue
       		2. each time we delete the first node in queue
       		3. the child of just-deleted node will be root 

        """
        if root == None:
            return 0
        
        depth = 0
        queue = [root]
        
        while len(queue) != 0:
            depth += 1
            
            for i in range (0, len(queue)):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                
                del queue[0] 
        return depth