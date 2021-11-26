inp = input("Enter number end with (-1) : ").split()
answer = 0
for e in inp:
    if int(e) == -1:
        answer = 1
if answer == 0 :
    print("Invalid INPUT !!!") #ตรวจสอบว่ามี -1 มั้ย
else :
    lst = []
    for e in inp:
        if int(e) != -1 :
            lst.append(e)    #นำตัวที่ไม่ใช่ -1 เก็บเข้าลิส
        else :
            break

    a =0
    for e in range(len(lst)):
        number = lst.count(lst[e])  #นับจำนวนแต่ละตัว
        if number > len(lst)/2:
            if number == 0  :
                a == 0
            elif number > 0 :
                a = number
                num = lst[e]
    if a == 0 :
        print("Not found")
    else:
        print(num)
