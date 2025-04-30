def gameLoop(color_board, word_board, chosen_board):

playerAction = {
    'Player 1': 'give clue',
    'Player 3': 'take guesses',
    'Player 2': 'give clue',
    'Player 4': 'take guesses'
}


def gameLoop(color_board, word_board, chosen_board, firstPlayer):
    print(firstPlayer + " Team is going first, guessers leave")
    displayBoards(color_board, word_board, 'c')
    clue = input('enter one word clue')
    numOfClues = input('number applying to it: ')
    print(firstPlayer + ' Guessers turn')
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

    
        
    print(displayBoards)
    input()

        

    
    checkIfGameOver(color_board, chosen_board, turn)


checkIfGameOver(color_board, chosen_board, turn)