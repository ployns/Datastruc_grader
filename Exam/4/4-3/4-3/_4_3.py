comparison = 0
def swap(ls, i, last, lastNum):
    global comparison
    if i < 0:
        return ls, last
    else:
        ls, position = swap(ls, i-1, last, lastNum)

        if ls[last] < ls[i]:
            if ls[last] == lastNum:
                position = i
            temp = ls[last]
            ls[last] = ls[i]
            ls[i] = temp
            if i != 0:
                comparison += 1
        return ls, position

def insert(ls, i):
    if i == 0:
        return ls
    else:
        global comparison
        ls = insert(ls, i-1)
        last = i
        lastNum = ls[last]
        comparison += 1
        ls, position = swap(ls, i, last, lastNum)

    return ls

print(' *** Insertion sort ***')
inp = [int(e) for e in input('Enter some numbers : ').split()]
n = len(inp)-1
ls = insert(inp,n)
print()
print(ls)
print('Data comparison = ', comparison)
