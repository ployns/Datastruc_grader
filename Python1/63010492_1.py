print("*** Converting hh.mm.ss to seconds ***")
hh, mm, ss = input("Enter hh mm ss : ").split()
hh, mm, ss = int(hh), int(mm), int(ss)
sum = hh*3600 + mm*60 + ss
if(hh<10 and hh>=0):
    h = "0"+ str(hh)
else:
    h = str(hh)
if(mm<10 and mm>=0):
    m = "0"+ str(mm)
else:
    m = str(mm)
if(ss<10 and ss>=0):
    s = "0"+ str(ss)
else:
    s = str(ss)
if(0<=hh and 0<=mm<60 and 0<=ss<60 ):
    print(h+":"+m+":"+s+" =",f'{sum:,}',"seconds")
elif (hh<0):
    print("hh("+h+") is invalid!")
elif (0>mm or mm>=60):
    print("mm("+m+") is invalid!")
elif (0>ss or ss>=60):
    print("ss("+s+") is invalid!")


