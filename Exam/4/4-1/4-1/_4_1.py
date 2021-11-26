def search(n, l, arr, x):
    mid = (n + l) // 2
    if n > l:
        return 'Not found'
    if x == arr[mid]:
        return 'Found'
    elif x < arr[mid]:
        return search(n, mid-1, arr, x)
    elif x > arr[mid]:
        return search(mid+1, l, arr, x)

inp = input('Enter Input : ').split('/')
arr, a = list(map(int, inp[0].split())), int(inp[1])
print(search(0, len(arr) - 1, sorted(arr), a))