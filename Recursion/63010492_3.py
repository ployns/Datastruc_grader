def gcd(x,y):
    if y == 0:
        return x
    if x%y == 0:
        return y
    return gcd(y,x%y)

inp = input("Enter Input : ").split()
if inp[0] == '0' and inp[1] == '0':
    print("Error! must be not all zero.")
elif inp[0] == '0' and int(inp[0]) > int(inp[1]):
    print("The gcd of {} and {} is : {}".format(inp[0],inp[1],gcd(abs(int(inp[1])),abs(int(inp[0])))))
elif inp[1] == '0' and int(inp[1]) > int(inp[0]):
    print("The gcd of {} and {} is : {}".format(inp[1],inp[0],gcd(abs(int(inp[0])),abs(int(inp[1])))))
elif abs(int(inp[0])) > abs(int(inp[1])):
    print("The gcd of {} and {} is : {}".format(inp[0],inp[1],gcd(abs(int(inp[0])),abs(int(inp[1])))))
else:
    print("The gcd of {} and {} is : {}".format(inp[1],inp[0],gcd(abs(int(inp[1])),abs(int(inp[0])))))
