name1 = input ("What is the first player's name? ")
name2 = input ("What is the second player's name? ")
while True:
    print ("Welcome to the Rock, Paper, Scissors game!")
    P1_input = input (str(name1 + ": Choose, R for Rock, P for Paper, or S for Scissors! "))
    P2_input = input (str(name2 + ": Choose, R for Rock, P for Paper, or S for Scissors! "))
    if P1_input == "R" and P2_input == "R":
                 print ("It's a tie!")
    elif P1_input == "R" and P2_input == "P":
                 print (name2 + " wins!")
    elif P1_input == "R" and P2_input == "S":
                 print (name1 + " wins!")
    elif P1_input == "P" and P2_input == "R":
                 print (name1 + " wins!")
    elif P1_input == "P" and P2_input == "P":
                 print ("It's a tie!")
    elif P1_input == "P" and P2_input == "S":
                 print (name2 + " wins!")
    elif P1_input == "S" and P2_input == "R":
                 print (name2 + " wins!")
    elif P1_input == "S" and P2_input == "P":
                 print (name1 + " wins!")
    elif P1_input == "S" and P2_input == "S":
                 print ("It's a tie!")
    else:
        print ("Something went wrong, please try again.")

    usrinput = input ("Type 'exit' to leave the program, otherwise simply press enter to play again with the same players.")
    if usrinput == ("exit"):
        break
    
