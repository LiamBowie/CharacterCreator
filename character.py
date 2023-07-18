import math
import random

class Character:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.abilityScores = null
        self.skills = []
        self.armourClass = 10
        self.proficiencyBonus = 2

    def addSkill(self, skill):
        self.skills.append(skill)

    def getModifier(self, ability): 
        return math.floor((self.abilityScores[ability] - 10) / 2)


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

# start of script

## ABILITY SCORES ## 
decision = input('Do you want to manual enter your stats or have them rolled randomly? \n\nChoose: manual or random \n\n')

if decision == 'random':

    print('\nBehold, as the ethereal dice dance upon the digital plane, conjuring a tapestry of randomly generated scores that shall define your character\'s inherent abilities.')

    randomScores = roll_random_ability_scores()
    
    for ability in randomScores:
        print(f'{ability}: {randomScores[ability]}')

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


    print(manual_scores)