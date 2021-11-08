#class translator:

#    def deciToRoman(self, num):
#        num_map = [(1000,'M'),(900,'CM'),(500,'D'),(400,'D'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]             
#        roman = ''
#        while num > 0 :
#            for i,r in num_map:
#                while num>= i :
#                    roman = roman + r
#                    num = num-i
#        return roman

#    def romanToDeci(self, s):

#        return s

#num = int(input("Enter number to translate : "))

#print(translator().deciToRoman(num))
#if(num>0):
#    print(translator().romanToDeci(num))

class translator:

    def deciToRoman(self, num):
        fi = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
        s = {1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
        t = {1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
        fo = {1: "M", 2: "MM", 3: "MMM"}

        collec = ""
        temp = 0
        nlist = []
        roman = ""
        leng = len(str(num))

        for x in range(0, leng):
            temp = num % 10
            num = (num - temp) / 10
            nlist.append(int(temp))

        for y in range(0, leng):
            if y == 0:
                if nlist[y] in fi:
                    nlist[y] = fi[nlist[y]]
            elif y == 1:
                if nlist[y] in s:
                    nlist[y] = s[nlist[y]]
            elif y == 2:
                if nlist[y] in t:
                    nlist[y] = t[nlist[y]]
            elif y == 3:
                if nlist[y] in fo:
                    nlist[y] = fo[nlist[y]]
        nlist.reverse()

        for z in range(0,leng):
            roman += nlist[z]

        return roman

    def romanToDeci(self, s):

        return s

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(num))