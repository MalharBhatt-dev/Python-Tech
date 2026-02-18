
#! WAP to convert Binary to Integer

n = int(input("Enter Binary Number: "))
strnum = str(n)
out = 0
pow = len(strnum) - 1

for i in strnum:
    out = out + (2**(pow))*int(i) 
    pow = pow - 1

print(out)
 