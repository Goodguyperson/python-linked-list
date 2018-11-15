class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None

    #Add an element to specified position
    #Appends to start if position = 0 and end if position > size of list
    def addElement(self, position, newNode):
        temp = self.head

        if (position == 0):
            newNode.next = temp
            self.head = newNode
        else:
            for x in range(position - 1):
                if (temp.next != None):
                    temp = temp.next

            nextTemp = temp.next
            temp.next = newNode
            newNode.next = nextTemp

    #Prints current elements in List
    def printList(self):
        temp = self.head

        if (temp == None):
            print("Empty List\n")

        while (temp):
            print(temp.value)
            temp = temp.next


    #Returns size of List
    def length(self):
        temp = self.head
        holder = 0
        while (temp):
            temp = temp.next
            holder += 1

        return holder


    #Finds a Node given value and returns position within list, -1 if not found
    def findElement(self, testValue):
        temp = self.head
        position = 0

        while (temp):
            if (temp.value == testValue):
                return position

            temp = temp.next
            position += 1

        return -1


    #Deletes an element, given value, within the linked list and returns bool depending on success
    def deleteElementGivenValue(self, value):
        temp = self.head.next
        tempPrev = self.head

        if (value == tempPrev.value):
            self.head = temp
            return True
        else:
            while (temp):
                if (temp.value == value):
                    tempPrev.next = temp.next
                    return True

                tempPrev = temp
                temp = temp.next

        return False


    #Deletes an element, given position, within the linked list and returns bool depending on success
    def deleteElementGivenPosition(self, position):
        temp = self.head.next
        tempPrev = self.head
        currPos = 0

        if (position == 0):
            self.head = temp
            return True
        else:
            while (temp):
                if (currPos == position):
                    tempPrev.next = temp.next
                    return True

                tempPrev = temp
                temp = temp.next
                currPos += 1

        return False


    #Checks if one list is equal to another list
    def equals(self, newList):
        temp = self.head
        newTemp = newList.head

        while (temp):
            if (temp.value != newTemp.value):
                return False

            temp = temp.next
            newTemp = newTemp.next

        #checks if end of list
        if (temp == newTemp):
            return True

        return False


    #Reverses a linked list
    def reverse(self):
        prev = None
        temp = self.head

        while (temp):
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next

        self.head = prev


if __name__ == '__main__':  #Will not run if imported
    newList = LinkedList()
    newList1 = LinkedList()
    newList2 = LinkedList()

    node11 = Node(1)
    node12 = Node(2)
    node13 = Node(3)
    node14 = Node(4)

    node21 = Node(1)
    node22 = Node(2)
    node23 = Node(3)
    node24 = Node(4)

    node31 = Node(1)
    node32 = Node(2)
    node33 = Node(3)
    node34 = Node(4)


    print("Test printList and addElement:")

    newList.printList()

    newList.addElement(0, node11)
    newList.addElement(0, node12)
    newList.addElement(2, node13)
    newList.addElement(10, node14)

    newList.printList()

    newList1.addElement(0, node21)
    newList1.addElement(2, node23)
    newList1.addElement(10, node24)

    #Test findElement
    assert newList.findElement(2) == 0
    assert newList.findElement(1) == 1
    assert newList.findElement(3) == 2

    #Test deleteElementGivenValue and compare lists
    assert newList.deleteElementGivenValue(2)
    assert newList.equals(newList1)

    #Test deleteElementGivenPosition and compare lists
    assert newList.deleteElementGivenPosition(0)
    assert newList1.deleteElementGivenValue(1)
    assert newList.equals(newList1)

    #Test Reverse
    newList.reverse()

    newList2.addElement(0, node34)
    newList2.addElement(1, node33)

    assert newList.equals(newList2)

