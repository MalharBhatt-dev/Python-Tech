
#h wap to replace space by * in the string

str = input("Enter the string with spaces :")

for i in range(0,len(str)) :
    if (str[i] ==' '):
        str[i] = '*'
print(str)