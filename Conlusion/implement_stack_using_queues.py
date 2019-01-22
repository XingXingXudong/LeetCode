# coding: utf-8

from collections import deque


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        if len(self.queue) == 1:
            return self.queue.popleft()
        self._adjust()
        return self.queue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        rtn = self.pop()
        self.queue.append(rtn)
        return rtn

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0

    def _adjust(self):
        """
        Adjust the queue.
        """
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.empty() == False
    assert stack.top() == 2
    assert stack.pop() == 2
    stack.push(3)
    assert stack.pop() == 3
    assert stack.top() == 1
    assert stack.pop() == 1
    assert stack.empty() == True


