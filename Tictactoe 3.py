def tictactoe():

    print ("Welcome to Tic-Tac-Toe!")
    #Starting Board
    game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

    #Creating Graphics
    line = (((" ---") * 3) + ("\n") + (("|   ")* 3) + ("|") + ("\n"))
    board = (line * 3) + ((" ---") * 3)
    
    print (board)

    while True:
        Valid_input = False

        #Player 1 input
        print ("It's Player 1's turn! Please input a coordinate to place your X in using the format 'row,column'.")
        print ("(i.e. '1,2' places your X in the first row, second column.")
        Player_1 = input()
        while Valid_input is not True:
        
            Player1_list = Player_1.split(",")
            Player1_list = list(map(int, Player1_list))

            #Assigning Player 1 input to position in game
            player1_row = (Player1_list [0] - 1)
            player1_column = (Player1_list [1] - 1)

            #Checking if the position is already occupied
            if game [player1_row] [player1_column] != 0:
                print ("This spot has already been taken! Please try another.")
                Player_1 = input()
            else:
                Valid_input = True

        #Updating game
        game [player1_row] [player1_column] = ("X")

        #Updating Graphics
        board_list = list(board)
        
        if game [0][0] == ("X"):
            board_list [15] = ("X")
        if game [0][1] == ("X"):
            board_list [19] = ("X")
        if game [0][2] == ("X"):
            board_list [23] = ("X")
        if game [1][0] == ("X"):
            board_list [42] = ("X")
        if game [1][1] == ("X"):
            board_list [46] = ("X")
        if game [1][2] == ("X"):
            board_list [50] = ("X")
        if game [2][0] == ("X"):
            board_list [69] = ("X")
        if game [2][1] == ("X"):
            board_list [73] = ("X")
        if game [2][2] == ("X"):
            board_list [77] = ("X")
            
        board= "".join(board_list)

        #Printing board and checking to see if the board is full
        counter = 0
        for element in game:
            for element_2 in element:
                if element_2 == 0:
                    counter = counter + 1
        print (board)
        
        #Horizontal wins
        if game [0][0] == game [0][1] and game [0][0] == game [0][2] and game [0][0] != 0:
            return ("Player " + str (game [0][0]) + " has won.")
        elif game [1][0] == game [1][1] and game [1][0] == game [1][2] and game [1][0] != 0:
            return ("Player " + str(game [1][0]) + " has won.")
        elif game [2][0] == game [2][1] and game [2][0] == game [2][2] and game [2][0] != 0:
            return ("Player " + str(game [2][0]) + " has won.")

        #Vertical Wins
        elif game [0][0] == game [1][0] and game [0][0] == game [2][0] and game [0][0] != 0:
           return ("Player " + str (game [0][0]) + " has won.")
        elif game [0][1] == game [1][1] and game [0][1] == game [2][1] and game [0][1] != 0:
            return ("Player " + str (game [0][1]) + " has won.")
        elif game [0][2] == game [1][2] and game [0][2] == game [2][2] and game [0][2] != 0:
            return ("Player " + str (game [0] [2]) + " has won.")

        #Diagonal Wins
        elif game [0][0] == game [1][1] and game [0][0] == game [2][2] and game [0][0] != 0:
            return ("Player " + str (game [0][0]) + " has won.")
        elif game [0][2] == game [1][1] and game [0][2] == game [2][0] and game [0][2] != 0:
            return ("Player " + str (game [0][0]) + " has won.")
        elif counter == 0:
            return ("The board is full. Game Over!")


        #Resetting the valid input variable
        Valid_input = False
    
        #Player 2 input
        print ("It's Player 2's turn! Please input a coordinate to place your O in using the format 'row,column'.")
        print ("(i.e. '1,2' places your X in the first row, second column.")
        Player_2 = input()

        while Valid_input is not True:

            Player2_list = Player_2.split(",")
            Player2_list = list(map(int, Player2_list))

           #Assigning Player 2 input to position in game
            player2_row = (Player2_list [0] - 1)
            player2_column = (Player2_list [1] - 1)

            #Checking if the position is already occupied
            if game [player2_row] [player2_column] != 0:
                print ("This spot has already been taken! Please try another.")
                Player_2 = input()
            else:
                Valid_input = True

        #Updating game
        game [player2_row] [player2_column] = ("O")

        #Updating Graphics
        board_list = list(board)
        
        if game [0][0] == ("O"):
            board_list [15] = ("O")
        if game [0][1] == ("O"):
            board_list [19] = ("O")
        if game [0][2] == ("O"):
            board_list [23] = ("O")
        if game [1][0] == ("O"):
            board_list [42] = ("O")
        if game [1][1] == ("O"):
            board_list [46] = ("O")
        if game [1][2] == ("O"):
            board_list [50] = ("O")
        if game [2][0] == ("O"):
            board_list [69] = ("O")
        if game [2][1] == ("O"):
            board_list [73] = ("O")
        if game [2][2] == ("O"):
            board_list [77] = ("O")
            
        board= "".join(board_list)


        #Printing board and checking to see if the board is full
        counter = 0
        for element in game:
            for element_2 in element:
                if element_2 == 0:
                    counter = counter + 1
        print (board)
                    
       #Horizontal wins
        if game [0][0] == game [0][1] and game [0][0] == game [0][2] and game [0][0] != 0:
            return ("Player " + str (game [0][0]) + " has won.")
        elif game [1][0] == game [1][1] and game [1][0] == game [1][2] and game [1][0] != 0:
            return ("Player " + str(game [1][0]) + " has won.")
        elif game [2][0] == game [2][1] and game [2][0] == game [2][2] and game [2][0] != 0:
            return ("Player " + str(game [2][0]) + " has won.")

        #Vertical Wins
        elif game [0][0] == game [1][0] and game [0][0] == game [2][0] and game [0][0] != 0:
           return ("Player " + str (game [0][0]) + " has won.")
        elif game [0][1] == game [1][1] and game [0][1] == game [2][1] and game [0][1] != 0:
            return ("Player " + str (game [0][1]) + " has won.")
        elif game [0][2] == game [1][2] and game [0][2] == game [2][2] and game [0][2] != 0:
            return ("Player " + str (game [0] [2]) + " has won.")

        #Diagonal Wins
        elif game [0][0] == game [1][1] and game [0][0] == game [2][2] and game [0][0] != 0:
            return ("Player " + str (game [0][0]) + " has won.")
        elif game [0][2] == game [1][1] and game [0][2] == game [2][0] and game [0][2] != 0:
            return ("Player " + str (game [0][0]) + " has won.")
        elif counter == 0:
            return ("Game Over!")

                    
#Main Code
if __name__ == "__main__":
    while True:
        print (tictactoe())
        answer = input("Play again? (N to quit)").upper()
        if answer == "N":
            break
