import random
from race import Race, DraconicAncestry
from character import Character

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

## Available races
# TODO: Player's must choose one tool proficiency from the given list in the dwarven races. Write relevant control flow. (include option for multiple choices?)
available_races = {
    'dragonborn' : Race('Dragonborn', {'str': 2, 'cha': 1}, 'medium', 30, ['common', 'draconic'], [], False, [], [], [], {'breath weapon': 'You can use your action to exhale destructive energy. Your draconic ancestry determines the size, shape, and damage type of the exhalation. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw, the type of which is determined by your draconic ancestry. The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level. After you use your breath weapon, you can\'t use it again until you complete a short or long rest.'}),
    'mountain dwarf' : Race('Mountain Dwarf', {'str': 2, 'con': 2}, 'medium', 25, ['common', 'dwarvish'], ['poison'], False, ['battleaxe', 'handaxe', 'lighthammer', 'warhammer'], ['light', 'medium'], ['smith\'s tools', 'brewer\'s supplies', 'mason\'s tools'], {'dwarven resilience': 'You have advantage against saving throws against poison', 'stonecunning': 'Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.'}),
    'hill dwarf': Race('Hill Dwarf', {'con': 2, 'wis': 1}, 'medium', 25, ['common, dwarvish'], ['poison'], True, ['battleaxe', 'handaxe', 'lighthammer', 'warhammer'], ['light', 'medium'], ['smith\'s tools', 'brewer\'s supplies', 'mason\'s tools'], {'dwarven resilience': 'You have advantage against saving throws against poison', 'stonecunning': 'Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.', 'Dwarven Toughness': 'Your hit point maximum increases by 1, and it increases by 1 every time you gain a level'})
}

## Draconic Ancestries
ancestries = {
    'black'  : DraconicAncestry('black', 'acid', '5 by 30ft line', 'dex'),
    'blue'   : DraconicAncestry('blue', 'lightning', '5 by 30ft line', 'dex'),
    'brass'  : DraconicAncestry('brass', 'fire', '5 by 30ft line', 'dex'),
    'bronze' : DraconicAncestry('bronze', 'lightning', '5 by 30ft line', 'dex'),
    'copper' : DraconicAncestry('copper', 'acid', '5 by 30ft line', 'dex'),
    'gold'   : DraconicAncestry('gold', 'fire', '15ft cone', 'dex'),
    'green'  : DraconicAncestry('green', 'poison', '15ft cone', 'con'),
    'red'    : DraconicAncestry('red', 'fire', '15ft cone', 'dex'),
    'silver' : DraconicAncestry('silver', 'cold', '15ft cone', 'con'),
    'white'  : DraconicAncestry('white', 'cold', '15ft cone', 'con')
}

player = Character()

## RACE ## 
# chosen_race = 'mountain dwarf'
print('Amidst the vast expanse of fantasy, which race shall thee assume on this odyssey? Choose wisely, for destiny eagerly awaits your decision.')
for race in available_races:
    print(f'- {race.capitalize()}')

while(True):
    chosen_race = input('\nEnter the name of your chosen race: ').lower()

    if(chosen_race in available_races):
        chosen_race = available_races[chosen_race]
        break
    else: 
        print('Please select a race from the list of available races.')

match chosen_race.name:
    case 'Dragonborn':

        print('Dragonborn of noble kin, reveal your Draconic Ancestry - Red, Blue, Black, or another? The power of your lineage awaits your answer. Available anceestries: ')
        for ancestry in ancestries:
            print(f"- {ancestry}")
            
        while(True):
            chosen_ancestry = input('Enter your choice: ').lower()

            if chosen_ancestry in ancestries.keys():
                chosen_ancestry = ancestries[chosen_ancestry]
                ancestry = chosen_ancestry
                chosen_race.add_resistances(chosen_ancestry.damage_resistance_type)
                chosen_race.additional_traits['breath_weapon'] = ""
                player.add_race(chosen_race)
                print(f"A fine choice indeed. Your {chosen_ancestry.dragon_type.capitalize()} dragon lineage gives you resistance to {chosen_ancestry.damage_resistance_type} damage and a {chosen_ancestry.breath_weapon} {chosen_ancestry.damage_resistance_type} breath weapon.")
                break
            else:
                print('You must select an ancestry from the list above')
    case 'Hill Dwarf':
        player.hit_points += player.level
        player.add_race(chosen_race)
    case _:
        player.add_race(chosen_race)


print(player.race)

## ABILITY SCORES ## 
# decision = input('Do you want to manually enter your stats or have them rolled randomly? \n\nChoose: manual or random \n\n')
decision = 'random'

if decision == 'random':

    #print('\nBehold, as the ethereal dice dance upon the digital plane, conjuring a tapestry of randomly generated scores that shall define your character\'s inherent abilities.')

    random_scores = roll_random_ability_scores()
    
    print('Abilities rolled:')
    for ability in random_scores:
        print(f'{ability}: {random_scores[ability]}')
    
    player.update_ability_scores(random_scores)

elif decision == 'manual':

    print('\nRoll 4d6 and add the three highest together to obtain your ability scores.\n')

    manual_scores = {'str': 0, 'dex': 0, 'con': 0, 'wis': 0, 'int': 0, 'cha': 0}
    score_text = {
        'str': 'Enter thy strength, mighty warrior, and reveal the power within (strength): ', 
        'dex': 'Unveil the nimbleness that courses through thy veins, agile soul (dexterity): ', 
        'con': 'Embrace the endurance that fortifies thy spirit, resilient hero (constitution): ', 
        'wis': 'Tap into the wellspring of wisdom, wise sage, and share its depth (wisdom): ', 
        'int': 'Let the flame of intelligence burn bright, cunning mind, as you disclose its brilliance (intelligence): ', 
        'cha': 'Awaken the aura of charisma that captivates hearts, enchanting soul (charisma): '
    }

    for ability in manual_scores:

        while manual_scores[ability] == 0:
            try: 
                current_score = int(input(score_text[ability]))
            except ValueError: 
                print('\nYou must enter a number\n')

            if current_score in range(3, 19):
                manual_scores[ability] = current_score
            else: 
                print('\nYour score must be between 3 and 18\n')


    #print(manual_scores)
