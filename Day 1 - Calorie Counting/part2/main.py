def read_file(namefile):
    with open(namefile, 'r') as file:
        lines = file.read().splitlines()
    return lines

def add_value_in_order(c_list, c_value):
    position = len(c_list)
    for i in range(len(c_list)):
        if c_value > c_list[i]:
            position = i
            break
    c_list.insert(position, c_value)

if __name__ == "__main__":
    day_input = read_file("input.txt")
 
    current_calories = 0
    max_calories = [0, 0, 0]
    # Treat Input    
    for calories in day_input:
        # Calculate Sum of Calories by Elf
        if calories != '':
            current_calories += int(calories)
            continue
        
        # Check if the current Elf have the maximum value 
        # Compare with last | max_calories is an ordered list
        if current_calories > max_calories[-1]:
            # Remove the last element as we need to add a new one
            max_calories.pop(-1)
                
            # Add value in the correct Position
            add_value_in_order(max_calories, current_calories)  
        # Reset Calorie counter for the next Elf                  
        current_calories = 0
   
    # Calculate the Sum of the three with the higher calories         
    sum_total = 0
    for calorie in max_calories:
        sum_total += calorie
    print('How many Calories are those Elves carrying in total?')     
    print(sum_total)
