class Stack :

    def __init__(self,list=None) :
        if list == None:
            self.list = []
        else:
            self.list = list

    def isEmpty(self) :
        return len(self.list) == 0

    def push(self,data) :
        self.list.append(data)

    def pop(self) :
        if self.isEmpty():
            return None
        else:
            return self.list.pop()

    def size(self) :
        return len(self.list)

    def peek(self) :
        return self.list[-1]



def infix2postfix() :
    s = Stack()
    result = ''
    op = set(['+','-','*','/','(',')','^'])
    pr = {'+':1,'-':1,'*':2,'/':2,'^':3}
    #print(" ***Infix to Postfix***")
    token = input("Enter Infix : ")

    for i in token:
        if i not in op:
            result += i
        elif i == '(':
            s.push('(')
        elif i == ')':
            while s.size() and s.peek() != '(':
                result += s.pop()
            s.pop()
        else:
            while s.size() and s.peek() != '(' and pr[i] <= pr[s.peek()]:
                result += s.pop()
            s.push(i)
    while not s.isEmpty():
        result += s.pop()

    print('Postfix : ', end='')
    print(result)

infix2postfix()