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


class Solution_2(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        @logic: Stack
            1. Tree traversal without using recursion, we use stack instead.
            2. stack =[] almost like a list in python data structure  
                *stack.pop(): get last element and del it from current list
                *stack.append(): adding new element just like what list did
        """
        if root == None:
            return root
        
        #define a sack
        stack = [root]
        
        while len(stack) != 0:
            node = stack.pop() #pop up last element of the stack
            
            #invert
            node.left, node.right = node.right, node.left
            
            #attention here! -> append after invert 
            if node.left:
                stack.append(node.left) #append at the last of the stack
            if node.right:
                stack.append(node.right)
                
        return root

class Solution_3(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        @logic: BFS, Queue
            1. this way kind same with using stack
            2. instead of pop up last element each time, we take head of the queue
            3. also, new child node will put into last of the queue
            4. each time after invert child node, we should delete current node.
        
        @note:
            1. why if i define node = queue[0], and then using node.left instead of using queue[0].left, cannot AC.
            saying: Time Limit Exceeded
        """
        if root == None:
            return root
        
        # define a queue
        queue = [root]
        
        while len(queue) != 0:
            
            #node = queue[0]
            
            #invert
            queue[0].left, queue[0].right = queue[0].right, queue[0].left
            
            #attention here! -> append after invert 
            if queue[0].left:
                queue.append(queue[0].left) 
            if queue[0].right:
                queue.append(queue[0].right)
            
            del queue[0]
                
        return root

    