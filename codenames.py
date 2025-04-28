import json
import random
def main():
    boards = createBoards()
    color_board = boards[0]
    word_board = boards[1]
    chosen_board = boards[2]
    setPlayers()
    gameLoop(color_board, word_board, chosen_board)
    displayWinner()

def createBoards():
    with open("color_matrices.json", "r") as file:
        matrices = [json.loads(line) for line in file]
        
    chosen_matrix = random.choice(matrices)
    
    with open("words.txt", "r") as file:
        all_words = [line.strip() for line in file if line.strip()]
        
    selected_words = random.sample(all_words, 25)
    
    matrix = [selected_words[i*5:(i+1)*5] for i in range(5)]
    
    return [chosen_matrix, matrix]
    
def setPlayers():
    print("hi")

def checkIfGameOver(color_board, chosen_board, turn):
    # Check if the black tile was chosen
    for r in range(len(color_board)):
        for c in range(len(color_board[0])):
            if color_board[r][c] == "black" and chosen_board[r][c] == "y":
                if turn == "red":
                    return [True, "blue"]
                else:
                    return [True, "red"]
    
    # Check if all red or all blue words have been guessed
    red_left = False
    blue_left = False
    for r in range(len(color_board)):
        for c in range(len(color_board[0])):
            if color_board[r][c] == "red" and chosen_board[r][c] != "y":
                red_left = True
            if color_board[r][c] == "blue" and chosen_board[r][c] != "y":
                blue_left = True
    
    if not red_left:
        return [True, "red"]
    if not blue_left:
        return [True, "blue"]
    
    # Otherwise, game is not over
    return [False, turn]

def gameLoop(color_board, word_board, chosen_board):
    
    checkIfGameOver(color_board, chosen_board, turn)

def displayWinner():
    print("hi")