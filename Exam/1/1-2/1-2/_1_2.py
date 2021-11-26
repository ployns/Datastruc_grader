inp = int(input("Input : "))
if inp > 0 :
    print("")
i = 1
j = inp*2 - 2

for e in range(inp): 
    for e in range(i):
        print('*', end="")
    for e in range(j):
        print(' ', end="")
    for e in range(i):
        print('*', end="")
    i = i+1
    j = j-2
    print()
i = i-1
j = j+2

for e in range(inp-1):
    i = i-1
    j = j+2
    for e in range(i):
        print('*', end="")
    for e in range(j):
        print(' ', end="")
    for e in range(i):
        print('*', end="")
    print()

if inp <= 0 :
    print('!!!Please enter number greater than zero!!!')
