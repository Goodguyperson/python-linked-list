class Queue:
    # A queue is a collection or objects that follows a FIFO semantics
    def __init__(self):
        self.items = []

    # returns size of queue
    def size(self):
        return len(self.items)

    # adds element to queue
    def enqueue(self, newItem):
        self.items.insert(0, newItem)

    # removes top element from queue and returns it
    def dequeue(self):
        return self.items.pop()

    # looks at the top element without removing it
    def peek(self):
        return self.items[self.size() - 1]

if __name__ == '__main__':  #Will not run if imported
    newQueue = Queue()

    assert newQueue.size() == 0

    newQueue.enqueue(1)
    newQueue.enqueue(2)
    newQueue.enqueue(3)
    newQueue.enqueue(4)

    assert newQueue.size() == 4
    assert newQueue.peek() == 1
    assert newQueue.dequeue() == 1

    assert newQueue.size() == 3
    assert newQueue.peek() == 2
    assert newQueue.dequeue() == 2

    assert newQueue.size() == 2
    assert newQueue.peek() == 3
    assert newQueue.dequeue() == 3

    assert newQueue.size() == 1
    assert newQueue.peek() == 4
    assert newQueue.dequeue() == 4

    assert newQueue.size() == 0

    print("All done, no errors")
