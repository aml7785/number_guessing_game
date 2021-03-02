import random

def number_guessing():
    num = random.randint(1,100)
    score = 100
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100 (Earn a maximum score of 100): "))
        except:
            guess = int(input("Guess a number between 1 and 100 (Earn a maximum score of 100): "))
        if guess == num:
            print("Your score is " + str(score))
            print("You guessed the number")
            break
        else:
            score -= 2
            if num % 2 == 0:
                print("The number is even.")
            else:
                print("The number is odd.")
            if guess > num:
                print("Try a smaller number")
            else:
                print("Try a larger number")
            continue