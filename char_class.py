

class CharClass:

    def __init__(self, name:str, hit_dice:int, saving_throws:list, available_skills:list, 
                 no_of_skills:int, starting_equipment_choices:list, starting_equipment_given:list,
                 gold_dice:str, gold_multiplier:bool = True, armour_training:list = [], 
                 weapon_prof:list = [], tool_prof:list = [], features:dict = []):
        self.name = name
        self.hit_dice = hit_dice
        self.saving_throws = saving_throws
        self.available_skills = available_skills
        self.no_of_skills = no_of_skills
        self.starting_equipment_choices = starting_equipment_choices
        self.starting_equipment_given = starting_equipment_given
        self.gold_dice = gold_dice 
        self.gold_multiplier = gold_multiplier 
        self.armour_training = armour_training
        self.weapon_prof = weapon_prof
        self.tool_prof = tool_prof
        self.features = features
    
    def __repr__(self):
        parts = [f'Class: {self.name}']
        parts.append(f'\nHit Dice: 1d{self.hit_dice}')
        parts.append('\nSaving Throws: ')
        parts.extend(f'-{saving_throw} ' for saving_throw in self.saving_throws)
        parts.append(f'\nChoose {self.no_of_skills} skills from: ')
        parts.extend(f'-{skill} ' for skill in self.available_skills)
        parts.append(f'\nStarting equipment: ')
        parts.extend(f'{item}, ' for item in self.starting_equipment_given)
        for choice in self.starting_equipment_choices:
            parts.append('\nChoose one of the following:\n')
            parts.extend(f'-{option} ' for option in choice)
        parts.append(f'\nStarting gold: {self.gold_dice} ')
        parts.append(f'{"x 10" if self.gold_multiplier else ""}')
        parts.append('\nWeapons proficiency: ')
        parts.extend(f'-{weapons } ' for weapons in self.weapon_prof)
        parts.append('\nArmour training: ')
        parts.extend(f'-{armour} ' for armour in self.armour_training)
        if self.tool_prof:
            parts.append('\nTool proficiency: ')
            parts.extend(f'-{tools }' for tools in self.tool_prof)
        else:
            parts.append('\nNo tool proficiencies')
        
        return ''.join(parts)
