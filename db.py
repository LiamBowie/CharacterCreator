from race import Race, DraconicAncestry

available_races = {
    'dragonborn' : Race(
        race_name='Dragonborn', 
        ability_score_increase={'str': 2, 'cha': 1}, 
        size='medium', 
        speed=30, 
        lifespan='Young dragonborn grow quickly. They walk hours after hatching, attain the size and development of a 10-year-old human child by the age of 3, and reach adulthood by 15. They live to be around 80.',
        languages=['common', 'draconic'],  
        darkvision=False, 
        additional_traits={
            'breath weapon': 'You can use your action to exhale destructive energy. Your draconic ancestry determines the size, shape, and damage type of the exhalation. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw, the type of which is determined by your draconic ancestry. The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level. After you use your breath weapon, you can\'t use it again until you complete a short or long rest.'
            }
        ),
    'mountain dwarf' : Race(
        race_name='Mountain Dwarf', 
        ability_score_increase={'str': 2, 'con': 2}, 
        size='medium', 
        speed=25, 
        lifespan='Dwarves mature at the same rate as humans, but they\'re considered young until they reach the age of 50. On average, they live about 350 years',
        languages=['common', 'dwarvish'], 
        resistances=['poison'], 
        weapon_proficiency=['battleaxe', 'handaxe', 'lighthammer', 'warhammer'], 
        armour_training=['light', 'medium'], 
        tool_proficiency=['smith\'s tools', 'brewer\'s supplies', 'mason\'s tools'],
        additional_traits= {
            'dwarven resilience': 'You have advantage against saving throws against poison', 
            'stonecunning': 'Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.'
            }
        ),
    'hill dwarf': Race(
        race_name='Hill Dwarf', 
        ability_score_increase={'con': 2, 'wis': 1}, 
        size='medium', 
        speed=25, 
        lifespan='Dwarves mature at the same rate as humans, but they\'re considered young until they reach the age of 50. On average, they live about 350 years',
        languages=['common, dwarvish'], 
        resistances=['poison'], 
        darkvision=True, 
        weapon_proficiency=['battleaxe', 'handaxe', 'lighthammer', 'warhammer'], 
        armour_training=['light', 'medium'], 
        tool_proficiency=['smith\'s tools', 'brewer\'s supplies', 'mason\'s tools'], 
        additional_traits={
            'dwarven resilience': 'You have advantage against saving throws against poison', 
            'stonecunning': 'Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.', 'Dwarven Toughness': 'Your hit point maximum increases by 1, and it increases by 1 every time you gain a level'
            }
        )
}

draconic_ancestries = {
    'black'  : DraconicAncestry('black', 'acid', '5 by 30ft line', 'dex'),
    'blue'   : DraconicAncestry('blue', 'lightning', '5 by 30ft line', 'dex'),
    'brass'  : DraconicAncestry('brass', 'fire', '5 by 30ft line', 'dex'),
    'bronze' : DraconicAncestry('bronze', 'lightning', '5 by 30ft line', 'dex'),
    'copper' : DraconicAncestry('copper', 'acid', '5 by 30ft line', 'dex'),
    'gold'   : DraconicAncestry('gold', 'fire', '15ft cone', 'dex'),
    'green'  : DraconicAncestry('green', 'poison', '15ft cone', 'con'),
    'red'    : DraconicAncestry('red', 'fire', '15ft cone', 'dex'),
    'silver' : DraconicAncestry('silver', 'cold', '15ft cone', 'con'),
    'white'  : DraconicAncestry('white', 'cold', '15ft cone', 'con')
}