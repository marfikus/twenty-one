
import random

while True:
    try:
        n = int(input(":"))
    except ValueError:
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