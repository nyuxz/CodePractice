# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        @logit:
       		1. save linked list value to a empty list
       		2. check if this list is palindrome 
        """

        # empty linked list is palindrome
        if not head or not head.next:
            return True

        valList = []

        while head:
        	valList.append(head.val)
        	head = head.next

        length = len(valList)
       	for i in range(0, length / 2 ):
       		if valList[i] != valList[length - i - 1]:
       			return False

       	return True