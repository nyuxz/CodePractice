# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        @logic:
            1. each time swap two nodes and move on to next two
            2. we use a pointer to switch two nodes each time
            3. we use new_head pointer to record the whole linked list
        """
        
        if not head or not head.next:
            return head
        
        pointer = new_head = ListNode(0)

        while head and head.next:
            
            tmp = head.next 
            head.next = tmp.next
            tmp.next = head
            pointer.next = tmp # tmp will be in front of head
            pointer = head # pointer -> head, where pointer always point to the node before current pair
            head = head.next # move to swaping next two nodes pair
            
        return new_head.next


class Solution_2(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        @logic: Recursion
            1. think about create a new llist
            2. each time when we add new nodes, we swap the order
        """
        
        if not head or not head.next:
            return head
        
        new_head = head.next
        
        head.next = self.swapPairs(head.next.next)
        
        new_head.next = head
        
        return new_head