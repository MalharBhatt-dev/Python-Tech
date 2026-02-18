
#! Check List is Sorted or Not
       
nums = [1,5,10,20,40]
flag = 0

for i in range(0,len(nums)-2):
    if nums[i] > nums[i+1]:
        flag = 1
        break

if flag == 1:
    print(f"{nums} is not sorted")
else:
    print(f"{nums} is sorted")