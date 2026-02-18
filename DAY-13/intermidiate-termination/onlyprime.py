
#! WAP to print only prime numbers from the given list

l = [12,56,3,7,67,45,55,90]
out=[]
for i in l:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        out.append(i)

print(out)