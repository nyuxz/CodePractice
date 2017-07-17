#160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        @logit:
        	1. using two pointers, go through two linked list respectively.
        	2. O(n)
        	3. detail

        	A:      a1 → a2
                   			↘
                     			c1 → c2 → c3
                   			↗            
			B: b1 → b2 → b3

			let two pointers go through the total length of two llist.

			A': a1 → a2 → c1 → c2 → c3 → None → b1 → b2 → b3 → [c1 → c2 → c3]
			B': b1 → b2 → b3 → c1 → c2 → c3 → None → a1 → a2 → [c1 → c2 → c3]

        """
        if not headA or not headB:
        	return None

        pA = headA
        pB = headB

        while pA and pB and pA != pB:
        	pA = pA.next
        	pB = pB.next

        	if pA == pB:
        		return pA

        	if not pA: # when meet end of linked list A , then continous with linked list B
        		pA = headB

        	if not pB: # when meet end of linked list B , then continous with linked list A
        		pB = headA

        return pA

    def getIntersectionNode_2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        @logit:
        	1. find the length of two linked lists
        	2. find the length difference: diff = |len(A) - len(B)|
        	3. move pointer diff position of longer ahead. 
        """

        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        diff = abs(lenA - lenB)

        if lenA > lenB:
        	for i in range(diff):
        		headA = headA.next #A is longer list, move pinterA diff positions ahead
        elif lenB > lenA:
        	for i in range(diff):
        		headB = headB.next #B is longer list, move pinterB diff positions ahead

        while headA != headB:
        	headA, headB = headA.next, headB.next

       	return headA

    def getLength(self, head):
    	length = 0
    	while head:
    		length += 1
    		head = head.next

    	return length

