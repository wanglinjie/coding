#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:20160810

'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num = 0
        self.data = []
        self.min_pos = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if self.min_pos and self.data[self.min_pos[-1]] < x:
            self.min_pos.append(self.min_pos[-1])
        else:
            self.min_pos.append(self.num)
        self.num += 1
        

    def pop(self):
        """
        :rtype: void
        """
        if self.data:
            del self.data[-1]
            del self.min_pos[-1]
            self.num -= 1
        
        

    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_pos:
            return self.data[self.min_pos[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()