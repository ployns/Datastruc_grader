print("*** Fun with countdown ***")
ls = list(map(int,input('Enter List : ').strip().split()))
Answer = []
lsSub = []
for i in range(len(ls)):
    if (i+1) != len(ls):
        if (ls[i] - ls[i+1]) == 1:
            if len(lsSub) == 0:
                lsSub.append(ls[i])
            lsSub.append(ls[i+1])
            if ls[i] == 2:
                Answer.append(lsSub)
                lsSub = []
        else:
            if ls[i] == 1 and ls[i-1] != 2:
                lsSub.append(ls[i])
                Answer.append(lsSub)
                lsSub = []
            elif ls[i+1] == 1 and len(lsSub) == 0:
                lsSub.append(ls[i])
                Answer.append(lsSub)
                lsSub = []

Countdown = [len(Answer),Answer]
print(Countdown)