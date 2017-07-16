#237. Delete Node in a Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def deleteNode_2(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next



if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print ('initial:', head)
    print (Solution().deleteNode_2(2))





'''
ToDo:
1.deleteNode_2 still have bug
2. difference between 
    Deleting a node
    Delete a Linked List node at a given position

Reference:
http://www.geeksforgeeks.org/data-structures/linked-list/
'''