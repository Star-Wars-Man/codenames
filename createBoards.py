def createBoards():
    import json
    import random
    
    with open("color_matrices.json", "r") as file:
        matrices = [json.loads(line) for line in file]
        
    chosen_matrix = random.choice(matrices)
    
    with open("words.txt", "r") as file:
        all_words = [line.strip() for line in file if line.strip()]
        
    selected_words = random.sample(all_words, 25)
    
    matrix = [selected_words[i*5:(i+1)*5] for i in range(5)]
    
    chosen_board = [["n","n","n","n","n"],["n","n","n","n","n"],["n","n","n","n","n"],["n","n","n","n","n"],["n","n","n","n","n"]]
    
    return [chosen_matrix, matrix, chosen_board]