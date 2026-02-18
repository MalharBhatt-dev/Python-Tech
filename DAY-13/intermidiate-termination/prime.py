
n=int(input("Enter Number: "))

for i in range(2,n):
    if n % i == 0:
        print(f"{n} Not a Prime Number.")
        break
else:
    print(f"{n} is a Prime Number")

