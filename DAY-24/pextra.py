#wap to convert int into binary without using bin function.
integer_input = int(input("Enter an integer: "))
binary_output = "" 
if integer_input == 0:
    binary_output = "0"
while integer_input > 0:
    remainder = integer_input % 2
    binary_output = str(remainder) + binary_output
    integer_input //= 2
print("Binary representation:", binary_output)

#wap to convert binary into int.
binary_input = input("Enter a binary number: ")
integer_output = 0 
for index, digit in enumerate(reversed(binary_input)):
    if digit == '1':
        integer_output += 2 ** index
print("Integer representation:", integer_output)   
