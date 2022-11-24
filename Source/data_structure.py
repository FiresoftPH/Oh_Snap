# Created by Pattarapark Chutisamoot (FiresoftGH)

# Limited Size Stack

class Stack:
    def __init__(self, data = [], limit = int):
        self.data = data
        self.limit = limit

    def look(self):
        return self.data

    def get_data(self, index):
        return self.data[index]

    def push(self, item):
        if self.size() == self.limit:
            return "Stack is full"
        else:
            self.data.insert(0, item)
            return self.peek()

    def pop(self, index):
        if len(self.data) == 0:
            return "Stack is Empty"
        else:
            return self.data.pop(index)

    def peek(self):
        if len(self.data) == 0:
            return "Stack is Empty"
        else:
            return self.data[self.size() - 1]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.data)

    def search(self, index):
        return self.data[index]

    def clear(self):
        self.data = []
        return self.data