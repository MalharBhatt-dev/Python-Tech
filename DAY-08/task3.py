
#h wap to extract all the lowercase characters from string only if ascii value is even

str = input ("Enter the string :")
lt = ""
for i in str :
    if ('a'<=i<='z'):
        if(ord(i)%2==0):
            lt+=i
print(lt)
