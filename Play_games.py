import random
from tkinter import *

class Game:
    
    def gamers(self):
        self.bg = PhotoImage( file = "frpg.png")
        self.background_label=Label( self , image = self.bg )
        self.background_label.place( x = 0 , y = 0 , relwidth = 1, relheight = 1 )
        
        self.Games = StringVar()
        self.Games.set("Choose game" )
        self.drop_down_list = OptionMenu( self , self.Games , "Snake-Water-Gun" , "Tic-Tac-Toe" , "SOS GAME")
        self.drop_down_list.place( x = 400 , y = 150 , width = 200)
        
        self.prev = Button( self , text = "<<Prev" , font = ( "Georgia", 15) , fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = self.user_page).place( x = 25 , y = 50 )
        
        def games():
            try:
                if self.Games.get()== "Snake-Water-Gun":
                    self.list1 = ["SNAKE", "WATER", "GUN"]
                    self.player = input("Enter players name:")
                    i = 0
                    playerscore = 0
                    compscore = 0
                    rounds = int(input("Enter No of Rounds:"))
                    while i < rounds:
                        comp_chosen = random.choice(self.list1)
                        chosen = (input("Enter Snake Water or Gun:").upper())
                        if chosen == "SNAKE" and comp_chosen == "WATER":
                            print(f"{self.player} won round {i + 1} As computer chose {comp_chosen}")
                            i = i + 1
                            playerscore = self.playerscore + 1
                            print(f"{self.player}-{playerscore} \n Computer-{compscore}")
                        elif chosen == "SNAKE" and comp_chosen == "GUN":
                            print(f"Computer chosen {comp_chosen} and won round {i + 1}")
                            i = i + 1
                            compscore = compscore + 1
                            print(f"{self.player}-{playerscore} \n Computer-{compscore}")
                        elif chosen == "SNAKE" and comp_chosen == "SNAKE":
                            print(f"Computer chosen {comp_chosen} and round {i + 1} is drawn")
                            i = i + 1
                            print(f"{self.player}-{playerscore} \n Computer-{compscore}")
                        elif chosen == "WATER" and comp_chosen == "SNAKE":
                            print(f"Computer chosen {comp_chosen} and won round {i + 1}")
                            i = i + 1
                            compscore = compscore + 1
                            print(f"{self.player}-{playerscore} \n Computer-{compscore}")
                        elif chosen == "WATER" and comp_chosen == "WATER":
                            print(f"Computer chosen {comp_chosen} and round {i + 1} is drawn")
                            i = i + 1
                            print(f"{self.player}-{playerscore} \n Computer-{compscore}")
                        elif chosen == "WATER" and comp_chosen == "GUN":
                            print(f"{self.player} won round {i + 1} As computer chose {comp_chosen}")
                            i = i + 1
                            playerscore = playerscore + 1
                            print(f"{self.player}-{playerscore} \n Computer-{compscore}")
                        elif chosen == "GUN" and comp_chosen == "GUN":
                            print(f"Computer chosen {comp_chosen} and round {i + 1} is drawn")
                            i = i + 1
                            print(f"{self.player}-{playerscore} \n Computer-{compscore}")
                        elif chosen == "GUN" and comp_chosen == "SNAKE":
                            print(f"{self.player} won round {i + 1} As computer chose {comp_chosen}")
                            i = i + 1
                            playerscore = playerscore + 1
                            print(f"{self.player}-{playerscore} \n Computer-{compscore}")
                        elif chosen == "GUN" and comp_chosen == "WATER":
                            print(f"Computer chosen {comp_chosen} and won round {i + 1}")
                            i = i + 1
                            compscore = compscore + 1
                            print(f"{self.player}-{playerscore} \n Computer-{compscore}")
                        else:
                            print("Enter correct spelling and try again")
                    if playerscore > compscore:
                        print(f"{self.player} won the game with scores \n {self.player}-{playerscore} \n Computer-{compscore}")
                    elif compscore > playerscore:
                        print(f"computer won the game with scores \n {self.player}-{playerscore} \n Computer-{compscore}")
                    else:
                        print(f"The game is drawn with each scoring {playerscore}")
            except:
                print("You have done an error !!")
            try:
                if (self.Games.get()== "Tic-Tac-Toe"):
                    board = [[" ", "1", "2", "3"], ["1", "_", "_", "_"], ["2", "_", "_", "_"], ["3", "_", "_", "_"]]

                    def print_board(player_1_name, player_2_name):  # PRINTING THE BOARD
                        print()
                        for i in range(100):
                            print("-", end="")
                        print("")

                        # now printing the scoreboard
                        print(player_1_name, "→ X ")
                        print(player_2_name, "→ O ")
                        for i in range(100):
                            print("-", end="")
                        print("\n")

                        for i in range(4):
                            for j in range(4):
                                print("| ", end="")
                                print(board[i][j], end=" ")
                            print("|\n")

                    def score_check(choice, row_no, col_no):
                        if (row_no == 1):
                            if (col_no == 1):
                                if (board[row_no][col_no + 1] == choice and board[row_no][col_no + 2] == choice):
                                    return 1
                                elif (board[row_no + 1][col_no] == choice and board[row_no + 2][col_no] == choice):
                                    return 1
                                elif (board[row_no + 1][col_no + 1] == choice and board[row_no + 2][col_no + 2] == choice):
                                    return 1
                            elif (col_no == 2):
                                if (board[row_no][col_no + 1] == choice and board[row_no][col_no - 1] == choice):
                                    return 1
                                elif (board[row_no + 1][col_no] == choice and board[row_no + 2][col_no] == choice):
                                    return 1
                            elif (col_no == 3):
                                if (board[row_no][col_no - 1] == choice and board[row_no][col_no - 2] == choice):
                                    return 1
                                elif (board[row_no + 1][col_no] == choice and board[row_no + 2][col_no] == choice):
                                    return 1
                                elif (board[row_no - 1][col_no + 1] == choice and board[row_no - 2][col_no + 2] == choice):
                                    return 1
                        if (row_no == 2):
                            if (col_no == 1):
                                if (board[row_no][col_no + 1] == choice and board[row_no][col_no - 1] == choice):
                                    return 1
                                elif (board[row_no + 1][col_no] == choice and board[row_no - 1][col_no] == choice):
                                    return 1
                            elif (col_no == 2):
                                if (board[row_no + 1][col_no + 1] == choice and board[row_no - 1][col_no - 1] == choice):
                                    return 1
                                elif (board[row_no + 1][col_no - 1] == choice and board[row_no - 1][col_no + 1] == choice):
                                    return 1
                            elif (col_no == 3):
                                if (board[row_no][col_no - 1] == choice and board[row_no][col_no + 1] == choice):
                                    return 1
                                elif (board[row_no - 1][col_no] == choice and board[row_no + 1][col_no] == choice):
                                    return 1
                        if (row_no == 3):
                            if (col_no == 1):
                                if (board[row_no][col_no + 1] == choice and board[row_no][col_no + 2] == choice):
                                    return 1
                                elif (board[row_no - 1][col_no] == choice and board[row_no - 2][col_no] == choice):
                                    return 1
                                elif (board[row_no - 1][col_no + 1] == choice and board[row_no - 2][col_no + 2] == choice):
                                    return 1
                            elif (col_no == 2):
                                if (board[row_no][col_no - 1] == choice and board[row_no][col_no + 1] == choice):
                                    return 1
                                elif (board[row_no - 1][col_no] == choice and board[row_no - 2][col_no] == choice):
                                    return 1
                            elif (col_no == 3):
                                if (board[row_no][col_no - 1] == choice and board[row_no][col_no - 2] == choice):
                                    return 1
                                elif (board[row_no - 1][col_no] == choice and board[row_no - 2][col_no] == choice):
                                    return 1
                                elif (board[row_no - 1][col_no - 1] == choice and board[row_no - 2][col_no - 2] == choice):
                                    return 1
                        return 0

                    player_1_name = input("Enter the name of player 1 :- ")
                    player_2_name = input("Enter the name of player 2 :- ")
                    print_board(player_1_name, player_2_name)
                    for i in range(9):
                        if (i % 2 == 0):
                            print("\n", player_1_name, "This is you Turn !! \n\n")
                            row_no = (int)(input("ENTER ROW NUMBER :- "))
                            column_no = (int)(input("ENTER COLUMN NUMBER :- "))
                            board[row_no][column_no] = 'X'
                            print_board(player_1_name, player_2_name)
                            if (score_check('X', row_no, column_no) == 1):
                                print(player_1_name, "WINS")
                                break
                            else:
                                continue
                        else:
                            print("\n", player_2_name, "This is you Turn !! \n\n")
                            row_no = (int)(input("ENTER ROW NUMBER :- "))
                            column_no = (int)(input("ENTER COLUMN NUMBER :- "))
                            board[row_no][column_no] = 'O'
                            print_board(player_1_name, player_2_name)
                            if (score_check('O', row_no, column_no) == 1):
                                print(player_2_name, "WINS")
                                break
            except:
                print("You have done an error !!")
            try:
                if (self.Games.get()== "SOS GAME"):
                    N = (int)(input("Enter the value of N greater than 2 :- "))  # asking the size of the grid

                    board = [["_", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_", "_"],
                            ["_", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_", "_"],
                            ["_", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_", "_"],
                            ["_", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_", "_"]]

                    # initializing the score of both players with 0
                    player_1_score = 0
                    player_2_score = 0

                    # to win a game, the player have to make the required combination with his/her own chosen letter in between two 'S'

                    # defining a to print board with 'N' as its size

                    def print_board(N):  # PRINTING THE BOARD
                        print()
                        for i in range(100):
                            print("-", end="")
                        print("")

                        # now printing the scoreboard
                        print(player_1_name, "choice :", player_1_char, "\tSCORE OF", player_1_name, ":", player_1_score)
                        print(player_2_name, "choice :", player_2_char, "\tSCORE OF", player_2_name, ":", player_2_score)
                        for i in range(100):
                            print("-", end="")
                        print("\n")
                        for i in range(N + 1):
                            for j in range(N + 1):
                                print("| ", end="")
                                if (i == 0 and j == 0):
                                    print("X ", end="")
                                elif (i == 0):
                                    print(j, end=" ")
                                elif (j == 0):
                                    print(i, end=" ")
                                else:
                                    print(board[i][j], end=" ")
                            print("|\n")

                    # defining the score check function, to check all the possible combinations of choice patterns
                    def score_chk(choice):

                        # checking all the possibilities for the letter 'S'
                        if (choice == 'S'):
                            if (board[row_no + 1][column_no + 1] == player_1_char and board[row_no + 2][column_no + 2] == 'S'):
                                return 1
                            if (board[row_no + 1][column_no + 1] == player_2_char and board[row_no + 2][column_no + 2] == 'S'):
                                return 2
                            if (board[row_no - 1][column_no - 1] == player_1_char and board[row_no - 2][column_no - 2] == 'S'):
                                return 1
                            if (board[row_no - 1][column_no - 1] == player_2_char and board[row_no - 2][column_no - 2] == 'S'):
                                return 2
                            if (board[row_no - 1][column_no + 1] == player_1_char and board[row_no - 2][column_no + 2] == 'S'):
                                return 1
                            if (board[row_no - 1][column_no + 1] == player_2_char and board[row_no - 2][column_no + 2] == 'S'):
                                return 2
                            if (board[row_no + 1][column_no - 1] == player_1_char and board[row_no + 2][column_no - 2] == 'S'):
                                return 1
                            if (board[row_no + 1][column_no - 1] == player_2_char and board[row_no + 2][column_no - 2] == 'S'):
                                return 2
                            if (board[row_no][column_no - 1] == player_1_char and board[row_no][column_no - 2] == 'S'):
                                return 1
                            if (board[row_no][column_no - 1] == player_2_char and board[row_no][column_no - 2] == 'S'):
                                return 2
                            if (board[row_no][column_no + 1] == player_1_char and board[row_no][column_no + 2] == 'S'):
                                return 1
                            if (board[row_no][column_no + 1] == player_2_char and board[row_no][column_no + 2] == 'S'):
                                return 2
                            if (board[row_no - 1][column_no] == player_1_char and board[row_no - 2][column_no] == 'S'):
                                return 1
                            if (board[row_no - 1][column_no] == player_2_char and board[row_no - 2][column_no] == 'S'):
                                return 2
                            if (board[row_no + 1][column_no] == player_1_char and board[row_no + 2][column_no] == 'S'):
                                return 1
                            if (board[row_no + 1][column_no] == player_2_char and board[row_no + 2][column_no] == 'S'):
                                return 2
                        # checking all the possibilities for the letter of player_1 choice
                        elif (choice == player_1_char):
                            if (board[row_no][column_no + 1] == "S" and board[row_no][column_no - 1] == "S"):
                                return 1
                            if (board[row_no + 1][column_no] == "S" and board[row_no - 1][column_no] == "S"):
                                return 1
                            if (board[row_no + 1][column_no + 1] == "S" and board[row_no - 1][column_no - 1] == "S"):
                                return 1
                            if (board[row_no - 1][column_no + 1] == "S" and board[row_no + 1][column_no - 1] == "S"):
                                return 1
                        # checking all the possibilities for the player_2 choice
                        elif (choice == player_2_char):
                            if (board[row_no][column_no + 1] == "S" and board[row_no][column_no - 1] == "S"):
                                return 2
                            if (board[row_no + 1][column_no] == "S" and board[row_no - 1][column_no] == "S"):
                                return 2
                            if (board[row_no + 1][column_no + 1] == "S" and board[row_no - 1][column_no - 1] == "S"):
                                return 2
                            if (board[row_no - 1][column_no + 1] == "S" and board[row_no + 1][column_no - 1] == "S"):
                                return 2
                        else:
                            return 0

                            # Asking for the name of both the players

                    player_1_name = input("PLAYER 1 PLEASE ENTER YOUR NAME :- ")
                    player_2_name = input("PLAYER 2 PLEASE ENTER YOU NAME  :- ")

                    # Asking player_1 to enter his/her choice
                    print(player_1_name, "ENTER ONE CHARACTER :- ")
                    player_1_char = input()
                    player_1_char = player_1_char.upper()  # we are converting the user input to upper case for easy comparision thereafter

                    # Asking player_2 to enter his/her choice
                    print(player_2_name, "ENTER ONE CHARACTER :- ")
                    player_2_char = (input())
                    player_2_char = player_2_char.upper()
                    print_board(N)

                    # initializing the value of row number and column number with 0
                    row_no = 0
                    column_no = 0

                    # copying the opted choices of both the players
                    player_1_choice = player_1_char
                    player_2_choice = player_2_char

                    for i in range(N * N):
                        if (i % 2 == 0):
                            # asking player_1 to choose his/her move. Either press 'S' or his/her randomly chosen letter
                            print("Your move", player_1_name, ":-")
                            print("PRESS \" S \" OR \"", player_1_char, "\"")
                            player_1_choice = input()
                            player_1_choice = player_1_choice.upper()
                            # Asking the row and column number, to insert the chosen letter at that place
                            row_no = (int)(input("ENTER ROW NUMBER :- "))
                            column_no = (int)(input("ENTER COLUMN NUMBER :- "))
                            board[row_no][column_no] = player_1_choice
                            # Increasing the score of player_1, if he/she gets the required pattern and same follows for player_2
                            if (score_chk(player_1_choice) == 1):
                                player_1_score += 1
                            elif (score_chk(player_1_choice) == 2):
                                player_2_score += 1
                            print_board(N)
                        else:
                            # Asking player_2 to choose his/her move.Either press 'S' or his/her randomly chosen letter
                            print("Your move", player_2_name, ":-")
                            print("PRESS \" S \" OR \"", player_2_char, "\"")
                            player_2_choice = input()
                            player_2_choice = player_2_choice.upper()
                            # Asking the row and column number for player_2, to insert the chosen letter at that place
                            row_no = (int)(input("ENTER ROW NUMBER :- "))
                            column_no = (int)(input("ENTER COLUMN NUMBER :- "))
                            board[row_no][column_no] = player_2_choice
                            # Increasing the score of player_1, if he/she gets the required pattern and same follows for player_2
                            if (score_chk(player_2_choice) == 1):
                                player_1_score += 1
                            elif (score_chk(player_2_choice) == 2):
                                player_2_score += 1
                            print_board(N)

                    # Checking which player got more points and then declaring the player with more score as winner
                    if (player_1_score > player_2_score):
                        print(player_1_name, " WINS !!\n")
                    elif (player_1_score < player_2_score):
                        print(player_2_name, " WINS !!\n")
                    else:
                        print("THERE IS A TIE !!\n")
                else:
                    print("Select A Game !!")
            except:
                print("You have done an error !!")
                print("Play Again !")

        self.gamesbutton = Button(self , text = "SELECT" , command = games , anchor = 'center' , font = ("Georgia",22) ,  width = 8 , relief = SUNKEN , bg = "white" , fg = "black")
        self.gamesbutton.place(x = 400, y = 300)