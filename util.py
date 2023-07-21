import random

def roll_random_ability_scores():
    ability_scores = {'str': 0, 'dex': 0, 'con': 0, 'wis': 0, 'int': 0, 'cha': 0}

    # For each player characters abilities  
    for ability in ability_scores:
        rolls = []
        # roll a six sided dice four times and save each value.
        for i in range(4):
            rolls.append(random.randint(1, 6))
        
        # sort the rolls into ascending order and drop the lowest value. 
        rolls.sort()
        rolls.pop(0)

        # Add the remaining rolls to get the final score and add that to the scores dictionary 
        finalScore = sum(rolls)
        ability_scores[ability] = finalScore

    return ability_scores

def roll(dice:str):
    split = dice.split('d')
    no_of_dice = int(split[0])
    no_of_faces = int(split[1])
    final_value = 0
    for roll in range(no_of_dice):
        value = random.randint(1, no_of_faces)
        final_value += value 
        
    return final_value

def remove_item_from_list(item_to_remove, list):
    if item_to_remove in list:
        list.remove(item_to_remove)
    return list

def sanitize(input):
    return input.lower().strip()