
#! WAP to extract only prime numbers from the given list

s = [12,67,89,45,3,13,17,20]
out = []

for i in s: #12
    div = 1 
    for j in range(2,i):
        if i % j == 0:
            div = div + 1
    if div == 1:
        out.append(i)

print(f"Prime Numbers: {out}")
