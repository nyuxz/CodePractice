# 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/description/

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

'''
@logic: 
队列是先进先出, 每次出只能出队列的头部, 栈是后进先出
想办法每次把入队的元素弄到队列头部. 
可以考虑在每次push到队列的时候对其他元素做个重新pop和push将当前元素转移到队头. 
'''

class MyStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.insert(0, x)
        for i in range(len(self.stack)-1):
            self.stack.insert(0, self.stack[-1])
            self.stack.pop()

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()