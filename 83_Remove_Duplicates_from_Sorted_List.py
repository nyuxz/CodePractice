# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        @logit:
            1. recursion
        """
        # empty llinst and one-element llinst 
        if not head or not head.next:
            return head
        
        head.next = self.deleteDuplicates(head.next)
        
        if head.val != head.next.val:
            return head
        else:
            return head.next
            

    def deleteDuplicates_2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        @logit:
            1. a pointer gp through every node and check if node.next.val = node.val
        """
        
        # we use a pointer point to head of the linked list 
        # is kind of like we use this pointer represent this llist.
        pointer = head
        
        while pointer:
            if pointer.next and pointer.next.val == pointer.val:
                pointer.next = pointer.next.next # pointer skip duplicated node, 
                                                 # represent we delete this node from linked list.
            else:
                pointer = pointer.next
        
        return head

    def deleteDuplicates_3(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        @logit:
            1. fast, slow pointer

        @To-Do: didn't AC
        """
        
        if not head or not head.next:
            return head
        
        newHead = ListNode(0)
        newHead.next = head
        
        fast = head
        slow = newHead
        
        pre = 0 
        
        while fast:
            
            if fast.val != slow.val:
                slow.next.val = fast.val
                slow = slow.next
            else:
                pre = fast.val
            
            while fast.val == pre:
                fast = fast.next
            
        slow.next = None
    
        return newHead.next
        


