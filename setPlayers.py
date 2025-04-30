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