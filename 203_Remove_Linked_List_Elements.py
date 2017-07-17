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

    def removeElements_2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        @logit:
            1. using fast and slow two pointers
            2. fast pointer go through every node, if the node.val != val,
            then pass the value to slow pointer
            3. speed of fase pointer is same, but fast pointer is one position ahead of slow pointer
            4. we can using slow pointer to change the val of the linked list which do not include target value.
        """
    
        newHead = ListNode(0)
        newHead.next = head
       
        fast = head #fast pointer is one position ahead slow pointer 
        slow = newHead
       
        while fast:
            if fast.val != val:
                slow.next.val = fast.val
                slow = slow.next
               
            fast = fast.next 
       
        slow.next = None #善始善终
       
        return newHead.next #represent the llist slow poiner pointed






