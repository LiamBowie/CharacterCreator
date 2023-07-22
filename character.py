import math
from util import roll

starting_scores = {'str': 0, 'dex': 0, 'con': 0, 'wis': 0, 'int': 0, 'cha': 0}

class Character:
    def __init__(self, name:str = '', level:int = 1, proficiency_bonus:int = 2, armour_class:int = 10, 
                 hit_points:int = 0, hit_dice:int = 0, ability_scores:dict = starting_scores, saving_throws:list = [],
                 skills:list = [], initiative:int = 0, race:str = '', character_class = '', size:str = '',
                 speed:int = 0, languages:list = [],  darkvision:bool = False, resistances:list = [],
                 weapon_proficiency:list = [], armour_training:list = [], tool_proficiency:list = [],
                 spells:list = [], traits:dict = {}, equipment:list = []):
        self.name = name
        self.level = level
        self.proficiency_bonus = proficiency_bonus
        self.armour_class = armour_class
        self.hit_points = hit_points
        self.hit_dice = hit_dice
        self.ability_scores = ability_scores
        self.saving_throws = saving_throws
        self.skills = skills
        self.initiative = initiative
        self.race = race
        self.character_class = character_class
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
        self.equipment = equipment

    def __repr__(self):
        parts = [f'{self.name.capitalize()}, level {self.level} {self.race} {self.character_class}']
        parts.append(f'{self.size.capitalize()} creature')
        parts.append(f'AC: {self.armour_class}, Initiative: {"+" if self.get_modifier("dex") >= 0 else ""}{self.initiative}, Speed: {self.speed}ft, HP: {self.hit_points}')
        parts.append(f'Hit dice: d{self.hit_dice} Proficiency bonus: +{self.proficiency_bonus}') 
        for ability in self.ability_scores:
            parts.append(f'{ability}: {self.ability_scores[ability]} ({"+" if self.get_modifier(ability) >= 0 else ""}{self.get_modifier(ability)})')
        parts.append('Saving Throws:')
        parts.extend(saving_throw for saving_throw in self.saving_throws)
        parts.append('Skills:')
        parts.extend(skill for skill in self.skills)
        if self.darkvision:
            parts.append(f'Darkvision')
        parts.append('Speaks, reads, and writes:')
        parts.extend(f'- {language.capitalize()}' for language in self.languages)
        if self.resistances:
            parts.append('Resistances:')
            parts.extend(f'- {resistance.capitalize()}' for resistance in self.resistances)
        else: 
            parts.append('No resistances')
        if self.weapon_proficiency:
            parts.append('Weapon proficiencies:')
            parts.extend(f'- {proficiency.capitalize()}' for proficiency in self.weapon_proficiency)
        else:
            parts.append('No weapon proficiencies')
        if self.armour_training:
            parts.append('Armour training:')
            parts.extend(f'- {armour_type.capitalize()}' for armour_type in self.armour_training)
        else:
            parts.append('No armour training')   
        if self.tool_proficiency:
            parts.append('Tool proficiencies:')
            parts.extend(f'- {tools.capitalize()}' for tools in self.tool_proficiency)
        else:
            parts.append('No tool proficiencies')
        parts.append('Equipment:')
        parts.extend(item for item in self.equipment)
        parts.append(f'Starting Gold: {self.starting_gold}gp')
        if self.spells:
            parts.append('Spells known:')
            parts.extend(f'- {spell.capitalize()}' for spell in self.spells)
        parts.append('Traits:')
        parts.extend(f'{title.capitalize()}. {description}' for title, description in self.traits.items())
        
        return '\n'.join(parts)

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

    def add_class(self, character_class, chosen_skills, chosen_equipment):
        self.character_class = character_class.name
        self.hit_dice = character_class.hit_dice
        self.hit_points = self.hit_dice + self.get_modifier('con')
        self.saving_throws.extend(character_class.saving_throws)
        self.skills = chosen_skills
        if chosen_equipment:
            self.equipment = chosen_equipment
        else:
            self.starting_gold = roll(character_class.gold_dice)
            if character_class.gold_multiplier == True:
                self.starting_gold*10
        self.armour_training.extend(armour for armour in character_class.armour_training if armour not in self.armour_training)
        self.weapon_proficiency.extend(prof for prof in character_class.weapon_prof if prof not in self.weapon_proficiency)
        self.tool_proficiency.extend(tools for tools in character_class.tool_prof if tools not in self.tool_proficiency)

    def set_initiative(self):
        self.initiative = self.get_modifier('dex')
    
    def set_armour_class(self):
        self.armour_class = 10 + self.get_modifier('dex')

    def update_ability_scores(self, new_scores):
        for ability in new_scores:
            self.ability_scores[ability] += new_scores[ability]
        self.set_initiative()
        self.set_armour_class()

    def add_skill(self, skill):
        self.skills.append(skill)

    def get_modifier(self, ability): 
        return math.floor((self.ability_scores[ability] - 10) / 2)

