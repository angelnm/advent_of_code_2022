def read_file(namefile):
    with open(namefile, 'r') as file:
        lines = file.read().splitlines()
    return lines

def get_score_round(opponent, you):
    if opponent == you:
        return 3
    elif (opponent+1)%3==you:
        return 6
    return 0

def get_shape_from_strategy(opponent, strategy):
    if strategy == 'X':
        return (opponent+2)%3
    elif strategy == 'Y':
        return opponent
    return (opponent+1)%3

TEXT2NUM = {'A':0, 'B':1, 'C':2}
if __name__ == "__main__":
    day_input = read_file("input.txt")
        
    score = 0
    for c_round in day_input:
        opponent, strategy = c_round.split()
        
        opponent = TEXT2NUM[opponent]
        you = get_shape_from_strategy(opponent, strategy)
        
        # Sum the Shape you selected
        score += you+1
 
        # Sum the result of the round       
        score += get_score_round(opponent, you) 
        
    print("What would your total score be if everything goes exactly according to your strategy guide?")
    print(score)