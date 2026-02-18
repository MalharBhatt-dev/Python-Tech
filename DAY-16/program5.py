
#! 5. WAP TO GROUP THE NUMBERS BY THEIR REMAINDERS WHEN DIVIDED BY 3. 
#!    DATA = [1,2,3,4,5,6,7,8,9]
#!    OUTPUT = {0: [3,6,9], 1:[1,4,7], 2:[2,5,8]}

data = [1,2,3,4,5,6,7,8,9]
out = {}

for i in data:
    rem = i % 3
    if rem not in out:
        out[rem] = [i]
    else:
        out[rem].append(i)

print(out)
