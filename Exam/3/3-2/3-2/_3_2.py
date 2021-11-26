def findMinimum(data):
   if len(data) == 1 :
        return data[0]
   else :
        minnumber = findMinimum(data[1:])
        Min = data[0]
        if minnumber < Min :
            Min = minnumber 
        return Min

inp = list(map(int,input('Enter Input : ').split(' ')))
print(("Min : {}").format(findMinimum(inp)))

