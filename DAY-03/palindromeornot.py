
#! WAP To check if the given string is Palindrome or Not

string = input("Enter String: ")

if string == string[::-1]:
    print(f"{string} is Palindrome")
    print(string)
    print(string[::-1])

else:
    print(f"{string} is not Palindrome")
    print(string)
    print(string[::-1])
