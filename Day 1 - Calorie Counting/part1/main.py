def read_file(namefile):
    with open(namefile, 'r') as file:
        lines = file.read().splitlines()
    return lines

if __name__ == "__main__":
    day_input = read_file('input.txt') 
    
    max_calories = 0
    current_calories = 0
    # Treat Input
    for calorie in day_input:
        # Calculate Sum of Calories by Elf
        if calorie != '':
            current_calories += int(calorie)
            continue
        
        # Check if the current Elf have the maximum value
        if current_calories > max_calories:
            max_calories = current_calories
    print('How many total Calories is that Elf carrying?')
    print(max_calories)