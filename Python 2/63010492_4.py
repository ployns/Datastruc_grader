def hbd(age):
    if age%2 == 0 :
        a = 20
    else :
        a = 21
    b = age//2
    return ("saimai is just " + str(a) + ", in base " + str(b) + "!")

year = input("Enter year : ")
print(hbd(int(year)))

