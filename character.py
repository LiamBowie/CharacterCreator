import math

starting_scores = {'str': 0, 'dex': 0, 'con': 0, 'wis': 0, 'int': 0, 'cha': 0}

class Character:
    level = 1
    proficiency_bonus = 2
    armour_class = 10
    hit_points = 0

    def __init__(self, name:str = '', level:int = 1, proficiency_bonus:int = 2, armour_class:int = 10, 
                 hit_points:int = 0, ability_scores:dict = starting_scores, race:str = '', size:str = '',
                 speed:int = 0, languages:list = [],  darkvision:bool = False, resistances:list = [],
                 weapon_proficiency:list = [], armour_training:list = [], tool_proficiency:list = [],
                 spells:list = [], traits:dict = {}):
        self.name = name
        self.level = level
        self.proficiency_bonus = proficiency_bonus
        self.armour_class = armour_class
        self.hit_points = hit_points
        self.ability_scores = ability_scores
        self.race = race
        self.size = size
        self.speed = speed
        self.languages = languages
        self.darkvision = darkvision
        self.resistances = resistances
        self.weapon_proficiency = weapon_proficiency
        self.armour_training = armour_training
        self.tool_proficiency = tool_proficiency
        self.spells = spells
        self.traits = traits

    def __repr__(self):
        return (
            f"Character(name='{self.name}', level={self.level}, proficiency_bonus={self.proficiency_bonus}, "
            f"armour_class={self.armour_class}, hit_points={self.hit_points}, ability_scores={self.ability_scores}, "
            f"race='{self.race}', size='{self.size}', speed={self.speed}, languages={self.languages}, "
            f"darkvision={self.darkvision}, resistances={self.resistances}, weapon_proficiency={self.weapon_proficiency}, "
            f"armour_training={self.armour_training}, tool_proficiency={self.tool_proficiency}, spells={self.spells}, "
            f"traits={self.traits})"
        )

    def add_race(self, race):
        self.race = race.name
        for ability in race.ability_score_increase:
            self.ability_scores[ability] += race.ability_score_increase[ability]
        self.size = race.size
        self.speed = race.speed
        self.languages.extend(race.languages)
        self.resistances.extend(race.resistances)
        self.darkvision = race.darkvision
        self.weapon_proficiency.extend(race.weapon_proficiency)
        self.armour_training.extend(race.armour_training)
        self.tool_proficiency.extend(race.tool_proficiency)
        self.spells.extend(race.spells)
        self.traits.update(race.additional_traits)


    def update_ability_scores(self, new_scores):
        for ability in new_scores:
            self.ability_scores[ability] += new_scores[ability]

    def add_skill(self, skill):
        self.skills.append(skill)

    def get_modifier(self, ability): 
        return math.floor((self.ability_scores[ability] - 10) / 2)

