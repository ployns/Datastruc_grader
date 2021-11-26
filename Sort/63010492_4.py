def selection(n):
    for i in range(len(n)):
        min = i
        for j in range(i+1, len(n)):
            if n[min] > n[j]:
                min = j
        n[i], n[min] = n[min], n[i]
    return n



l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+ Ans)
else:
    l=list(map(int, l))
    lst = []
    for i in l:
        lst.append(i)
        lst_sorted = selection(lst.copy())
        if len(lst_sorted) <= 1:
            print(f"list = {lst} : median = {lst_sorted[0]:.1f}")
        else:
            print(f"list = {lst} : median = {lst_sorted[len(lst)//2] if len(lst)%2==1 else (lst_sorted[len(lst)//2-1]+lst_sorted[len(lst)//2])/2:.1f}")