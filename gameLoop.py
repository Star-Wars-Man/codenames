import os

def gameLoop(color_board, word_board, chosen_board, firstPlayer):
    print(firstPlayer + " Team is going first, guessers leave")
    displayBoards(color_board, word_board, 'c')
    clue = input('enter one word clue')
    numOfClues = input('number applying to it: ')
    os.system('clear')
    print(firstPlayer + ' Guessers turn')
    print("your clue is " + clue)
    print("you have " + numOfClues + " guesses")
    displayBoards(color_board, word_board, 'g')
    for i in range(numOfClues):
        clueR = input('enter row of guess (starts at 0 ends at 4)')
        clueC = input('enter column of guess (starts at 0 ends at 4)')
        if color_board[clueR][clueC] == firstPlayer:
            chosen_board[clueR][clueC] = 'y'
        else:
            print('Wrong guess')
            break
    over = checkIfGameOver(color_board, chosen_board, firstPlayer)
    next_team = ""
    if firstPlayer == "red":
        next_team == "blue"
    else:
        next_team == "red"
    if over[0]:
        return over[1]
    else:
        
        gameLoop(color_board, word_board, chosen_board, next_team)