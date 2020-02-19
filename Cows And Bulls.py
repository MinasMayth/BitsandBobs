import random


def cows_and_bulls():
    print ("Welcome to the Cows and Bulls game!")
    userinput = str ("void")
    number = str (random.randint(1000,9999))
    split_number = list (number)
    print ("I'm thinking of a 4 digit number, try and guess!")

    while userinput != number:
        cows = 0
        bulls = 0
        userinput = str (input ())
        split_input = list (userinput)
        
        if split_input [1] == split_number [1]:
            cows = cows + 1
        elif split_input [1] == split_number [0] or split_input [1] == split_number [2] or split_input [1] == split_number [3]:
            bulls = bulls + 1

        if split_input [2] == split_number [2]:
            cows = cows + 1
        elif split_input [2] == split_number [1] or split_input [2] == split_number [0] or split_input [2] == split_number [3]:
            bulls = bulls + 1

        if split_input [3] == split_number [3]:
            cows = cows + 1
        elif split_input [3] == split_number [1] or split_input [3] == split_number [2] or split_input [3] == split_number [0]:
            bulls = bulls + 1

        if split_input [0] == split_number [0]:
            cows = cows + 1
        elif split_input [0] == split_number [1] or split_input [0] == split_number [2] or split_input [0] == split_number [3]:
            bulls = bulls + 1

        cows = str(cows)
        bulls = str(bulls)

        print (cows + " cows, " + bulls + " bulls.")

    return ("You guessed the number! It was " + number + ".")

if __name__=="__main__":
    print (cows_and_bulls())
