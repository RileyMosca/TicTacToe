## NAUGHTS AND CROSSES
##AUTHOR: RILEY MOSCA

def create_empty_game():
    # Creating a new game
    rows, cols = 3, 3
    game = []
    for x in range(rows):
        column = []
        for y in range(cols):
            #Setting the current positions
            #On the  board to empty for default
            #Board type
            column.append("")
        game.append(column)
    return game

#Add player/ turn count mechanism later??
def display_game(game, count, player):
    print("Turn Count: " + str(count) + "")
    print("Current Turn: " + str(player) + "")
    for position in range(0, 3):
        print(game[position])
    print("\n")

def make_turn(game, x, y, player):
    #Checking the players piece to place in the game
    icon = ""
    if player == "naughts":
        icon = "O"
    elif player == "crosses":
        icon = "X"
    else:
        #Invalid player
        return

    #Must be a valid move
    #Position is not empty
    if game[x][y] != "":
        return

    #Position is opponents
    if icon == "O" and game[x][y] == "X":
        return
    if icon == "X" and game[x][y] == "O":
        return
    else:
        game[x][y] = icon
    return game

def check_win(game, player):
    icon = ""
    if player == "naughts":
        icon = "O"
    elif player == "crosses":
        icon = "X"
    else:
        return

    if game[0][0] == icon and game[0][1] == icon and game[0][2] == icon:
        return True
    elif game[1][0] == icon and game[1][1] == icon and game[2][2] == icon:
        return True
    elif game[2][0] == icon and game[2][1] == icon and game[2][2] == icon:
        return True
    elif game[0][0] == icon and game[1][1] == icon and game[2][2] == icon:
        return True
    elif game[2][0] == icon and game[1][1] == icon and game[0][2] == icon:
        return True
    elif game[0][0] == icon and game[1][0] == icon and game[2][0] == icon:
        return True
    elif game[0][1] == icon and game[1][1] == icon and game[2][1] == icon:
        return True
    elif game[0][2] == icon and game[1][2] == icon and game[2][2] == icon:
        return True
    else:
        return False

def handle_turns(game, count):
    #starting game, until a valid response is made
    while True:
        turn = input("Enter X for crosses or O for naughts:   ")
        if turn == "O" or turn == "X":
            break
        else:
            continue

    player = ""
    if turn == "X":
        player = "crosses"
    elif turn == "O":
        player = "naughts"

    #placing a piece on a valid position only
    x,y = 0,0
    while True:
        position = int(input("What position 0 - 8 would you like to place your piece?:   \n"))
        if position < 0 or position > 8:
            continue
        else:
            break
    if position == 0:
        x,y = 0,0
    if position == 1:
        x,y = 0,1
    if position == 2:
        x,y = 0,2
    if position == 3:
        x,y = 1,0
    if position == 4:
        x,y = 1,1
    if position == 5:
        x,y = 1,2
    if position == 6:
        x,y = 2, 0
    if position == 7:
        x,y = 2,1
    if position == 8:
        x,y = 2,2
    make_turn(game,x, y, player)
    display_game(game, count, player)

def check_tie(game):
    OCCUPIED_POS = 0
    for x in range(3):
        for y in range(3):
            if game[x][y] == "X" or game[x][y] == "O":
                #Game is in progress
                OCCUPIED_POS += 1
                continue
    if OCCUPIED_POS == 9:
        if check_win(game, "naughts") is False:
            return True
        elif check_win(game, "crosses") is False:
            return True
    return False

def play_tic_tac_toe():
    GAME = create_empty_game()
    TURN_COUNT = 1

    print("Welcome to tic tac toe, please follow the\n"
                    "instructions to get started, for this game\n"
                    "we will have two players, and the first to\n"
                    "get three \"X\" or \"O\" in a row wins!"
                    "\n\n\n")

    while check_win(GAME, "naughts") is False and check_win(GAME, "crosses") is False:
        handle_turns(GAME, TURN_COUNT)
        TURN_COUNT += 1
        if check_tie(GAME) is True:
            print("\nThis game is tied!")
            break

    if check_win(GAME, "naughts") is True:
        print("\nNaughts won!")
    elif check_win(GAME, "crosses") is True:
        print("\nCrosses won!")

#MAIN FUNCTION
def main():
    play_tic_tac_toe()

if __name__ == "__main__":
    main()