class Stack :
    def __init__(s) :    
        s.items = []

    def push(s,i):       
        s.items.append(i)

    def pop(s) :      
        return s.items.pop()

    def isEmpty(s) : 
        if s.items == [] :
            return True
        else :
            return False
    def size(s) :     
        return len(s.items)


print(" *** Stack implement by Python list***")
ls = [e for e in input("Enter data to stack : ").split()]
s = Stack()

for e in ls:
    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():
    s.pop()

print(s.size(),"Data in stack : ",s.items)