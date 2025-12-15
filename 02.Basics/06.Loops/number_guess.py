secret_number = 25
chances = 10
num = 1

print(
    "Welcome to the number guessing game...\nYou have 10 chances to guess the number between 1 and 50"
)
while num <= 10:
    print(f"You have {chances} chances left!")
    user_guess = int(input("Guess the number between 1 and 50: "))
    if user_guess == secret_number:
        print("Congrats, Your guess was right!")
        break
    else:
        if user_guess > secret_number:
            higher_or_lower = "lower"
        else:
            higher_or_lower = "higher"
        print(f"Your guess is wrong! try {higher_or_lower} number")
    num += 1
    chances = chances - 1
print(f"You lost!! the secret number was {secret_number}")
