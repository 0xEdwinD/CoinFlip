import random

print("type flip to flip coin")

while True:
    start = input()
    if start.lower() != "flip":
        print("invalid entry")
    else:
        if start.lower() == "flip":
            a = random.randint(1, 2)
            if a == 1:
                print("Heads")
            elif a == 2:
                print("Tails")
