# coding: utf-8


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self._min:
            self._stack.append(self._min)
            self._min = x
        self._stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        p = self._stack.pop()
        if p == self._min:
            self._min = self._stack.pop()
        return p

    def top(self):
        """
        :rtype: int
        """
        if self._stack:
            return self._stack[-1]
        else:
            return None
        
    def getMin(self):
        """
        :rtype: int
        """
        return self._min

    def __str__(self):
        return "<Stack>: " + str(self._stack) + "\nmin = " + str(self._min)
        

if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    minStack = MinStack()
    print(minStack)
    minStack.push(0)
    print(minStack)
    minStack.push(1)
    print(minStack)
    minStack.push(0)
    print(minStack)
    minStack.getMin()
    print(minStack)
    minStack.pop()
    print(minStack)
    minStack.top()
    print(minStack)
    minStack.getMin()
    print(minStack)
