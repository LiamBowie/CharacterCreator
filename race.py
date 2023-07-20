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
        parts.extend(f'{ability} +{increase}' for ability, increase in self.ability_score_increase.items())
        parts.append(f'size: {self.size}')
        parts.append(f'speed: {self.speed}ft')
        parts.append('speaks, reads, and writes:')
        parts.extend(f'- {language}' for language in self.languages)
        if(self.darkvision):
            parts.append('Darkvision')

        if(self.resistances):
            parts.append('resistant to:')
            parts.extend(f'- {resistance}' for resistance in self.resistances)
        else: 
            parts.append('No resistances')

        if(self.weapon_proficiency):
            parts.append('Weapon proficiencies:')
            parts.extend(f'- {proficiency}' for proficiency in self.weapon_proficiency)
        else:
            parts.append('No weapon proficiencies')
        
        if(self.armour_training):
            parts.append('Armour training:')
            parts.extend(f'- {armour_type}' for armour_type in self.armour_training)
        else:
            parts.append('No armour training')
            
        if(self.tool_proficiency):
            parts.append('Tool proficiencies:')
            parts.extend(f'- {tools}' for tools in self.tool_proficiency)
        else:
            parts.append('No tool proficiencies')
        
        if(self.spells):
            parts.append('Spells known:')
            parts.extend(f'- {spell}' for spell in self.spells)

        parts.append('Additional traits:')
        parts.extend(f'{title}. {description}' for title, description in self.additional_traits.items())
        
        return "\n".join(parts)
    
class DraconicAncestry:
    def __init__(self, dragon_type, damage_resistance_type, breath_weapon, saving_throw):
        self.dragon_type = dragon_type
        self.damage_resistance_type = damage_resistance_type
        self.breath_weapon = breath_weapon     
        self.saving_throw = saving_throw 