inp = input("Enter a positive number : ")
inp = int(inp)
numbers = '123456789ABCDEF'
lst = []
rev = []
if inp < 16 and inp > 0:
    for i in range(1, inp+1):
        if i < 10:
            lst.append(str(i))
        else:
            lst.append(numbers[i-1])
    for i in reversed(lst):
        rev.append(i)

    print(*lst, sep=" ")
    for i in range(inp-2):
        anwser = str(lst[i+1])
        for _ in range(inp*2-3):
            anwser += ' '
        anwser += str(lst[i])
        print(anwser)
    if inp != 1:
        print(*rev, sep=" ")
elif inp <= 0:
    print(str(inp) + ' is too low.')
elif inp >= 16:
    print(str(inp) + ' is too high.')
