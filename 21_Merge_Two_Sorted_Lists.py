# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

	def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        @logit: recursion
        """
        # handle empty llist
        if not l1 or not l2:
            return l1 or l2
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2 


    def mergeTwoLists_2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        @logit:
            1.using a pointer to go through two llist
            2.each time we pick up smaller node value
        @note:
        	1.at the beginning we have two pointer head and curr
        	2.as we go through l1 and l2, the rest node of llist decrease
        	3.so curr only have 2 node, which are the last node of l1 and l2
        	4.this is the reason we need another pointer head, to record the merged linked list
        """
        # handle empty llist
        if not l1 or not l2:
            return l1 or l2 
        
        head = curr = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        
        curr.next = l1 or l2
        
        return head.next

