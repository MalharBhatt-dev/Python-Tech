
#! WAP to extract vowels from the given List only if len of the string is ODD.

l = [12,3.4,True,3+5j,'Hii','Hello','Even']
out=[]
for i in l:
    if type(i) == str:
        if len(i) % 2 != 0:
            for j in i:
                if j in 'AEIOUaeiou':
                    out.append(j)
        

print(out)
            

