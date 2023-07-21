from character import Character
from util import roll_random_ability_scores, sanitize
from db import races, draconic_ancestries

player = Character()

## STEP ONE: CHOOSING A RACE ## 
print('Amidst the vast expanse of fantasy, which race shall thee assume on this odyssey? Choose wisely, for destiny eagerly awaits your decision.')
# List the available races
for race in races:
    print(f'- {race.capitalize()}')

# loop until a valid choice of race has been made
choosing_race = True
while(choosing_race):

    # Get user's choice of race
    chosen_race = sanitize(input('Enter the name of your chosen race: '))

    # If the chosen race is an viable choice 
    if chosen_race in races:
        # Retrieve the Race object 
        chosen_race = races[chosen_race]
        choosing_race = False
    # If the chosen race is not valid loop back to the input 
    else: 
        print('Please select a race from the list of available races.')

# Switch statement handles ay unique cases when adding a race to a character
match chosen_race.name:
    case 'Dragonborn':
        print('Reveal your Draconic Ancestry. The power of your lineage awaits your answer. Available anceestries: ')
        # List all available draconic ancestries
        for ancestry in draconic_ancestries:
            print(f"- {ancestry}")

        # Loop until a valid ancestry has been chosen
        choosing_ancestry = True 
        while(choosing_ancestry):
            # Get user input
            chosen_ancestry = sanitize(input('Enter your choice: '))

            # If user input matches a draconic ancestry...
            if chosen_ancestry in draconic_ancestries.keys():
                # Retrieve the ancestry object
                chosen_ancestry = draconic_ancestries[chosen_ancestry]
                # Add resistances from the ancestry to the race object 
                chosen_race.add_resistances(chosen_ancestry.damage_resistance_type)

                print(f"A fine choice indeed. Your {chosen_ancestry.dragon_type.capitalize()} dragon lineage gives you resistance to {chosen_ancestry.damage_resistance_type} damage and a {chosen_ancestry.breath_weapon} {chosen_ancestry.damage_resistance_type} breath weapon.") 

                player.add_race(chosen_race)
                choosing_ancestry = False
            
            # If the chosen ancestry is not valid, loop back to user input
            else:
                print('You must select an ancestry from the list above')

    case 'Hill Dwarf':
        # trait. 'Dwarven Toughness': 'Your hit point maximum increases by 1, and it increases by 1 every time you gain a level'
        player.hit_points += player.level
        player.add_race(chosen_race)

    case _:
        player.add_race(chosen_race)

## STEP THREE: DETERMINE ABILITY SCORES ## 
# Deciding whether to input ability scores manually or have them rolled randomly
deciding = True
while deciding:
    # User input
    decision = sanitize(input('Do you want to manually enter your stats or have them rolled randomly? type manual or random: '))

    # Randomly roll scores 
    if decision == 'random':
        random_scores = roll_random_ability_scores()
        player.update_ability_scores(random_scores)
        deciding = False

    # Manually enter scores 
    elif decision == 'manual':

        print('Roll 4d6 and add the three highest together to obtain your ability scores.')
        manual_scores = {'str': 0, 'dex': 0, 'con': 0, 'wis': 0, 'int': 0, 'cha': 0}
        score_text = {
            'str': 'Enter thy strength, mighty warrior, and reveal the power within (strength): ', 
            'dex': 'Unveil the nimbleness that courses through thy veins, agile soul (dexterity): ', 
            'con': 'Embrace the endurance that fortifies thy spirit, resilient hero (constitution): ', 
            'wis': 'Tap into the wellspring of wisdom, wise sage, and share its depth (wisdom): ', 
            'int': 'Let the flame of intelligence burn bright, cunning mind, as you disclose its brilliance (intelligence): ', 
            'cha': 'Awaken the aura of charisma that captivates hearts, enchanting soul (charisma): '
        }

        # Loop through ability scores and check that each input is a valid integer between 3 and 18
        for ability in manual_scores:
            while manual_scores[ability] == 0:
                try: 
                    current_score = int(input(score_text[ability]))
                except ValueError: 
                    print('\nYou must enter a number\n')

                if current_score in range(3, 19):
                    manual_scores[ability] = current_score
                else: 
                    print('Your score must be between 3 and 18')
            
        player.update_ability_scores(manual_scores)

        deciding = False
    
    # If neither option was selected, loop until a valid choice is made.
    else:
        decision = sanitize(input('Please enter "manual" or "random": '))

print('\n')
print(player) # Debugging and testing. 