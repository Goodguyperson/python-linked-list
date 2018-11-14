class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None

    def printList(self):
            temp = self.head
            while (temp):
                print(temp.value)
                temp = temp.next


newList = LinkedList()

node1 = Node("First")
node2 = Node(2)
node3 = Node(3)

newList.head = node1
node1.next = node2
node2.next = node3

newList.printList()
