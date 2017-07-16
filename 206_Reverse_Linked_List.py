# 206. Reverse Linked List

'''
Input : Head of following linked list  
       1->2->3->4->NULL
Output : Linked list should be changed to,
       4->3->2->1->NULL

Input : Head of following linked list  
       1->2->3->4->5->NULL
Output : Linked list should be changed to,
       5->4->3->2->1->NULL

Input : NULL
Output : NULL

Input  : 1->NULL
Output : 1->NULL
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = head
        rest = None
    
        while (first is not None):
            next = first.next
            first.next = rest
            rest = first
            first = next

        return rest

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print ('initial:', head)
    print ('reversed:',Solution().reverseList(head))


'''
Reference: 
http://www.geeksforgeeks.org/write-a-function-to-reverse-the-nodes-of-a-linked-list/
'''

class Solution_2(object):

    def reverseList_2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head: #while head exist and not None 
            p = head
            head = head.next
            p.next = new_head #let p.next and new_head linked together, and move to new_head
            new_head = p #no link new_head and p, just move from new_head to p
        return new_head


    def reverseList_3(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        @logit: Recursion
        """
        if not head or not head.next:
            return head

        p = head.next
        n = self.reverseList(p)

        # thinking linked list only have two elements.
        # [head -> None] will reverse to [None -> head]
        head.next = None
        p.next = head
        return n


    def reverseList_4(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        @logit:
            1. using a stack, push llist to stack and then pop up to print
        """

        # push to a stack
        p = head
        newList = []
        while p:
            newList.insert(0, p.val)
            p = p.next

        # pop up from stack
        p = head
        for v in newList:
            p.val = v
            p = p.next 
        return head










