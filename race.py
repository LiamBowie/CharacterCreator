class Race: 
    def __init__(self, race_name: str, ability_score_increase: dict, size: str, speed:int, lifespan:str, languages: list, resistances: list = [], darkvision: bool = False, weapon_proficiency: list = [], armour_training: list = [], tool_proficiency: list = [], spells: list = [], additional_traits: dict = []):
        self.name = race_name
        self.ability_score_increase = ability_score_increase
        self.size = size
        self.speed = speed
        self.languages = languages
        self.resistances = resistances
        self.darkvision = darkvision
        self.weapon_proficiency = weapon_proficiency
        self.armour_training = armour_training
        self.tool_proficiency = tool_proficiency
        self.spells = spells
        self.additional_traits = additional_traits

    def add_resistances(self, new_resistances):
        self.resistances.append(new_resistances)
    
    def __repr__(self):
        parts = [self.name]
        parts.extend(f"{ability} +{increase}" for ability, increase in self.ability_score_increase.items())
        parts.append(f"size: {self.size}")
        parts.append(f"speed: {self.speed}ft")
        parts.append("speaks, reads, and writes:")
        parts.extend(self.languages)
        parts.append("resistant to:")
        parts.extend(self.resistances)
        return " ".join(parts)
    
class DraconicAncestry:
    def __init__(self, dragon_type, damage_resistance_type, breath_weapon, saving_throw):
        self.dragon_type = dragon_type
        self.damage_resistance_type = damage_resistance_type
        self.breath_weapon = breath_weapon     
        self.saving_throw = saving_throw 