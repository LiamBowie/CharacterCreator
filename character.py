import math
import random

class Race: 
    def __init__(self, race_name, ability_score_increase, size, speed, languages, resistances):
        self.race_name = race_name
        self.ability_score_increase = ability_score_increase
        self.size = size
        self.speed = speed
        self.languages = languages
        self.resistances = resistances

    def add_resitances(self, new_resistances):
        for resistance in new_resistances:
            self.resistances.append(resistance)
    
    def __repr__(self):
        string = self.race_name.capitalize() + ";"
        for ability in self.ability_score_increase:
            string += f" {ability} +{self.ability_score_increase[ability]}"
        string += f"; size: {self.size}; speed: {self.speed}ft; speaks, reads, and writes:"
        for lang in self.languages:
            string += f" {lang}"
        string += "; resistant to: "
        for resistance in self.resistances:
            string += resistance
        return string

class Draconic_Ancestry:
    def __init__(self, dragon_type, damage_resistance_type, breath_weapon, saving_throw):
        self.dragon_type = dragon_type
        self.damage_resistance_type = damage_resistance_type
        self.breath_weapon = breath_weapon     
        self.saving_throw = saving_throw  

class Character:
    def __init__(self):
        self.ability_scores = {'str': 0, 'dex': 0, 'con': 0, 'wis': 0, 'int': 0, 'cha': 0}
        self.skills = []
        self.armourClass = 10
        self.proficiencyBonus = 2

    def add_race(self, race):
        self.race = race

        for ability in race.ability_score_increase:
            self.ability_scores[ability] += race.ability_score_increase[ability]

    def update_ability_scores(self, new_scores):
        for ability in new_scores:
            self.ability_scores[ability] += new_scores[ability]

    def add_skill(self, skill):
        self.skills.append(skill)

    def get_modifier(self, ability): 
        return math.floor((self.ability_scores[ability] - 10) / 2)

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

## Create a list of available classes (race_name, ability_score_increase, size, speed, languages) ## 


## Available races
available_races = {
    "dragonborn" : Race('Dragonborn', {'str': 2, 'cha': 1}, 'medium', 30, ['common', 'draconic'], []),
    "mountain dwarf" : Race('Mountain Dwarf', {'str': 2, 'con': 2}, 'medium', 25, ['common', 'dwarvish'], ['poison'])
}

## Draconic Ancestries
ancestries = {
    'black'  : Draconic_Ancestry('black', 'acid', '5 by 30ft line', 'dex'),
    'blue'   : Draconic_Ancestry('blue', 'lightning', '5 by 30ft line', 'dex'),
    'brass'  : Draconic_Ancestry('brass', 'fire', '5 by 30ft line', 'dex'),
    'bronze' : Draconic_Ancestry('bronze', 'lightning', '5 by 30ft line', 'dex'),
    'copper' : Draconic_Ancestry('copper', 'acid', '5 by 30ft line', 'dex'),
    'gold'   : Draconic_Ancestry('gold', 'fire', '15ft cone', 'dex'),
    'green'  : Draconic_Ancestry('green', 'poison', '15ft cone', 'con'),
    'red'    : Draconic_Ancestry('red', 'fire', '15ft cone', 'dex'),
    'silver' : Draconic_Ancestry('silver', 'cold', '15ft cone', 'con'),
    'white'  : Draconic_Ancestry('white', 'cold', '15ft cone', 'con')
}

player = Character()

## RACE ## 
# chosen_race = 'mountain dwarf'
print('Amidst the vast expanse of fantasy, which race shall thee assume on this odyssey? Choose wisely, for destiny eagerly awaits your decision.')
for race in available_races:
    print(f'- {race.capitalize()}')

while(not hasattr(player, 'race')):
    chosen_race = input('\nEnter the name of your chosen race: ').lower()
    if chosen_race == 'dragonborn':
        chosen_race = available_races[chosen_race]
        chosen_ancestry = 'none'

        print('Dragonborn of noble kin, reveal your Draconic Ancestry - Red, Blue, Black, or another? The power of your lineage awaits your answer. Available anceestries: ')
        for ancestry in ancestries:
            print(f"- {ancestry}")
            
        while (chosen_ancestry == 'none'):
            chosen_ancestry = input('Enter your choice: ').lower()

            if chosen_ancestry in ancestries.keys():
                chosen_ancestry = ancestries[chosen_ancestry]
                ancestry = chosen_ancestry
                chosen_race.add_resitances(chosen_ancestry.damage_resistance_type)
                player.add_race(chosen_race)
                print(f"A fine choice indeed. Your {chosen_ancestry.dragon_type.capitalize()} dragon lineage gives you resistance to {chosen_ancestry.damage_resistance_type} damage and a {chosen_ancestry.breath_weapon} {chosen_ancestry.damage_resistance_type} breath weapon.")
            else:
                print('You must select an ancestry from the list above')
    else:
        if(chosen_race in available_races):
            player.add_race(available_races[chosen_race])
        else: 
            print('Please select a race from the list of available races.')

print(player.race)

## ABILITY SCORES ## 
# decision = input('Do you want to manual enter your stats or have them rolled randomly? \n\nChoose: manual or random \n\n')
decision = 'random'

if decision == 'random':

    #print('\nBehold, as the ethereal dice dance upon the digital plane, conjuring a tapestry of randomly generated scores that shall define your character\'s inherent abilities.')

    random_scores = roll_random_ability_scores()
    
    # for ability in random_scores:
    #     print(f'{ability}: {random_scores[ability]}')
    
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
