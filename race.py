class Race: 
    def __init__(self, race_name: str, ability_score_increase: dict, size: str, speed:int, languages: list, resistances: list, darkvision: bool, weapon_proficiency: list, armour_training: list, tool_proficiency: list, additional_traits: dict):
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
        self.additional_traits = additional_traits

    def add_resistances(self, new_resistances):
        for resistance in new_resistances:
            self.resistances.append(resistance)
    
    def __repr__(self):
        string = self.name + ";"
        for ability in self.ability_score_increase:
            string += f" {ability} +{self.ability_score_increase[ability]}"
        string += f"; size: {self.size}; speed: {self.speed}ft; speaks, reads, and writes:"
        for lang in self.languages:
            string += f" {lang}"
        string += "; resistant to: "
        for resistance in self.resistances:
            string += resistance
        return string
    
class DraconicAncestry:
    def __init__(self, dragon_type, damage_resistance_type, breath_weapon, saving_throw):
        self.dragon_type = dragon_type
        self.damage_resistance_type = damage_resistance_type
        self.breath_weapon = breath_weapon     
        self.saving_throw = saving_throw 