class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        return False

    def push(self, data):
        if self.head == None:
            self.head = node(data)
        else:
            newnode = node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None

        else:
            pnode = self.head
            self.head = self.head.next
            pnode.next = None
            return pnode.data

    def iter(self):
        itnode = self.head
        if self.isempty():
            print('stack is empty')
        else:
            while(itnode != None):
                print(itnode.data, end=" ")
                itnode = itnode.next
            print()
    

mstack = stack()
for i in range(10):
    mstack.push(i)

mstack.iter()

mstack.pop()
mstack.iter()
