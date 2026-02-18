
#h WAP to print the numbers between 20 and 10 using range function

i = list( range(20, 9, -1))
print(i)\

#h wap to print numbers between -10 and 20 using range function
i = list(range(-10, 21, 1))
print(i)

#h wap to print upto 20 using range function
i = list(range(21))
print(i)

#h having very large number using range function
# for i in range(0, 10**18):
#     print(i)


#h wap to print the even numbers upto n:

#?Without using IF statement :
n = int(input("Enter the value of n:"))
for i in range(2, n+1, 2):
    print(f"Even numbers are:{i}")
#? Using IF statement :
n = int(input("Enter the value of n:"))
for i in range(1, n+1):
    if i % 2 == 0:  
        print(f"Even numbers are:{i}")

