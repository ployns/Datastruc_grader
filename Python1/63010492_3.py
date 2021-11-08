print(" *** Summation of each digit ***")
num = int(input("Enter a positive number : "))
sum = 0
while(num>0):
    #digit = n%10
    sum = sum+num%10
    num = num//10
print("Summation of each digit = ",sum)
