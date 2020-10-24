class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = [None] * k
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if not self.isEmpty():
            self.front -= 1
            if self.front == -1:
                self.front = len(self.deque) - 1
        self.deque[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if not self.isEmpty():
            self.rear += 1
            if self.rear == len(self.deque):
                self.rear = 0
        self.deque[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.deque[self.front] = None

        if not self.isEmpty():
            self.front += 1
            if self.front == len(self.deque):
                self.front = 0
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.deque[self.rear] = None

        if not self.isEmpty():
            self.rear -= 1
            if self.rear == -1:
                self.rear = len(self.deque) - 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear and self.deque[self.front] is None

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self.front == self.rear:
            return False
        elif self.front < self.rear:
            if self.front == 0 and self.rear == len(self.deque) - 1:
                return True
            else:
                return False
        elif self.front > self.rear:
            if self.front - self.rear == 1:
                return True
            else:
                return False
        else:
            return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()