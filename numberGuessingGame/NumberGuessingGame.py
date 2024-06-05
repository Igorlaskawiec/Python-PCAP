import random
def NumberGuessingGame():
    secretNumber = random.randint(1,99)
    print("Guess a number between 1 and 99")
    attemps = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attemps +=1

            if guess<1 or guess>99:
                print("Please guess number between 1 and 99")
            elif guess < secretNumber:
                print("Too low!")
            elif guess>secretNumber:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number!")
                break
        
        except ValueError:
            print("Invalid input")


NumberGuessingGame()