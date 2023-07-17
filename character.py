import math

class Character:
    def __init__(self, name, abilityScores, skills):
        self.name = name
        self.abilityScores = abilityScores
        self.skills = skills

    def getMod(self, ability): 
        return math.floor((self.abilityScores[ability] - 10) / 2)

scores = {"str": 15, "dex": 14, "con": 13, "wis": 12, "int": 10, "cha": 8}
skills = []

pc = Character("Percy", scores)

print(pc.getMod("str"))
print(pc.getMod("dex"))
print(pc.getMod("con"))
print(pc.getMod("wis"))
print(pc.getMod("int"))
print(pc.getMod("cha"))





