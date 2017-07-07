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



class ListNode(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
def print_llist(n):
  next = n.next
  print (n.val)
  if(next is not None):
    print_llist(next)
    
# Create a linked list
n0 = ListNode(4,None)
n1 = ListNode(3,n0)
n2 = ListNode(2,n1)
n3 = ListNode(1,n2)

print('the initial linked list:')
print_llist(n3)



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
    

    def reverseList(self, head, last = None):
      if not head:
        return last
      next = head.next
      head.next = last
      return self.reverseList(next, head)
    

result = Solution().reverseList(n3)
print_llist(result)


'''
Reference: 
http://www.geeksforgeeks.org/write-a-function-to-reverse-the-nodes-of-a-linked-list/
'''