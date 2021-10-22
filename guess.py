import random

print("Number guessing game")

number = random.randint(1, 9)

chances = 5

print("Guess a number (TRY TO GUESS A NUMBER BETWEEN 1-9)")


while chances == 5:


    guess = int(input("Enter your guess:- "))


    if guess == number:

        print("Congratulation YOU WON!!!")
        break

    # Check if the user entered number is smaller than the generated number
    elif guess < number:
        print("Your guess was too low: Guess a number higher number", guess)

  
    else:
        print("Your guess was too high: Guess a number lower than", guess)

  
    chances = chances-1


# Check whether the user guessed the correct number
if chances < 1:
    print("YOU LOSE!!! The number is", number)