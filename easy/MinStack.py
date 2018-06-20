class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.top_idx = -1
        self.heap_idx = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.top_idx += 1
        self.heap_idx.append(self.top_idx)
        idx = self.top_idx
        while self._parent(idx) >= 0:
            if self.stack[self.heap_idx[idx]] < self.stack[self.heap_idx[self._parent(idx)]]:
                self.heap_idx[idx], self.heap_idx[self._parent(idx)] = self.heap_idx[self._parent(idx)], self.heap_idx[idx]
                idx = self._parent(idx)
            else:
                break

    def pop(self):
        """
        :rtype: void
        """
        if self.top_idx < 0:
            pass
        pop_heap_idx = self.heap_idx.index(self.top_idx)
        if pop_heap_idx == self.top_idx:
            self.stack.pop()
            self.top_idx -= 1
            self.heap_idx.pop()
        else:
            self.heap_idx[pop_heap_idx] = self.heap_idx[self.top_idx]
            self.stack.pop()
            self.top_idx -= 1
            self.heap_idx.pop()
            self._heapify(pop_heap_idx)


    def top(self):
        """
        :rtype: int
        """
        if self.top_idx < 0:
            return None
        else:
            return self.stack[self.top_idx]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[self.heap_idx[0]]

    def _heapify(self, i):
        if i < 0:
            return
        while self._left(i) <= self.top_idx:
            idx_min = i
            if self.stack[self.heap_idx[self._left(i)]] < self.stack[self.heap_idx[idx_min]]:
                idx_min = self._left(i)
            if self._right(i) <= self.top_idx and self.stack[self.heap_idx[self._right(i)]] < self.stack[self.heap_idx[idx_min]]:
                idx_min = self._right(i)
            self.heap_idx[i], self.heap_idx[idx_min] = self.heap_idx[idx_min], self.heap_idx[i]
            if (i == idx_min):
                break
            i = idx_min
        
    def _parent(self, i):
        return (i - 1) / 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(395)
    print(minStack.stack)
    print(minStack.heap_idx)
    print(minStack.top_idx)
    minStack.push(276)
    print(minStack.stack)
    print(minStack.heap_idx)
    print(minStack.top_idx)
    minStack.push(29)
    print(minStack.stack)
    print(minStack.heap_idx)
    print(minStack.top_idx)
    minStack.push(-482)
    print(minStack.stack)
    print(minStack.heap_idx)
    print(minStack.top_idx)
    minStack.pop()
    print(minStack.stack)
    print(minStack.heap_idx)
    print(minStack.top_idx)
    minStack.push(-108)
    print(minStack.stack)
    print(minStack.heap_idx)
    print(minStack.top_idx)
    minStack.push(-251)
    print(minStack.stack)
    print(minStack.heap_idx)
    print(minStack.top_idx)
