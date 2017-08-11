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
        """
        res = []
        queue = [(root, 0)]
        while len(queue) > 0:
            node, depth = queue.pop()
            if node:
                if len(res) <= depth:
                    res.insert(0, [])
                res[-(depth+1)].append(node.val)
                queue.insert(0, (node.left, depth+1))
                queue.insert(0, (node.right, depth+1))
        return res

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
        """
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, depth, res):
        if root:
            if depth >= len(res):
                res.insert(0, [])
            res[-(depth+1)].append(root.val)
            self.dfs(root.left, depth+1, res)
            self.dfs(root.right, depth+1, res)