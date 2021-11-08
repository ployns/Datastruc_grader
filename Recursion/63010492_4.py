def Hanoi(start, source, end, aux):
    if start>0:
        Hanoi(start-1, source, aux, end)
        lst[aux-1].append(lst[source-1].pop())
        print("move",start,"from ",chr(ord('A')+source-1), "to" ,chr(ord('A')+aux-1))
        print('|  |  |')
        printl(n,lst[0],lst[1],lst[2])
        Hanoi(start-1, end, source, aux)

def printl(n, p1, p2 ,p3):
    if n!=0:
      if len(p1) >= n:
         print(p1[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      if len(p2) >= n:
         print(p2[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      if len(p3) >= n:
         print(p3[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      print()
      printl(n-1,p1,p2,p3)
    else:
        return

def init(n):
    if n == 0:
        return []
    return [n] + init(n-1)

n= int(input("Enter Input : "))
lst = [[],[],[]]
lst[0] = init(n)
print('|  |  |')
printl(n,lst[0],lst[1],lst[2])
Hanoi(n,1,2,3)