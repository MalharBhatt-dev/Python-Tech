
#h WAP to find the sum of digits of a number::eg: input - 145 output = 1+4+5 = 10

a = int(input("Enter the number:"))
sum =  0
i=0
while i < len(str(a)):
    sum += int(str(a)[i])
    i += 1
print("Sum of digits:", sum)

