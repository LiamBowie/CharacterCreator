from race import Race, DraconicAncestry
from char_class import CharClass
from util import remove_item_from_list
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
            'darkvision': 'Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can\'t discern color in darkness, only shades of gray.',
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
            'darkvision': 'Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can\'t discern color in darkness, only shades of gray.',
            'dwarven resilience': 'You have advantage against saving throws against poison', 
            'stonecunning': 'Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.', 
            'dwarven toughness': 'Your hit point maximum increases by 1, and it increases by 1 every time you gain a level'
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

def get_weapon_keys_by_category(category):
    result = []
    for key, weapon in weapons.items():
        if weapon.category == category:
            result.append(key)
    return result

classes = {
    'barbarian': CharClass(
        name='Barbarian',
        hit_dice=12,
        saving_throws=['str', 'con'],
        available_skills=['animal handling', 'athletics', 'intimidation', 'nature', 'perception', 'survival'],
        no_of_skills=2,
        starting_equipment_choices=[
                get_weapon_keys_by_category('martial melee'), 
                ['two handaxes'] + remove_item_from_list('handaxe', get_weapon_keys_by_category('simple melee')), 
            ],
        starting_equipment_given=['explorer\'s pack', 'four javelins'],
        gold_dice='2d4',
        armour_training=['light', 'medium', 'shields'],
        weapon_prof=['simple melee', 'simple ranged', 'martial melee', 'martial ranged'],
        features={
            'rage': 
    '''In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action.
    While raging, you gain the following benefits if you aren\'t wearing heavy armor:
        1. You have advantage on Strength checks and Strength saving throws.
        2. When you make a melee weapon attack using Strength, you gain a +2 bonus to the damage roll. This bonus increases as you level.
        3. You have resistance to bludgeoning, piercing, and slashing damage.
    If you are able to cast spells, you can\'t cast them or concentrate on them while raging.
    Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven\'t attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action.
    Once you have raged the maximum number of times for your barbarian level, you must finish a long rest before you can rage again. You may rage 2 times at 1st level, 3 at 3rd, 4 at 6th, 5 at 12th, and 6 at 17th.
        ''',
            'unarmoured defence': 'While you are not wearing any armor, your Armor Class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.'
        }
    ),
    'bard': CharClass(
        name='Bard',
        hit_dice=8,
        saving_throws=['dex', 'cha'],
        available_skills=["acrobatics", "animal Handling", "arcana", "athletics", "deception", "history", "insight", "intimidation", "investigation", "medicine", "nature", "perception", "performance", "persuasion", "religion", "sleight of Hand", "stealth", "survival"],
        no_of_skills=3,
        starting_equipment_choices=[
            ['rapier', 'longsword'] + get_weapon_keys_by_category('simple melee') + get_weapon_keys_by_category('simple ranged'),
            ['diplomat\'s pack', 'entertainer\'s pack'],
            ['lute', 'bagpipes', 'drum', 'dulcimer', 'flute', 'horn', 'lyre', 'pan flute', 'shawm', 'viol']
        ],
        starting_equipment_given=['leather armour', 'dagger'],
        gold_dice='5d4',
        armour_training=['light'],
        weapon_prof=['simple melee', 'simple ranged', 'hand crossbow', 'longsword', 'rapier', 'shortsword'],
        tool_prof=['Three musical instruments of your choice'],
        features={
            'bardic inspiration': 
    '''You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a d6. 
    Once within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time.
    You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain any expended uses when you finish a long rest.
    Your Bardic Inspiration die changes when you reach certain levels in this class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level.'''
        }
    ),
    'cleric': CharClass(
        name='Cleric',
        hit_dice=8,
        saving_throws=['wis', 'cha'],
        available_skills=['history', 'insight', 'medecine', 'persuasion', 'religion'],
        no_of_skills=2,
        starting_equipment_choices=[
            ['mace', 'warhammer' ], # warhammer if proficient
            ['scale mail', 'leather armour', 'chain mail'], # chain mail if proficient
            ['light crossbow, 20 bolts'] + get_weapon_keys_by_category('simple melee') + get_weapon_keys_by_category('simple ranged'),
            ['priest\'s pack', 'explorer\'s pack']
        ],
        starting_equipment_given=['shield', 'holy symbol'],
        gold_dice='5d4',
        armour_training=['light', 'medium', 'shields'],
        weapon_prof=['simple melee', 'simple ranged']
    ),
    'druid': CharClass(
        name='Druid',
        hit_dice=8,
        saving_throws=['int', 'wis'],
        available_skills=['arcana', 'animal handling', 'insight', 'medecine', 'nature', 'perception', 'religion', 'survival'],
        no_of_skills=2,
        starting_equipment_choices=[
            ['shield'] + get_weapon_keys_by_category('simple melee'),
            ['scimitar'] + get_weapon_keys_by_category('simple melee') + get_weapon_keys_by_category('simple ranged')
        ],
        starting_equipment_given=['leather armour', 'explorer\'s pack', 'druidic focus'],
        gold_dice='2d4',
        armour_training=['light', 'medium', 'shields'],
        weapon_prof=['clubs', 'daggers', 'darts', 'javelins', 'maces', 'quarterstaffs', 'scimitars', 'sickles', 'slings', 'spears'],
        tool_prof=['herbalism kit'],
        features={
            'druidic': 'You know Druidic, the secret language of druids. You can speak the language and use it to leave hidden messages. You and others who know this language automatically spot such a message. Others spot the message\'s presence with a successful DC 15 Wisdom (Perception) check but can\'t decipher it without magic.'
        }
    ),
    # 'fighter': CharClass(
    #     name='Fighter',
    #     hit_dice=10,
    #     saving_throws=['str', 'con']
    # ),
    # 'monk': CharClass(
    #     name='Monk',
    #     hit_dice=8,
    #     saving_throws=['str', 'dex']
    # ),
    # 'paladin': CharClass(
    #     name='Paladin',
    #     hit_dice=10, 
    #     saving_throws=['wis', 'cha']
    # ),
    # 'ranger': CharClass(
    #     name='Ranger',
    #     hit_dice=10,
    #     saving_throws=['str', 'dex']
    # ),
    # 'rogue': CharClass(
    #     name='Rogue',
    #     hit_dice=8,
    #     saving_throws=['dex', 'int']
    # ),
    # 'sorcerer': CharClass(
    #     name='Sorcerer',
    #     hit_dice=6,
    #     saving_throws=['con', 'cha']
    # ),
    # 'warlock': CharClass(
    #     name='Warlock',
    #     hit_dice=8,
    #     saving_throws=['wis', 'cha']
    # ),
    'wizard': CharClass(
        name="Wizard",
        hit_dice=6,
        saving_throws=['int', 'wis'],
        available_skills=['arcana', 'history', 'insight', 'investigation', 'medecine', 'religion'],
        no_of_skills=2,
        starting_equipment_choices=[
            ['quarterstaff', 'dagger'],#
            ['component pouch', 'arcane focus'],
            ['scholar\'s pack', 'explorer\'s pack']
        ],
        starting_equipment_given=["spellbook"],
        gold_dice="4d4",
        weapon_prof=["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"],
        features={"Arcane Recovery": 
    '''You have learned to regain some of your magical energy by studying your spellbook. Once per day when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your wizard level (rounded up), and none of the slots can be 6th level or higher. 
    For example, if you're a 4th-level wizard, you can recover up to two levels worth of spell slots. 
    You can recover either a 2nd-level spell slot or two 1st-level spell slots.'''},
    )
}