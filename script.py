from character import Character
from util import roll_random_ability_scores, sanitize
from db import available_races, draconic_ancestries

player = Character()

## STEP ONE: CHOOSING A RACE ## 
print('Amidst the vast expanse of fantasy, which race shall thee assume on this odyssey? Choose wisely, for destiny eagerly awaits your decision.')
for race in available_races:
    print(f'- {race.capitalize()}')

choosing_race = True
while(choosing_race):

    chosen_race = sanitize(input('Enter the name of your chosen race: '))
    if(chosen_race in available_races):
        chosen_race = available_races[chosen_race]
        
        choosing_race = False
    else: 
        print('Please select a race from the list of available races.')

match chosen_race.name:
    case 'Dragonborn':

        print('Dragonborn of noble kin, reveal your Draconic Ancestry - Red, Blue, Black, or another? The power of your lineage awaits your answer. Available anceestries: ')
        for ancestry in draconic_ancestries:
            print(f"- {ancestry}")

        choosing_ancestry = True 
        while(choosing_ancestry):
            chosen_ancestry = sanitize(input('Enter your choice: '))

            if chosen_ancestry in draconic_ancestries.keys():
                chosen_ancestry = draconic_ancestries[chosen_ancestry]
                ancestry = chosen_ancestry
                chosen_race.add_resistances(chosen_ancestry.damage_resistance_type)
                player.add_race(chosen_race)
                print(f"A fine choice indeed. Your {chosen_ancestry.dragon_type.capitalize()} dragon lineage gives you resistance to {chosen_ancestry.damage_resistance_type} damage and a {chosen_ancestry.breath_weapon} {chosen_ancestry.damage_resistance_type} breath weapon.")
                
                choosing_ancestry = False
            else:
                print('You must select an ancestry from the list above')
    case 'Hill Dwarf':
        player.hit_points += player.level
        player.add_race(chosen_race)
    case _:
        player.add_race(chosen_race)

## STEP THREE: DETERMINE ABILITY SCORES ## 
deciding = True
while deciding:

    decision = sanitize(input('Do you want to manually enter your stats or have them rolled randomly? type manual or random: '))
    if decision == 'random':
        deciding = False
        #print('\nBehold, as the ethereal dice dance upon the digital plane, conjuring a tapestry of randomly generated scores that shall define your character\'s inherent abilities.')
        random_scores = roll_random_ability_scores()
        player.update_ability_scores(random_scores)

    elif decision == 'manual':
        deciding = False
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
        
    else:
        decision = sanitize(input('Please enter "manual" or "random": '))

print('\n')
print(player)