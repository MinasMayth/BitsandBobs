import random
while True:
    guesses = 0
    user_guess = 0
    num = random.randint (1, 9)
    print ("I'm thinking of a number between 1 and 9. How many guesses will you need to find it?")


    
    user_guess = input ("Type a number between 1 and 9, and I'll tell you if it's higher, lower, or exactly the number I'm thinking of! ")
    if int (user_guess) > int (num):
        print ("My number is lower!")
        guesses = guesses + 1
    elif int (user_guess) < int (num):
        print ("My number is higher!")
        guesses = guesses + 1
    elif int (user_guess) == int (num):
        print ("Well done, you guessed my number! It was " + str (num) + ".")
        guesses = guesses + 1
    else:
        print ("An error occured, please try again.")

            
    while int (user_guess) != int (num):
        user_guess = input ("Try again: ")
        if int (user_guess) > int (num):
            print ("My number is lower!")
            guesses = guesses + 1
        elif int (user_guess) < int (num):
            print ("My number is higher!")
            guesses = guesses + 1
        elif int (user_guess) == int (num):
            print ("Well done, you guessed my number! It was " + str (num) + ".")
            guesses = guesses + 1
        else:
            print ("An error occured, please try again.")

            

    print ("You guessed my number in " + str (guesses) + " guesses!")


    usr_input = input ("Type 'exit' to leave this program, otherwise press enter to continue: ")
    if usr_input == "exit":
        break
            
