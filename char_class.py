

class CharClass:

    def __init__(self, name:str, hit_dice:int, saving_throws:list, available_skills:list, 
                 no_of_skills:int, starting_equipment:list, gold_xd4:int, gold_multiplier:bool = True, 
                 armour_training:list = [], weapon_prof:list = [], tool_prof:list = []):
        
        self.name = name
        self.hit_dice = hit_dice
        self.saving_throws = saving_throws
        self.available_skills = available_skills
        self.no_of_skills = no_of_skills
        self.starting_equipment = starting_equipment
        self.gold_xd4 = gold_xd4 # x = no. of d4's rolled to determine the value of gold
        self.gold_multiplier = gold_multiplier # whether or not the value attained from [starting_gold]d4's is multiplied by 10
        self.armour_training = armour_training
        self.weapon_prof = weapon_prof
        self.tool_prof = tool_prof