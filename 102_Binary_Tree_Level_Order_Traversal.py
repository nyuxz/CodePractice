# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/#/description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        @logic: BFS
        """
        recordList = [] # return result is a list of list
        if root == None:
            return recordList
    
        queue = [root]
        
        while len(queue) != 0:
        	# append the value of the nodes, not the current queue
            recordList.append([node.val for node in queue]) # .append(queue) raise error
            
            child = []
            for node in queue:
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
                
                queue = child
            
        return recordList

class Solution_2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        @logic: DFS
            1. preorder dfs traversal the tree nodes
            2. at meantime record the depth of each node
            3. root at depth 0
            4. this solution need more practices 
        """
        
        # this funciton kind like a driver
        recordList = []
        self.pre_dfs(root, 0, recordList)
        return recordList
    
    def pre_dfs(self, root, depth, recordList):
        if root == None:
            return recordList
        
        if len(recordList) < depth+1: #len(recordList) is the depth of root node
            recordList.append([]) #append a new list to record the value of nodes of next level child
            
        recordList[depth].append(root.val)
        self.pre_dfs(root.left, depth+1, recordList)
        self.pre_dfs(root.right, depth+1, recordList)
