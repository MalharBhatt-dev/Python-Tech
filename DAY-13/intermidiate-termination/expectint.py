
#! WAP to print values except integer data type from the list

l = [1,'Hello','Python',5,6,7,8.99,[1,2,3]]
out=[]

for i in l:
    if type(i) == int:
        continue
    out.append(i)
print(out)
    
