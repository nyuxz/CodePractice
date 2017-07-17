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
       		3. time: O(n), space: O(n)
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


    def isPalindrome_2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        @logit:
       		1. use fast and slow pointer to find the center position
       		2. fast pointer is twice speed of slow pointer, so that when faster pointer
       		reach None, slow pointer at the middle of the linked list
       		3. reverse second half linked list to compare with the first half
       		4. ignore the even/odd length of the linked list, coz slow pointer will alway point
       		to second half linked list.      	
        """

        if not head or not head.next:
            return True

        fast = slow = head

        # fast pointer move two position each time
        # if odd length llist, stop at fast.next.next == None
        # if even length llist, stop at fastnext == None
       	while fast.next and fast.next.next: # pay attention here !!
       		fast = fast.next.next
       		slow = slow.next

       	# make slow pointer alway point to second half of linked list
       	slow = slow.next

       	# reverse second half linked list
       	slow = self.reverseList(slow)

       	while slow:
       		if head.val != slow.val: # we are comparing with the value only
       			return False

       		slow = slow.next
       		head = head.next

       	return True 

    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head






