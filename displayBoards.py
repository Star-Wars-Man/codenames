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