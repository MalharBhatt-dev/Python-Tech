
#h wap to reverse the string using for loop:

s = input("Enter the string:")
rev = ""

#! Method 1:(not recommended)
for i in range(len(s) - 1, -1, -1):
    rev += s[i]
print("Reversed string is:", rev)
#? OR
for i in range(0,len(s)):
    rev += s[len(s)-1 - i]
print("Reversed string is:", rev)

#! Method 2:
reve = ""
st = input("Enter the string:")
for i in st[::-1]:
    reve += i
print("Reversed string is:", reve)

#! Method 3:
rever=""
str = input("Enter the string:")
for i in str:
    rever = i + rever
print("Reversed string is:", rever)

