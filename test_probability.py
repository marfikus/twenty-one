
import random

while True:
    input_string = input("Enter number (from 0 to 19) or 'q' for quit: ")
    if input_string == "q":
        break
    try:
        n = int(input_string)
    except ValueError:
        print("incorrect input")
        continue

    if n < 0 or n > 19:
        print("incorrect input")
        continue

    if n <= 10:
        probability = [1, 1, 1, 1]
    elif 10 < n <= 13:
        probability = [1, 1, 1, 0]
    elif 13 < n <= 16:
        probability = [1, 1, 0, 0]
    elif 16 < n <= 19:
        probability = [1, 0, 0, 0]

    print(probability)
    pr = random.choice(probability)
    print(pr)
    if pr:
        print("yes")
    else: 
        print("no")