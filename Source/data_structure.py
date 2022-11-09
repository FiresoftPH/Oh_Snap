# Limited Size Stack

class Stack:
    def __init__(self, data = [], limit = int):
        self.data = data
        self.limit = limit

    def look(self):
        return self.data

    def push(self, item):
        if self.size() == self.limit:
            return "Stack is full"
        else:
            return self.data.insert(0, item)

    def pop(self, index):
        if len(self.data) == 0:
            return "Stack is Empty"
        else:
            return self.data.pop(index)

    def peek(self):
        if len(self.data) == 0:
            return "Stack is Empty"
        else:
            return self.data[0]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.data)

    def search(self, index):
        return self.data[index]

# Node Class for linked list
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data
        
    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

# Singly linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True

            current = current.next
        
        return found

    def remove(self, item):
        current = self.head
        previous = None
        while not found:
            if current.getData() == item:
                found = True

            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()

        else:
            previous.setNext(current.getNext())

    def squish(self):
        current = self.head
        if current is None:
            return None
        while current.next is not None:
            if current.getData() == current.next.getData():
                operation = current.next.next
                current.next = None
                current.next = operation
            else:
                current = current.next

        return self.head
        
    def printList(self):
        operation = self.head
        while (operation):
            print(operation.data)
            operation = operation.next