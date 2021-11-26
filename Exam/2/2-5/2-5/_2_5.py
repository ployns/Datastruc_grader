class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

def findMean(l) :
    a = l.head
    total = 0
    while a.next is not None :
        total += int(a.data)
        a = a.next
    total += int(a.data)
    print(total/len(l))

def findMedian(l) :
    if (len(l)+1)/2 % 10 == 0 :
        A = l.nodeAt((len(l)+1)/2)
        print(int(A))
    else :
        print(int(l.nodeAt((len(l)+1)/2))+int(l.nodeAt((len(l)+1)/2)+1))


inputlist = [int(e) for e in input('Enter numbers : ').split()]

l = LinkedList()

for data in inputlist:
    l.append(data)

print("Output :")
print(l)
print('Amount of data =', len(l))
findMean(l)


