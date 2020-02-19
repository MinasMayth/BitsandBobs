import random
import time

def random_user_guess():
    time.sleep (2)
    won = False
    no_of_guesses = 0
    x = list(range(0, 101))
    print ("Think of a number between 0 and 100, and I'll try to guess it!")
    time.sleep(2)
    print ("Have you thought of one? Good! Let's start!")

    while won is not True:
        guess = random.randint(x[0],x[len(x)-1])
        time.sleep(2)
        answer = input ("""Well, my guess is """ + str (guess) + """! If my guess is too high, type 'too high',
if my guess is too low, type 'too low', and if my guess is right, type 'correct'!\n""")

        if answer == "too high":
            x = list(range(x[0],guess))
            no_of_guesses += 1
        elif answer == "too low":
            final_position = x[len(x)-1]
            x = list(range((guess + 1),final_position + 1))
            no_of_guesses += 1
        elif answer == "correct":
            print ("Yes! I got it!")
            no_of_guesses += 1
            won = True
        else:
            return ("Error")
    time.sleep (1)
    return ("Your number was " + str(guess) + ", and I guessed it in " + str (no_of_guesses) + " guesses.")

def binary_user_guess():
    i = 0
    # i is the lowest number in range of possible guess
    j = 100
    # j is the highest number in range of possible guesses
    m = 50
    # m is the middle number in range of possible guesses
    counter = 1
    # counter is the number of guesses take.
    print ("Please think of a number between 0 and 100.")
    condition = input("Is your guess " + str(m) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high)")
    while condition != "1":
        counter += 1
        if condition == "0":
            i = m + 1
        elif condition == "2":
            j = m - 1
        m = int ((i + j) / 2)
        condition = input("Is your guess " + str(m) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high) ")
    return ("It took" , counter , "times to guess your number")

if __name__ == "__main__":
    while True:
        method = input ("Binary or Random? ").lower()

        if method == "binary":
            print (binary_user_guess())
        elif method == "random":
            print (random_user_guess())
        else:
            print ("Not Available.")
