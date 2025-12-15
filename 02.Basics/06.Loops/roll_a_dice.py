import random

while True:
    inp = input("Press 'Enter' to roll the dice, or press 'q' to quite the game!!!\n")
    if inp == "q":
        print("Thanks for playing the game!!!")
        break
    elif inp == "":
        number = random.randint(1, 6)
        print(f"You got {number}")
    else:
        print("invalid input")
