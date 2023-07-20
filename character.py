import math

class Character:
    level = 1
    proficiency_bonus = 2
    armour_class = 10
    hit_points = 0
    ability_scores = {'str': 0, 'dex': 0, 'con': 0, 'wis': 0, 'int': 0, 'cha': 0}

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

