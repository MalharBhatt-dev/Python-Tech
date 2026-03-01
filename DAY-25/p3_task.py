#wap to print fibonnaci series upto n.

n = int(input("Enter the number :"))
a  = 0
b = 1
print(a,end=" ")
print(b,end=" ")
i = 0 
while i <= n:
    out = a +b
    print(out , end=' ')
    a = b 
    b = out
    i += 1 
