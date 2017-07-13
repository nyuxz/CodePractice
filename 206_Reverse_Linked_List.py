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
 
    def recurse(self, head, rest):
      if head is None:
        return rest
      next = head.next
      head.next = rest
      return recurse(next, head)


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