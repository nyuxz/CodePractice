#141. Linked List Cycle

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        @logit: 
      		1. loop go through list will be slow, so using dict
      		2. 用dict保存还要考虑到键不能是对象，所以这里采取以对象的id作为键的做法
      		3. O(n)
        """
        map = {}
        while head:
            if id(head) in map:
                return True
            else:
                map[id(head)] = True
            head = head.next #linked list point to next element
        return False


