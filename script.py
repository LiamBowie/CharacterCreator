from character import Character
from util import roll_random_ability_scores, sanitize
from db import available_races, draconic_ancestries

player = Character()

## RACE ## 
# chosen_race = 'mountain dwarf'
print('Amidst the vast expanse of fantasy, which race shall thee assume on this odyssey? Choose wisely, for destiny eagerly awaits your decision.')
for race in available_races:
    print(f'- {race.capitalize()}')

while(True):
    chosen_race = sanitize(input('\nEnter the name of your chosen race: '))
    if(chosen_race in available_races):
        chosen_race = available_races[chosen_race]
        break
    else: 
        print('Please select a race from the list of available races.')

match chosen_race.name:
    case 'Dragonborn':

        print('Dragonborn of noble kin, reveal your Draconic Ancestry - Red, Blue, Black, or another? The power of your lineage awaits your answer. Available anceestries: ')
        for ancestry in draconic_ancestries:
            print(f"- {ancestry}")
            
        while(True):
            chosen_ancestry = sanitize(input('Enter your choice: '))

            if chosen_ancestry in draconic_ancestries.keys():
                chosen_ancestry = draconic_ancestries[chosen_ancestry]
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
