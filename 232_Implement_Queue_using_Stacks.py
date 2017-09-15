'''
operations of queue following:
push(x) – Push element x to the back of queue.
pop() – Removes the element from in front of queue.
peek() – Get the front element.
empty() – Return whether the queue is empty.

operations of stacks following:
push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
empty() – Return whether the stack is empty.
'''

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.inStack.append(x)     

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.move()
        self.outStack.pop() 

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.move()
        return self.outStack[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self.inStack) and (not self.outStack)
    
    def move(self):
        '''
        it moves all elements of the "inStack" to the "outStack" when the "outStack" is empty
        note: inStack里的东西会'倒置'到outStack
        '''
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# P.s.
# Cannot AC ?????