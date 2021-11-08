def odd_list(alist):
    oddList = []
    for x in alist:
        if x % 2 == 1:
            oddList.append(x)

    return oddList
    

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
#print(ls)

opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
