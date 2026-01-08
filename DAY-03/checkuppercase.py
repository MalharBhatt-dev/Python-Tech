n = input("Enter the Character: ")

if ord(n) >= 65 and ord(n) <= 90:
    print(ord(n))
    print(f"{n} is an UPPERCASE Character")

if n >= "A" and n <= "Z":
    print(f"{n} is an UPPERCASE Character")

if n.isupper():
    print('UPPERCASE')
