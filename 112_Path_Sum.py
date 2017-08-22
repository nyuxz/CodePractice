# 112. Path Sum
# https://leetcode.com/problems/path-sum/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if not root:
            return False 
        
        # check if current node is leaf node
        if not root.left and not root.right:
            return True if sum == root.val else False
        
        else:
        	# if not leaf node, update sum to sum - node.val
            sum -= root.val
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        


class Solution_2(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        @logic: Stack
        """
        
        stack = [(root, sum)]
        
        while len(stack) > 0:
            node, current_sum = stack.pop()
            
            if node:
                if not node.left and not node.right and node.val == current_sum:
                    return True
                
                stack.append((node.right, current_sum - node.val))
                stack.append((node.left, current_sum - node.val))
            
        return False


class Solution_3(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        @logic: Queue
        """
        
        queue = [(root, sum)]
        
        while len(queue) > 0:
            node, current_sum = queue.pop()
            
            if node:
                if not node.left and not node.right and node.val == current_sum:
                    return True
                
                queue.insert(0, (node.right, current_sum - node.val))
                queue.insert(0, (node.left, current_sum - node.val))
            
        return False


class Solution_4(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        @logic: record the path
        """
        pre, cur = None, root
        cur_sum = 0
        stack = []

        while cur or len(stack) > 0:

            while cur:
                stack.append(cur)
                cur_sum += cur.val
                cur = cur.left

            cur = stack[-1]

            if not cur.left and not cur.right and cur_sum == sum:
                return True

            elif cur.right and pre != cur.right:
                cur = cur.right

            else:
                pre = cur
                # del leaf node
                stack.pop()
                # del leaf value
                cur_sum -= cur.val
                cur = None

        return False


