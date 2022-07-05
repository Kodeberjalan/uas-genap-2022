class queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printQueue(self):
        print(self.items)
class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)
        return self.items
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    def sort(self):
        return self.items.sort()
    def sortdecending (self):
        return self.items.sort(reverse=True)
    def printStack(self):
        print(self.items)
   
n=int(input('Masukkan jumlah data: '))
q1=queue()
for i in range (n):
    data=int(input('Masukkan data: '))
    q1.enqueue(data)
print('queue 1: ')
q1.printQueue()
s1=stack()

for i in range (n):
    data=q1.dequeue()
    s1.insert(data)
    s1.sort()
print('stack 1: ')
s1.printStack()
s2=stack()
for i in range (n):
    data=s1.pop()
    s2.insert(data)
    s2.sortdecending()
print('stack 2: ')
s2.printStack()
q2=queue()
for i in range (n):
    data=s2.pop()
    q2.enqueue(data)
print('queue 2: ')
q2.printQueue()