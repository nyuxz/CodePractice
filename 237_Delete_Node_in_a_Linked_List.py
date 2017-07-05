#237. Delete Node in a Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def __init__(self):
	    self.head = None
        
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if self.head == None:
            return
        
        temp = self.head
        
        if node == 0:
            self.head = temp.next
            temp = None
            return

		# Find previous node of the node to be delete
        for i in range(node -1 ):
            temp = temp.next
            if temp is None:
                break

		# If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

		# Node temp.next is the node to be deleted
		# store pointer to the next of node to be deleted
        next = temp.next.next

		# Unlink the node from linked lis
        temp.next = None
        
        temp.next = next
        