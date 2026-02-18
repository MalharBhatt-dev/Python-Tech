
#! Find Second Largest Number

nums = [32,23,32,50,50,50,32,61]
largest = 0
s_largest = 0

for i in nums:
    if i > s_largest:
        if i > largest:
            s_largest = largest
            largest = i
        elif i == largest:
            continue
        else:
            s_largest = i


print(f'{s_largest} is the second largest in the {nums}.')