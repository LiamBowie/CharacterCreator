from character import Character
from util import roll_random_ability_scores, sanitize, clear
from db import races, draconic_ancestries, classes

player = Character()

## STEP ONE: CHOOSING A RACE ## 
clear()
print('Amidst the vast expanse of fantasy, which race shall thee assume on this odyssey? Choose wisely, for destiny eagerly awaits your decision.')
# List the available races
for race in races:
    print(f'- {race.capitalize()}')

# loop until a valid choice of race has been made
choosing_race = True
race_choice = ''
while(choosing_race):
    # Get user's choice of race
    race_choice = sanitize(input('Enter the name of your chosen race: '))
    # If the chosen race is an viable choice 
    if race_choice not in races:
        print('Please select a race from the list of available races.')
    else:
        choosing_race = False
 
# Retreive the full race object from the selection 
race_choice = races[race_choice]

# Switch statement handles ay unique cases when adding a race to a character
clear()
match race_choice.name:
    case 'Dragonborn':
        print('Reveal your Draconic Ancestry. The power of your lineage awaits your answer. Available anceestries: ')
        # List all available draconic ancestries
        for ancestry in draconic_ancestries:
            print(f"- {ancestry}")

        # Loop until a valid ancestry has been chosen
        choosing_ancestry = True 
        ancestry_choice = ''
        while(choosing_ancestry):
            # Get user input
            ancestry_choice = sanitize(input('Enter your choice: '))

            # If user input matches a draconic ancestry...
            if ancestry_choice not in draconic_ancestries.keys():
                print('You must select an ancestry from the list above')
            else:
                choosing_ancestry = False
            
            # Retrieve the ancestry object
            ancestry_choice = draconic_ancestries[ancestry_choice]
            # Add resistances from the ancestry to the race object 
            race_choice.add_resistances(ancestry_choice.damage_resistance_type)

            print(f"A fine choice indeed. Your {ancestry_choice.dragon_type.capitalize()} dragon lineage gives you resistance to {ancestry_choice.damage_resistance_type} damage and a {ancestry_choice.breath_weapon} {ancestry_choice.damage_resistance_type} breath weapon.") 

            player.add_race(race_choice)
            

    case 'Hill Dwarf':
        # trait. 'Dwarven Toughness': 'Your hit point maximum increases by 1, and it increases by 1 every time you gain a level'
        player.hit_points += player.level
        player.add_race(race_choice)

    case _:
        player.add_race(race_choice)

## STEP TWO: CHOOSE A CLASS ##
clear()
print('Descriptive text about choosing classes')
for c in classes:
    print(f'- {c.capitalize()}')

choosing_class = True
class_choice = ''
while choosing_class:
    class_choice = sanitize(input('Enter your class: '))
    if class_choice not in classes:
        print ('Select a class from the list above')
    else:
        choosing_class = False

chosen_class = classes[class_choice]

# Choosing skills 
clear()
print(f'Choose {chosen_class.no_of_skills} of the following skills: ')

for skill in chosen_class.available_skills:
    print(f'-{skill}')

skills = []
count = 0
while count < chosen_class.no_of_skills:
    chosen_skill = sanitize(input(f'Skill {count+1}: '))

    if chosen_skill not in chosen_class.available_skills:
        print('Select a skill from the list above')
    elif chosen_skill in player.skills:
        print(f'You are already proficient in {skill}')
    else:
        skills.append(chosen_skill)
        count += 1
    
# Choosing equipment
clear()
print('Would you like to choose your starting equipment or recieve starting gold?')
choosing_gold_or_equipment = True
gold_or_equipment = ''
while choosing_gold_or_equipment:
    gold_or_equipment = sanitize(input('Type gold or equipment: '))

    if gold_or_equipment == 'gold' or gold_or_equipment == 'equipment':
        choosing_gold_or_equipment = False

equipment = []
if gold_or_equipment == 'equipment':
    print('Choose one of the following: ')
    for choice in chosen_class.starting_equipment_choices:
        string = ['']
        for item in choice:
            string.append(f'-{item} ')
        print(''.join(string))
        equipment_choice = ''
        choosing_equipment = True
        while choosing_equipment:
            equipment_choice = sanitize(input('I choose: '))
            if equipment_choice not in choice:
                print('Choose an item from the list')
            else:
                choosing_equipment = False
        equipment.append(equipment_choice)
    
    equipment.extend(chosen_class.starting_equipment_given)

player.add_class(chosen_class, skills, equipment)

## STEP THREE: DETERMINE ABILITY SCORES ## 
# Deciding whether to input ability scores manually or have them rolled randomly
clear()
print('Do you want to manually enter your stats or have them rolled randomly?')
choosing_method = True
input_method = ''
while choosing_method:
    # User input
    input_method = sanitize(input('type manual or random: '))
    if input_method == 'random' or input_method == 'manual':
        choosing_method = False

# Randomly roll scores 
if input_method == 'random':
    random_scores = roll_random_ability_scores()
    player.update_ability_scores(random_scores)
    deciding = False

# Manually enter scores 
elif input_method == 'manual':
    clear()
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

## STEP FOUR: DESCRIBE YOUR CHARACTER ##
#Name
clear()
name = ''
choosing_name = True
while choosing_name:
    name = input('Enter a name for your character: ').strip()
    if name == '':
        print('You must enter a name')
        continue

    confirm_name = sanitize(input(f'Are you happy with "{name}"? Type "y" to confirm: '))
    if confirm_name == 'y':
        choosing_name = False

player.set_name(name)

# Age
clear()
print(race_choice.lifespan)
age:int
choosing_age = True
while choosing_age:
    try:
        age = int(input('How old is your adventurer?: '))
        choosing_age = False
    except ValueError:
        print('You must enter a number')

player.set_age(age)

# Gender
clear()
gender = ''
choosing_gender = True
while choosing_gender:
    gender = input('What is your character\'s gender (press enter to skip): ').strip()

    if not gender: break
     
    confirm_gender = sanitize(input(f'Are you happy with "{gender}"? Type "y" to confirm: '))
    if confirm_gender == 'y':
        choosing_gender = False

player.set_gender(gender)

clear()
print(player) # Debugging and testing. 