# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        @logic: Recursion
            1. check left_node.left with right_node.right
            2. check left_node.right with right_node.left
        """
        
        if not root:
            return True 
        
        # a driver
        return self.checkSymm(root.left, root.right) 
        
        
    def checkSymm(self, left_child, right_child):
        
        if not left_child or not right_child:
            return left_child == right_child
        
        if left_child.val != right_child.val:
            return False
        else:
            return self.checkSymm(left_child.left, right_child.right) and self.checkSymm(left_child.right, right_child.left)



class Solution_2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        @logic: DFS, Stack
        """
        if not root:
            return True
        
        # define two stack list
        stack_left , stack_right = [root.left], [root.right]
        
        while len(stack_left)>0 and len(stack_right)>0:
            
            left = stack_left.pop()
            right = stack_right.pop()
            
            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            
            #appending order is important
            stack_left.append(left.left) # append to last
            stack_left.append(left.right)
            stack_right.append(right.right)
            stack_right.append(right.left)
            
        #return len(stack_left) == 0 and len(stack_right) == 0
        return True


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        @logic: BFS, queue
        """
        if not root:
            return True

        queue_left, queue_right= [root.left], [root.right]

        while len(queuel) > 0 and len(queuer) > 0:

            left = queue_left.pop()
            right = queue_right.pop()

            if not left and not right:
                continue

            elif not left or not right:
                return False

            if left.val != right.val:
                return False

            queue_left.insert(0, left.left) # insert at beginning
            queue_left.insert(0, left.right)
            queue_right.insert(0, right.right)
            queue_right.insert(0, right.left)

        return len(queuel) == 0 and len(queuer) == 0




