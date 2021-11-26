def bubble(arr,n,m):
    if n == len(arr)-1:
        n = 0
        m += 1 
    if m == len(arr): return
    if arr[n] > arr[m]:
        arr[n],arr[m] = arr[m],arr[n]
    bubble(arr,n+1,m)
    return arr

inp = [int(i) for i in input("Enter Input : ").split()]
print(bubble(inp,0,0))
