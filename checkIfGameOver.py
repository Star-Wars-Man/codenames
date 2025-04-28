def checkIfGameOver(color_board, word_board, chosen_board):
    black_row = 0
    for row in color_board:
        if "black" in row:
            black_colonm = row.index("black")
        else:
            black_row += 1
    