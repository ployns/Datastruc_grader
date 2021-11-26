def palindrome(text):
    lst = []
    listBan = ['?','“','”',';','’','!','.',' ' ]
    for i in text:
       if i not in listBan:
           lst.append(i.lower())          
    if len(lst) == 1: 
        return 
    elif len(lst) == 2 and lst[0] == lst[-1]:   
        return
    elif lst[0] == lst[-1]:
        return palindrome(lst[1:-1])  
    else:
        return False    
        
inp = input('Enter Input : ')

if palindrome(inp) is False:
    print(("\'{}\' is not palindrome").format(inp))

else:
    print(("\'{}\' is palindrome").format(inp))

