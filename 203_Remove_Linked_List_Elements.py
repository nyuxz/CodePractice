# 203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        @logit:
            1. [important] create a fake head to link the the llist (pre) where do not have deleted node 
            2. go through every node. O(n)
        """
        fakeHead = pre = ListNode(0)  # create fake head linking to pre
        pre.next = head
        
        while head:
            if head.val == val:
                pre.next = head.next # skip node with target value
            else:
                pre = pre.next

            head = head.next
        
        return fakeHead.next # which will represent pre