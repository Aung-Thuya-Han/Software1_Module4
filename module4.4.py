import random
computer_choice = random.randint(1, 10)
user_guess = int(input("Enter your guess: "))

while user_guess != computer_choice:
    if user_guess < computer_choice:
        print("Too low.")
        user_guess = int(input("Enter your guess: "))
    elif user_guess > computer_choice:
        print("Too high.")
        user_guess = int(input("Enter your guess: "))

print(f"Correct! The number is {computer_choice}.")
