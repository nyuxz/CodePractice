#237. Delete Node in a Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def __init__(self):
	    self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (" %d " %(temp.val),)
            temp = temp.next

    def deleteNode_2(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node = self.head 
        node.val = node.next.val
        node.next = node.next.next
        
    def deleteNode(self, position):
 
        # If linked list is empty
        if self.head == None:
            return
 
        # Store head node
        temp = self.head
 
        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return
 
        # Find previous node of the node to be deleted
        for i in range(position -1 ):
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
 
        # Unlink the node from linked list
        temp.next = None
 
        temp.next = next

if __name__ == '__main__':
    # create linked list
    llist = Solution()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    llist.push(8)
    print ("Created Linked List: ")
    llist.printList()


    llist.deleteNode(2)
    print ("\nLinked List after Deletion at position 2: ")
    llist.printList()

    llist.deleteNode_2(2)
    print ("\nLinked List after Deletion at position 2: ")
    llist.printList()

'''
ToDo:
1.deleteNode_2 still have bug
2. difference between 
    Deleting a node
    Delete a Linked List node at a given position

Reference:
http://www.geeksforgeeks.org/data-structures/linked-list/
'''