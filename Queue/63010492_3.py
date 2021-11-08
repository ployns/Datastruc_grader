class Queue:
    def __init__(self, lst = None):
        if lst == None:
            self.items = []
        else:
            self.items = lst

    def dequeue(self):
         return self.items.pop(0)

    def enqueue(self, data):
        self.items.append(data)
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

lst = [str(i) for i in input("Enter code,hint : ").split(',')]
q = Queue()
a = ord(lst[1]) - ord(lst[0][0])

for i in lst[0]:
    q.enqueue(chr(ord(i)+a))
    print(q.items)
