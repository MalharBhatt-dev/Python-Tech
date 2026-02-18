
#! WAP to group numbers by their remainder when divided by 3
l = [1,2,3,4,5,6,7,8,9]
d={}

for i in l:
    rem = i % 3
    if rem not in d:
        d[rem] = [i]
    else:
        d[rem].append(i)

print(f"Desired Output: {d}")