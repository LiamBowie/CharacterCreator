from race import Race, DraconicAncestry

available_races = {
    'dragonborn' : Race('Dragonborn', {'str': 2, 'cha': 1}, 'medium', 30, ['common', 'draconic'], [], False, [], [], [], {'breath weapon': 'You can use your action to exhale destructive energy. Your draconic ancestry determines the size, shape, and damage type of the exhalation. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw, the type of which is determined by your draconic ancestry. The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level. After you use your breath weapon, you can\'t use it again until you complete a short or long rest.'}),
    'mountain dwarf' : Race('Mountain Dwarf', {'str': 2, 'con': 2}, 'medium', 25, ['common', 'dwarvish'], ['poison'], False, ['battleaxe', 'handaxe', 'lighthammer', 'warhammer'], ['light', 'medium'], ['smith\'s tools', 'brewer\'s supplies', 'mason\'s tools'], {'dwarven resilience': 'You have advantage against saving throws against poison', 'stonecunning': 'Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.'}),
    'hill dwarf': Race('Hill Dwarf', {'con': 2, 'wis': 1}, 'medium', 25, ['common, dwarvish'], ['poison'], True, ['battleaxe', 'handaxe', 'lighthammer', 'warhammer'], ['light', 'medium'], ['smith\'s tools', 'brewer\'s supplies', 'mason\'s tools'], {'dwarven resilience': 'You have advantage against saving throws against poison', 'stonecunning': 'Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.', 'Dwarven Toughness': 'Your hit point maximum increases by 1, and it increases by 1 every time you gain a level'})
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