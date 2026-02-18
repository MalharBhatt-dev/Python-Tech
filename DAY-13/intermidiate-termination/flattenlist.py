
#! WAP to flatten a Nested List

l = [1,2,3,4,5,[23,24,25],[11,22]]
out = []

for i in l:
    if type(i) == list:
        for j in i:
            out.append(j)
    else:
        out.append(i)

print(f"{out} is a Flatten List of {l}")