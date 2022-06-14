import random

def easy(num):
    attempts=10
    while attempts>0:
        guess=int(input("You have "+str(attempts)+ " attempts remaining to guess the number. \nMake a guess: "))
        if guess==num:
            print("You've guessed the correct number. You Win!")
            return
        elif guess>num:
            print("Too high! Guess again: ")
            attempts-=1
        elif guess<num:
            print("Too low! Guess again: ")
            attempts-=1
    print("You're out of guesses. You lose!")

def hard(num):
    attempts = 5
    while attempts > 0:
        guess = int(input("You have " + str(attempts) + " attempts remaining to guess the number. \nMake a guess: "))
        if guess == num:
            print("You've guessed the correct number. You Win!")
            return
        elif guess > num:
            print("Too high! Guess again: ")
            attempts -= 1
        elif guess < num:
            print("Too low! Guess again: ")
            attempts -= 1
    print("You're out of guesses. You lose!")

num=random.randrange(1,100)
print("Welcome to the guessing game! \nI'm thinking of a number between 1 to 100")
while 1:
    level = input("Choose a difficulty: type 'easy' or 'hard': ")
    if level=='easy':
        easy(num)
    elif level=='hard':
        hard(num)
    else:
        print("Invalid Input! try again.")

