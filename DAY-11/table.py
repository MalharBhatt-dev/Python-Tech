
#! WAP to ptint Multiplication Table for a number

start = int(input("Enter Start Number for Table:"))
end = int(input("Enter End Number for Table:"))

for i in range(start,end+1):
    print(f"Table of {i} ")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print("-"*20)
