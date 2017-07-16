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
        tmp = ListNode(float("-inf"))
        while head:
            tmp.next, head.next, head = head, tmp.next, head.next
        return tmp.next


    def reverseList_3(self, head):
        [begin, end] = self.reverseListRecu(head)
        return begin
    def reverseListRecu(self, head):
        if not head:
            return [None, None]
            
        [begin, end] = self.reverseListRecu(head.next)
        
        if end:
            end.next = head
            head.next = None
            return [begin, head]
        else:
            return [head, head]


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
            p = p.next #this kind of like: let p and p.next linked together, and move to p.next
        return head










