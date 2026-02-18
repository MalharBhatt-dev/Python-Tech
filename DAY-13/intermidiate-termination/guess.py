
import random as rd

luckyNum = rd.randint(1,10)

counter = 0
while True:
    num = int(input("Enter A Number: "))
    if num == luckyNum:
        print(f"Your Guess is correct {num}")
        print(f"counter: {counter}")
        break
    elif num > luckyNum:
        print(f"{num} is greater than guess number!!")
        counter += 1
    else:
        print(f"{num} is smaller than guess number!!")
        counter += 1