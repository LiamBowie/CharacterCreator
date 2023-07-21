

class Weapon:
    def __init__(self, name:str, category:str, cost_amount:int, cost_denomination:str, 
                 damage_dice:str, damage_type:str, weight_in_lbs:int, properties:list = []):
        self.name = name
        self.category = category
        self.cost_amount = cost_amount
        self.cost_denomination = cost_denomination
        self.damage_dice = damage_dice
        self.damage_type = damage_type
        self.weight_in_lbs = weight_in_lbs
        self.properties = properties