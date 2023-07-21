from race import Race, DraconicAncestry
from char_class import CharClass
from weapon import Weapon

races = {
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
        darkvision=True,
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
        ),
        'drow elf': Race(
            race_name='Drow Elf',
            ability_score_increase={'dex': 2, 'cha': 1},
            size='medium',
            speed=30,
            lifespan='Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old.',
            languages=['common', 'elvish'],
            darkvision=True,
            weapon_proficiency=['rapiers', 'shortswords', 'hand crossbows'],
            spells=['dancing lights'],
            additional_traits={
                'superior darkvision': 'Accustomed to the depths of the Underdark, you have superior vision in dark and dim conditions. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can\'t discern color in darkness, only shades of gray.',
                'keen senses': 'You have proficiency in the Perception skill.',
                'fey ancestry': 'You have advantage on saving throws against being charmed, and magic can\'t put you to sleep.',
                'trance': 'Elves don\'t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is "trance.") While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep. \nIf you meditate during a long rest, you finish the rest after only 4 hours. You otherwise obey all the rules for a long rest; only the duration is changed.',
                'sunlight sensitivity': 'You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.'
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

classes = {
    'barbarian': CharClass(
        name='Barbarian',
        hit_dice=12,
        saving_throws=['str', 'con'],
        available_skills=['animal handling', 'athletics', 'intimidation', 'nature', 'perception', 'survival'],
        no_of_skills=2,
        starting_equipment=[['greataxe', 'any martial weapon'], ['two handaxes', 'any simple weapon'], ['explorer\'s pack'], ['four javelins'] ],
        gold_dice='2d4',
        armour_training=['light', 'medium', 'shields'],
        weapon_prof=['simple', 'martial']
    )
}

weapons = {
    'club': Weapon(
        name='Club',
        category='simple melee',
        cost_amount=1,
        cost_denomination='sp',
        damage_dice='1d4',
        damage_type='bludgeoning',
        weight_in_lbs=2,
        properties=['light']
    ),
    'dagger': Weapon(
        name='Dagger',
        category='simple melee',
        cost_amount=2,
        cost_denomination='gp',
        damage_dice='1d4',
        damage_type='piercing',
        weight_in_lbs=1,
        properties=['finesse', 'light', 'range(20/60)']
    ),
    'greatclub': Weapon(
        name='Greatclub',
        category='simple melee',
        cost_amount=2,
        cost_denomination='sp',
        damage_dice='1d8',
        damage_type='bludgeoning',
        weight_in_lbs=10,
        properties=['two-handed']
    ),
    'handaxe': Weapon(
        name='Handaxe',
        category='simple melee',
        cost_amount=5,
        cost_denomination='gp',
        damage_dice='1d6',
        damage_type='slashing',
        weight_in_lbs=2,
        properties=['light', 'range(20/60)']
    ),
    'javelin': Weapon(
        name='Javelin',
        category='simple melee',
        cost_amount=5,
        cost_denomination='sp',
        damage_dice='1d6',
        damage_type='piercing',
        weight_in_lbs=2,
        properties=['range(20/60)']
    ),
    'light hammer': Weapon(
        name='Light hammer',
        category='simple melee',
        cost_amount=2,
        cost_denomination='gp',
        damage_dice='1d4',
        damage_type='bludgeoning',
        weight_in_lbs=2,
        properties=['light', 'range(20/60)', 'versatile(1d8)']
    ),
    'mace':  Weapon(
        name='Mace',
        category='simple melee',
        cost_amount=5,
        cost_denomination='gp',
        damage_dice='1d6',
        damage_type='bludgeoning',
        weight_in_lbs=4,
    ),
    'quarterstaff':  Weapon(
        name='Quarterstaff',
        category='simple melee',
        cost_amount=2,
        cost_denomination='sp',
        damage_dice='1d6',
        damage_type='bludgeoning',
        weight_in_lbs=4,
        properties=['versatile(1d8)']
    ),
    'sickle': Weapon(
        name='Sickle',
        category='simple melee',
        cost_amount=1,
        cost_denomination='gp',
        damage_dice='1d4',
        damage_type='slashing',
        weight_in_lbs=2,
        properties=['light']
    ),
    'spear': Weapon(
        name='Spear',
        category='simple melee',
        cost_amount=1,
        cost_denomination='gp',
        damage_dice='1d6',
        damage_type='piercing',
        weight_in_lbs=0,
        properties=['range(20/60)', 'versatile(1d8)']
    ),
    'light crossbow': Weapon(
        name='Light crossbow',
        category='simple ranged',
        cost_amount=25,
        cost_denomination='gp',
        damage_dice='1d8',
        damage_type='piercing',
        weight_in_lbs=5,
        properties=['ammunition', 'range(80/320)', 'loading', 'two-handed']
    ),
    'dart': Weapon(
        name='Dart',
        category='simple ranged',
        cost_amount=5,
        cost_denomination='cp',
        damage_dice='1d4',
        damage_type='piercing',
        weight_in_lbs=0.25,
        properties=['finesse', 'range(20/60)']
    ),
    'shortbow': Weapon(
        name='Shortbow',
        category='simple ranged',
        cost_amount=25,
        cost_denomination='gp',
        damage_dice='1d8',
        damage_type='piercing',
        weight_in_lbs=2,
        properties=['ammunition', 'range(80/320)', 'two-handed']
    ),
    'sling': Weapon(
        name='Sling',
        category='simple ranged',
        cost_amount=1,
        cost_denomination='sp',
        damage_dice='1d4',
        damage_type='bludgeoning',
        weight_in_lbs=0,
        properties=['ammunition', 'range(30/120)']
    ),
    'battleaxe': Weapon(
        name='Battleaxe',
        category='martial melee',
        cost_amount=10,
        cost_denomination='gp',
        damage_dice='1d8',
        damage_type='slashing',
        weight_in_lbs=4,
        properties=['versatile(1d10)']
    ),
    'flail': Weapon(
        name='Flail',
        category='martial melee',
        cost_amount=10,
        cost_denomination='gp',
        damage_dice='1d8',
        damage_type='bludgeoning',
        weight_in_lbs=2
    ),
    'glaive': Weapon(
        name='Glaive',
        category='martial melee',
        cost_amount=20,
        cost_denomination='gp',
        damage_dice='1d10',
        damage_type='slashing',
        weight_in_lbs=6,
        properties=['heavy', 'reach', 'two-handed']
    ),
    'greataxe': Weapon(
        name='Greataxe',
        category='martial melee',
        cost_amount=30,
        cost_denomination='gp',
        damage_dice='1d12',
        damage_type='slashing',
        weight_in_lbs=7,
        properties=['heavy', 'two-handed']
    ),
    'greatsword': Weapon(
        name='Greatsword',
        category='martial melee',
        cost_amount=50,
        cost_denomination='gp',
        damage_dice='2d6',
        damage_type='slashing',
        weight_in_lbs=6,
        properties=['heavy', 'two-handed']
    ),
    'halberd': Weapon(
        name='Halberd',
        category='martial melee',
        cost_amount=20,
        cost_denomination='gp',
        damage_dice='1d10',
        damage_type='slashing',
        weight_in_lbs=6,
        properties=['heavy', 'reach', 'two-handed']
    ),
    'lance': Weapon(
        name='Lance',
        category='martial melee',
        cost_amount=10,
        cost_denomination='gp',
        damage_dice='1d12',
        damage_type='piercing',
        weight_in_lbs=6,
        properties=['reach', 'special']
    ),
    'longsword': Weapon(
        name='Longsword',
        category='martial melee',
        cost_amount=15,
        cost_denomination='gp',
        damage_dice='1d8',
        damage_type='slashing',
        weight_in_lbs=3,
        properties=['versatile(1d10)']
    ),
    'maul': Weapon(
        name='Maul',
        category='martial melee',
        cost_amount=10,
        cost_denomination='gp',
        damage_dice='2d6',
        damage_type='bludgeoning',
        weight_in_lbs=10,
        properties=['heavy', 'two-handed']
    ),
    'morningstar': Weapon(
        name='Morningstar',
        category='martial melee',
        cost_amount=15,
        cost_denomination='gp',
        damage_dice='1d8',
        damage_type='piercing',
        weight_in_lbs=4
    ),
    'pike': Weapon(
        name='Pike',
        category='martial melee',
        cost_amount=5,
        cost_denomination='gp',
        damage_dice='1d10',
        damage_type='piercing',
        weight_in_lbs=18,
        properties=['heavy', 'reach', 'two-handed']
    ),
    'rapier': Weapon(
        name='Rapier',
        category='martial melee',
        cost_amount=25,
        cost_denomination='gp',
        damage_dice='1d8',
        damage_type='piercing',
        weight_in_lbs=2,
        properties=['finesse']
    ),
    'scimitar': Weapon(
        name='Scimitar',
        category='martial melee',
        cost_amount=25,
        cost_denomination='gp',
        damage_dice='1d6',
        damage_type='slashing',
        weight_in_lbs=3,
        properties=['finesse', 'light']
    ),
    'shortsword': Weapon(
        name='Shortsword',
        category='martial melee',
        cost_amount=10,
        cost_denomination='gp',
        damage_dice='1d6',
        damage_type='piercing',
        weight_in_lbs=2,
        properties=['finesse', 'light']
    ),
    'trident': Weapon(
        name='Trident',
        category='martial melee',
        cost_amount=5,
        cost_denomination='gp',
        damage_dice='1d6',
        damage_type='piercing',
        weight_in_lbs=4,
        properties=['range(20/60)', 'versatile(1d8)']
    ),
    'war pick': Weapon(
        name='War pick',
        category='martial melee',
        cost_amount=5,
        cost_denomination='gp',
        damage_dice='1d8',
        damage_type='piercing',
        weight_in_lbs=2
    ),
    'warhammer': Weapon(
        name='Warhammer',
        category='martial melee',
        cost_amount=15,
        cost_denomination='gp',
        damage_dice='1d8',
        damage_type='bludgeoning',
        weight_in_lbs=2,
        properties=['versatile(1d10)']
    ),
    'whip': Weapon(
        name='Whip',
        category='martial melee',
        cost_amount=2,
        cost_denomination='gp',
        damage_dice='1d4',
        damage_type='slashing',
        weight_in_lbs=3,
        properties=['finesse', 'reach']
    ),
    'blowgun': Weapon(
        name='Blowgun',
        category='martial ranged',
        cost_amount=10,
        cost_denomination='gp',
        damage_dice='1d1',
        damage_type='piercing',
        weight_in_lbs=1,
        properties=['ammunition', 'range(25/100)', 'loading']
    ),
    'hand crossbow': Weapon(
        name='Hand crossbow',
        category='martial ranged',
        cost_amount=75,
        cost_denomination='gp',
        damage_dice='1d6',
        damage_type='piercing',
        weight_in_lbs=3,
        properties=['ammunition', 'range(30/120)', 'light', 'loading']
    ),
    'heavy crossbow': Weapon(
        name='Heavy crossbow',
        category='martial ranged',
        cost_amount=50,
        cost_denomination='gp',
        damage_dice='1d10',
        damage_type='piercing',
        weight_in_lbs=18,
        properties=['ammunition', 'range(100/400)', 'heavy', 'loading', 'two-handed']
    ),
    'longbow': Weapon(
        name='Longbow',
        category='martial ranged',
        cost_amount=50,
        cost_denomination='gp',
        damage_dice='1d8',
        damage_type='piercing',
        weight_in_lbs=2,
        properties=['ammunition', 'range(150/600)', 'heavy', 'two-handed']
    ),
    'net': Weapon(
        name='Net',
        category='martial ranged',
        cost_amount=1,
        cost_denomination='gp',
        damage_dice='0d0',
        damage_type='',
        weight_in_lbs=3,
        properties=['special', 'thrown', 'range(5/15)']
    )
}