class MyInt:
    def __init__(self, value):
        self.value = value

    def isPrime(self):
        if self.value <= 1:
            return f'{self.value} isPrime : False'
        if self.value == 2:
            return f'{self.value} isPrime : True'

        for e in range(2, (self.value//2) + 1):
            if self.value % e == 0:
                return f'{self.value} isPrime : False'
        return f'{self.value} isPrime : True'

    def showPrime(self):
        if self.value <= 1:
            return "!!!A prime number is a natural number greater than 1"

        def check_prime(v):
            if self.value == 2:
                return True
            if self.value == 1:
                return False
            for e in range(2, 1+v//2):
                if v % e == 0:
                    return False
            return True
        out = ''
        for i in range(2, 1+self.value):
            if check_prime(i):
                out += str(i)+" "
        return out

    def __sub__(self, obj):
        return self.value - (obj.value // 2)


def anwser(inp1, inp2):
    a = MyInt(inp1)
    b = MyInt(inp2)
    print(a.isPrime())
    print(b.isPrime())
    print(f'Prime number between 2 and {a.value} : ' + a.showPrime())
    print(f'Prime number between 2 and {b.value} : ' + b.showPrime())
    print(f"{a.value} - {b.value} = {a-b}")


print(" *** class MyInt ***")
inp = list(map(int, input("Enter 2 number : ").split()))
anwser(inp[0], inp[1])