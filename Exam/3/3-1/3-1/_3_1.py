def natural_sum(n):
    if n <= 1 :
        return n
    else :
        return n + natural_sum(n-1)

print(" *** Natural sum ***")
num = int(input("Enter number : ")) 
i = 1
while i <= num :
    print(i,end='')
    i = i+1
    if i <= num :
        print(" + ",end='')

print(" = %.d" %(natural_sum(num)))
