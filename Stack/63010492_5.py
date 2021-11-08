class Stack:
    def __init__(s) :    
        s.items = []
    def push(s,i):       
        s.items.append(i)
    def pop(s):
        return s.items.pop()
    def __str__(s):
        s = ""
        for i in s.items:
            s += str(i) + " "
        return s
    def size(s):
        return len(s.items)
    def is_empty(s):
        return s.size() == 0

s = Stack()
def dec2bin(decnum):
    while decnum > 0:
        t = decnum%2
        s.push(t)
        decnum = decnum//2 
        answer = ''
    while not s.is_empty():
        answer = answer+str(s.pop())
        

    return answer


print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))


