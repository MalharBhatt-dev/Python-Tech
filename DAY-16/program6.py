
#! 6. WAP TO REMOVE DUPLICATES FROM THE LIST AND ADD THE NON DUPLICATE VALUES TO THE 
#! SECOND LIST.

input = [1,3,1,5,2,1,4,5,6,6,2,7]
out = []

for i in input:
    count = 0
    for j in input:
        if i == j:
            count += 1
        if count > 1:
            break
    if count == 1:
        out.append(i)

print(out)