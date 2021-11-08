class Queue:
    def __init__(self, lst = None):
        if lst == None:
            self.items = []
        else:
            self.items = lst

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        return 'Number in Queue is :  ' + str(self.items)

    def dequeue(self):
        if self.isEmpty():
            return print(-1)
        return print('Pop', self.items.pop(0), 'size in queue is', self.size())

    def enqueue(self, data):
        self.items.append(data)
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


lst = [str(i) for i in input("Enter Input : ").split(',')]

q = Queue()

for i in lst:
    i = i.split()
    if i[0] == 'E':
        print('Add', q.enqueue(i[1]), 'index is', q.size()-1)
    elif i[0] == 'D':
        q.dequeue()

print(q)