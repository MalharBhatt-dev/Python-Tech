
#h wap to check is a given character is a vowel or consonant..->

c = input("Enter the character:")
if 'A'<=c<='Z' or 'a'<=c<='z':
    if c in 'AEIOUaeiou':
        print(f"{c} is a Vowel.")
    else:
        print(f"{c} is a Consonant.")
else:
    print("Invalid Input...")

