import math
import random

class Character:
    def __init__(self, abilityScores):
        self.name = ""
        self.age = 0
        self.abilityScores = abilityScores
        self.skills = []
        self.armourClass = 10 + abilityScores["dex"]
        self.proficiencyBonus = 2

    def addSkill(self, skill):
        self.skills.append(skill)

    def getModifier(self, ability): 
        return math.floor((self.abilityScores[ability] - 10) / 2)


def roll_random_ability_scores():
    ability_scores = {"str": 0, "dex": 0, "con": 0, "wis": 0, "int": 0, "cha": 0}

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

myScores = roll_random_ability_scores()
print(myScores)

