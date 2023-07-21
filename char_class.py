

class CharClass:

    def __init__(self, name:str, hit_dice:int, saving_throws:list, available_skills:list, 
                 no_of_skills:int, starting_equipment:list, gold_dice:str, gold_multiplier:bool = True, 
                 armour_training:list = [], weapon_prof:list = [], tool_prof:list = []):
        self.name = name
        self.hit_dice = hit_dice
        self.saving_throws = saving_throws
        self.available_skills = available_skills
        self.no_of_skills = no_of_skills
        self.starting_equipment = starting_equipment
        self.gold_dice = gold_dice 
        self.gold_multiplier = gold_multiplier 
        self.armour_training = armour_training
        self.weapon_prof = weapon_prof
        self.tool_prof = tool_prof