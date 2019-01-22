# coding: utf-8

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_out = list()
        self.stack_in = list()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack_in.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack_out:
            self._move_to_out()
        return self.stack_out.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stack_out:
            self._move_to_out()
        return self.stack_out[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack_in) == 0 and len(self.stack_out) == 0

    def _move_to_out(self):
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        
if __name__ == '__main__':
    myqueue = MyQueue()
    myqueue.push(1)
    myqueue.push(2)
    assert myqueue.pop() == 1
    assert myqueue.peek() == 2
    assert myqueue.empty() == False
    myqueue.push(3)
    assert myqueue.pop() == 2
    assert myqueue.pop() == 3
    assert myqueue.empty() == True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

