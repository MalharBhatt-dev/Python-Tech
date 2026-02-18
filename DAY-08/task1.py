
#h Wap to print the characters present at old index from a string.

s = input("Enter the string :")
output = ""
for i in range(0,len(s)):
    if (i%2!=0):
        output += s[i]
print(output)    