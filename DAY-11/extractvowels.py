
#! WAP to extract only vowels from the string data in the given list

a = [12,3.4,'Holiday',True,'apple',8+9j]

out=[]

for i in a:
    if type(i) == str:
        for j in i:
            if j in 'AEIOUaeiou':
                out.append(j)

print(out)
