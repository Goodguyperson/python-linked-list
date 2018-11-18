class Stack:
    # A stack is a collection or objects that follows a LIFO semantics
    def __init__(self):
        self.items = []

    # returns size of stack
    def size(self):
        return len(self.items)

    # adds element to stack
    def push(self, newItem):
        self.items.append(newItem)

    # removes top element from stack and returns it
    def pop(self):
        return self.items.pop()

    # looks at the top element without removing it
    def peek(self):
        return self.items[self.size() - 1]

if __name__ == '__main__':  #Will not run if imported
    newStack = Stack()

    assert newStack.size() == 0

    newStack.push(1)
    newStack.push(2)
    newStack.push(3)
    newStack.push(4)

    assert newStack.size() == 4
    assert newStack.peek() == 4
    assert newStack.pop() == 4

    assert newStack.size() == 3
    assert newStack.peek() == 3
    assert newStack.pop() == 3

    assert newStack.size() == 2
    assert newStack.peek() == 2
    assert newStack.pop() == 2

    assert newStack.size() == 1
    assert newStack.peek() == 1
    assert newStack.pop() == 1

    assert newStack.size() == 0

    print("All done, no errors")
