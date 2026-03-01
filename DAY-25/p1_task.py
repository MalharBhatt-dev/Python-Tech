#wap to (in while)to print factorial of a given number..
n = int(input("Enter the number :"))
fact0 = 1
i = 1
while i <= n:
    fact0 *= i 
    i+=1
print(f"The factorial of the number {n} is : {fact0}")