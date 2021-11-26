class node:
    def __init__(self,data,next = None ):
        self.data = data
        if next is None :
            self.next = None
        else :
            self.next = next

    def __str__(self):
        return str(self.data)

    def createList(l=[]):
        if l == [] :
            return node(None)
        else:
            h = node(l[0])
            t = h 
            for i in range(1,len(l)):
                t.next = node(l[i])
                t = t.next
            return h
    def printList(H):
        return self.data(H)

    def mergeOrderesList(p,q):
        newLinked = ''
        newLinked = p + q
        return newLinked

        


inp = input('Enter numbers : ').split('/')
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)
