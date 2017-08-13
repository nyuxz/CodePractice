# 107. Binary Tree Level Order Traversal II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        @logic: BFS
        """
        # result is a list of list
        result = []
        
        # queue record the node and depth
        queue = [(root, 0)]
        
        while len(queue) > 0: 
            
            node, depth = queue.pop()
            
            if node:
                # if we move to next depth 
                if len(result) <= depth:
                    # we will create a new list of list to record node.val
                    result.insert(0, [])
                # append node.val at last list of result list   
                result[-(depth+1)].append(node.val)
                
                queue.insert(0, (node.left, depth+1))
                queue.insert(0, (node.right, depth+1))
        
        return result
                

class Solution_2(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        stack = [(root, 0)]
        while len(stack) > 0:
            node, depth = stack.pop()
            if node:
                if len(res) <= depth:
                    res.insert(0, [])
                res[-(depth+1)].append(node.val)
                stack.append((node.right, depth+1))
                stack.append((node.left, depth+1))
        return res

class Solution_3(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        @recursion
        """
        result = []
        self.dfs(root, 0, result)
        return result

    def dfs(self, root, depth, result):
        if root:
            if depth >= len(result):
                result.insert(0, [])
            result[-(depth+1)].append(root.val)
            self.dfs(root.left, depth+1, result)
            self.dfs(root.right, depth+1, result)



