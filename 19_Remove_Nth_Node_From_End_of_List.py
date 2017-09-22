# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        @logic:
            1. use two pointer, one pointer is n+1 ahead another one at the inital position
            2. when faster pointer reach the end of the llist, 
                the slow pointer should reach the node which one position ahead the to-delete node
        """
        new_head = ListNode(0)
        
        new_head.next = head
        
        # my understanding is to tread slower and faster as pointer as well as copy of new_head llist 
        faster = slower = new_head
        
        # make faster pointer n+1 step ahead
        for i in range(n+1):
            faster = faster.next
            
        while faster:
            faster = faster.next
            slower = slower.next
        
        # delete node   
        slower.next = slower.next.next
        
        # coz new_head linked with slower pointer, where new_head.next refer to slower llist
        return new_head.next


class Solution_2(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        @logic: using index
        	1. change node value
        """
        def getIndex(node):
            if not node:
                return 0
            index = getIndex(node.next) + 1
            if index > n:
                node.next.val = node.val
            return index
        getIndex(head)
        return head.next

class Solution_3(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        @logic: index
        	1. not change node value
        """
        def remove(node):
            if not node:
                return 0, node
            index, node.next = remove(node.next)
            next_node = node if n != index+1 else node.next
            return index+1, next_node
        ind, new_head = remove(head)
        return new_head


'''
P.s.
It looks that linked list in python is associate with index
solutuon_2 and solution_3 need more understanding
'''
