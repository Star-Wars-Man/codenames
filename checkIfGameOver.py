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