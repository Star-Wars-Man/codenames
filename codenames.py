import json
import random
def main():
    boards = createBoards()
    color_board = boards[0]
    word_board = boards[1]
    chosen_board = boards[2]
    firstPlayer = setPlayers(color_board)
    winner = gameLoop(color_board, word_board, chosen_board, firstPlayer)
    displayWinner(winner)

def createBoards():
    with open("color_matrices.json", "r") as file:
        matrices = [json.loads(line) for line in file]
        
    chosen_matrix = random.choice(matrices)
    
    with open("words.txt", "r") as file:
        all_words = [line.strip() for line in file if line.strip()]
        
    selected_words = random.sample(all_words, 25)
    
    matrix = [selected_words[i*5:(i+1)*5] for i in range(5)]
    
    return [chosen_matrix, matrix]
    
def setPlayers(color_board):
    print('Players 1 and 3 are Red Team, Players 2 and 4 are Blue Team')
    print('Players 1 and 2 are Clue Givers, Players 3 and 4 are Guessers')
    
    r_count = 0
    for row in color_board:
        for color in row:
            if color == "red":
                r_count += 1
    
    if r_count == 9:
        return "red"
    else:
        return "blue"

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
def displayBoards(color_board, word_board, player_type):
    for r in range(len(word_board)):
        for c in range(len(word_board[0])):
            word = word_board[r][c]
            if player_type == "c":
                color = color_board[r][c]
                print(f"{word} ({color})", end="\t")
            else:
                print(f"{word}", end="\t")
        print()

def gameLoop(color_board, word_board, chosen_board, firstPlayer):
    displayBoards(color_board, word_board, player_type)
    checkIfGameOver(color_board, chosen_board, turn)

def displayWinner(winner):
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    TROPHY = "🏆"
    CONFETTI = "🎉"
    WIDTH = 80
    LINE = "=" * WIDTH

    def center(text):
        return text.center(WIDTH)

    if winner == "red":
        print(f"\n{RED}{LINE}")
        print(center(f"{TROPHY}  RED TEAM WINS!  {TROPHY}"))
        print(center(f"{CONFETTI} Congrats Players 1 and 3! {CONFETTI}"))
        print(f"{LINE}{RESET}\n")
    elif winner == "blue":
        print(f"\n{BLUE}{LINE}")
        print(center(f"{TROPHY}  BLUE TEAM WINS!  {TROPHY}"))
        print(center(f"{CONFETTI} Congrats Players 2 and 4! {CONFETTI}"))
        print(f"{LINE}{RESET}\n")
    else:
        print(center("❗ Invalid winner specified."))