import re

all_colors = {
        "UN": "#080807",
        "IR": "#482F1E",
        "BR": "#A86F4D",
        "SI": "#CAC2BA",
        "GO": "#BABA36",
        "PL": "#5DB1AF",
        "DI": "#5D62EE",
        "MA": "#EE5DEB",
        "GR": "#E75A5A",
        "CH": "#A6F368"
    }

all_fonts_colors = {
        "UN": "white",
        "IR": "white",
        "BR": "white",
        "SI": "black",
        "GO": "black",
        "PL": "white",
        "DI": "white",
        "MA": "white",
        "GR": "white",
        "CH": "blue"
    }

all_champion_id = {
    1: 'Annie',
    2: 'Olaf',
    3: 'Galio',
    4: 'TwistedFate',
    5: 'XinZhao',
    6: 'Urgot',
    7: 'Leblanc',
    8: 'Vladimir',
    9: 'Fiddlesticks',
    10: 'Kayle',
    11: 'MasterYi',
    12: 'Alistar',
    13: 'Ryze',
    14: 'Sion',
    15: 'Sivir',
    16: 'Soraka',
    17: 'Teemo',
    18: 'Tristana',
    19: 'Warwick',
    20: 'Nunu',
    21: 'MissFortune',
    22: 'Ashe',
    23: 'Tryndamere',
    24: 'Jax',
    25: 'Morgana',
    26: 'Zilean',
    27: 'Singed',
    28: 'Evelynn',
    29: 'Twitch',
    30: 'Karthus',
    31: "Chogath",
    32: 'Amumu',
    33: 'Rammus',
    34: 'Anivia',
    35: 'Shaco',
    36: 'DrMundo',
    37: 'Sona',
    38: 'Kassadin',
    39: 'Irelia',
    40: 'Janna',
    41: 'Gangplank',
    42: 'Corki',
    43: 'Karma',
    44: 'Taric',
    45: 'Veigar',
    48: 'Trundle',
    50: 'Swain',
    51: 'Caitlyn',
    53: 'Blitzcrank',
    54: 'Malphite',
    55: 'Katarina',
    56: 'Nocturne',
    57: 'Maokai',
    58: 'Renekton',
    59: 'JarvanIV',
    60: 'Elise',
    61: 'Orianna',
    62: 'Wukong',
    63: 'Brand',
    64: 'LeeSin',
    67: 'Vayne',
    68: 'Rumble',
    69: 'Cassiopeia',
    72: 'Skarner',
    74: 'Heimerdinger',
    75: 'Nasus',
    76: 'Nidalee',
    77: 'Udyr',
    78: 'Poppy',
    79: 'Gragas',
    80: 'Pantheon',
    81: 'Ezreal',
    82: 'Mordekaiser',
    83: 'Yorick',
    84: 'Akali',
    85: 'Kennen',
    86: 'Garen',
    89: 'Leona',
    90: 'Malzahar',
    91: 'Talon',
    92: 'Riven',
    96: "KogMaw",
    98: 'Shen',
    99: 'Lux',
    101: 'Xerath',
    102: 'Shyvana',
    103: 'Ahri',
    104: 'Graves',
    105: 'Fizz',
    106: 'Volibear',
    107: 'Rengar',
    110: 'Varus',
    111: 'Nautilus',
    112: 'Viktor',
    113: 'Sejuani',
    114: 'Fiora',
    115: 'Ziggs',
    117: 'Lulu',
    119: 'Draven',
    120: 'Hecarim',
    121: "Khazix",
    122: 'Darius',
    126: 'Jayce',
    127: 'Lissandra',
    131: 'Diana',
    133: 'Quinn',
    134: 'Syndra',
    136: 'AurelionSol',
    141: 'Kayn',
    142: 'Zoe',
    143: 'Zyra',
    145: "Kaisa",
    147: "Seraphine",
    150: 'Gnar',
    154: 'Zac',
    157: 'Yasuo',
    161: "Velkoz",
    163: 'Taliyah',
    166: "Akshan",
    164: 'Camille',
    200: "Belveth",
    201: 'Braum',
    202: 'Jhin',
    203: 'Kindred',
    221: 'Zeri',
    222: 'Jinx',
    223: "TahmKench",
    234: 'Viego',
    235: 'Senna',
    236: 'Lucian',
    238: 'Zed',
    240: 'Kled',
    245: 'Ekko',
    246: 'Qiyana',
    254: 'Violet',
    266: 'Aatrox',
    267: 'Nami',
    268: 'Azir',
    350: 'Yuumi',
    360: 'Samira',
    412: 'Thresh',
    420: 'Illaoi',
    421: "RekSai",
    427: 'Ivern',
    429: 'Kalista',
    432: 'Bard',
    497: 'Rakan',
    498: 'Xayah',
    516: 'Ornn',
    517: 'Sylas',
    526: 'Rell',
    518: 'Neeko',
    523: 'Aphelios',
    555: 'Pyke',
    875: "Sett",
    711: "Vex",
    777: "Yone",
    887: "Gwen",
    876: "Lillia",
    888: "Renata",
    895: "Nilah",
    1024: "MonkeyKing",

}


champion_roles = {

    'Sustainable': ['Aatrox', 'Belveth', 'Camille', 'Darius', 'Fiora', 'Gnar', 'Gwen', 'Illaoi', 'Irelia', 'Kayn', 
                    'Leesin', 'Renekton', 'Viego', 'Sylas', 'Sett', 'Swain', 'Hecarim', 'Mordekaiser',
                    'Tryndamere', 'Riven', 'Nasus', 'Jax', 'Yasuo', 'Yone',],
    'Assassin': ['Akali', 'Kassadin', 'Masteryi', 'Rengar', 'Khazix', 'Evelynn', 'Talon', 'Zed', 'Leblanc', 
                 'Nocturne', 'Qiyana', 'Katarina', 'Pyke'],
    'BattleCarry': ['Azir', 'Cassiopeia', 'Lillia',  'Olaf', 'Ryze', 'Violet',  'Viktor',  'Wukong', 
                    'Xinzhao', 'Monkeyking', 'Trundle',  'Gangplank' 'Graves', 'Anivia', 'Heimerdinger', 
                    'Fiddlesticks', 'Kennen', 'Taliyah', 'Vex', 'Aurelionsol', 'Gragas', 'Ahri'],
    'Support': ['Ashe', 'Bard', 'Janna', 'Karma', 'Karthus', 'Lulu', 'Maokai', 'Morgana', 'Nami', 'Orianna',
                'Rakan', 'Renata', 'Senna', 'Seraphine', 'Shaco', 'Sona', 'Soraka', 'Twistedfate', 'Yuumi', 'Zilean',
                'Malzahar', 'Ivern', 'Teemo', 'Yorick', 'Lux', 'Zyra'],
    'HyperCarry': ['Akshan', 'Aphelios', 'Caitlyn', 'Ezreal', 'Jhin', 'Jinx', 'Kaisa', 'Kalista', 'Kayle', 'Kindred', 
                   'Kogmaw', 'Lucian', 'Missfortune', 'Samira', 'Sivir', 'Tristana', 'Twitch', 'Vayne', 'Xayah', 
                   'Zeri', 'Draven', 'Quinn', 'Nilah'],
    'Burst': ['Annie',  'Brand', 'Fizz', 'Ekko', 'Lissandra', 'Nidalee', 'Neeko', 'Nunu', 'Syndra', 'Corki', 
              'Varus', 'Veigar', 'Velkoz', 'Xerath', 'Ziggs', 'Zoe', 'Pantheon', 'Rumble' 'Shyvana', 'Vladimir', 
              'Reksai', 'Diana', 'Jayce', 'Elise'],
    'Tank': ['Alistar', 'Amumu', 'Braum', 'Chogath', 'Drmundo', 'Galio', 'Garen', 'Kled', 'Leona', 'Malphite',
             'Nautilus', 'Ornn', 'Poppy', 'Rammus', 'Rell', 'Sejuani', 'Shen', 'Sion', 'Skarner', 'Tahmkench',
             'Taric', 'Thresh', 'Udyr', 'Urgot', 'Volibear', 'Warwick', 'Zac', 'Blitzcrank', 'Singed', 'Jarvaniv']

}

roles_dict = {

    'Sustainable': ('Aatrox', 'Belveth', 'Camille', 'Darius', 'Fiora', 'Gnar', 'Gwen', 'Illaoi', 'Irelia', 'Kayn', 
                    'Leesin', 'Renekton', 'Viego', 'Sylas', 'Sett', 'Swain', 'Hecarim', 'Mordekaiser', 'Tryndamere', 
                    'Riven', 'Nasus', 'Jax', 'Yasuo', 'Yone', 'Olaf','Violet', 'Wukong', 'Xinzhao', 'Trundle', 'Kled',
                    'Monkeyking', 'Graves'),
    'Assassin': ('Akali', 'Kassadin', 'Masteryi', 'Rengar', 'Khazix', 'Evelynn', 'Talon', 'Zed', 'Leblanc', 'Nocturne', 
                 'Qiyana', 'Katarina', 'Pyke'),
    'BattleCarry': ('Azir', 'Cassiopeia', 'Lillia', 'Ryze', 'Viktor',  'Ekko', 'Gangplank', 'Anivia', 'Heimerdinger', 
                    'Vladimir', 'Fiddlesticks', 'Kennen',  'Aurelionsol', 'Gragas', 'Ahri'),
    'Support': ('Bard', 'Janna', 'Karma', 'Lulu', 'Maokai', 'Morgana', 'Nami', 'Orianna', 'Rakan', 'Renata', 'Senna', 
                 'Seraphine', 'Sona', 'Soraka', 'Twistedfate', 'Yuumi', 'Zilean', 'Ivern',  'Yorick', 'Annie',),
    'HyperCarry': ('Akshan', 'Aphelios', 'Caitlyn', 'Ezreal', 'Jhin', 'Jinx', 'Kaisa', 'Kalista', 'Kayle', 'Kindred', 
                   'Kogmaw', 'Lucian', 'Missfortune', 'Samira', 'Sivir', 'Tristana', 'Twitch', 'Vayne', 'Xayah', 
                   'Zeri', 'Draven', 'Quinn', 'Nilah'),
    'Ranged-mage':('Syndra', 'Velkoz', 'Xerath', 'Ziggs', 'Zoe', 'Corki', 'Ashe', 'Karthus', 'Malzahar', 'Lux', 'Zyra',
                    'Brand', 'Taliyah', 'Vex', 'Shaco', 'Teemo',),
    'Burst': ('Fizz',  'Lissandra', 'Nidalee', 'Neeko', 'Nunu', 'Varus', 'Veigar', 'Pantheon', 'Rumble', 'Shyvana',  
              'Reksai', 'Diana', 'Jayce', 'Elise', 'Malphite',),
    'Tank': ('Alistar', 'Amumu', 'Braum', 'Chogath', 'Drmundo', 'Galio', 'Garen',  'Leona', 'Nautilus', 'Ornn',
             'Poppy', 'Rammus', 'Rell', 'Sejuani', 'Shen', 'Sion', 'Skarner', 'Tahmkench', 'Taric', 'Thresh', 'Udyr', 
             'Urgot', 'Volibear', 'Warwick', 'Zac', 'Blitzcrank', 'Singed', 'Jarvaniv')

}


'''def converting(champ):
    for i in roles_dict.items():
        for s in i[1]:
            if re.findall(champ.lower().capitalize(), s):
                return i[0]
                break'''

def converting(champ):
    for i in champion_roles.items():
        for s in i[1]:
            if re.findall(champ.lower().capitalize(), s):
                # print('done')
                return i[0]
                
                # break

    else:
        print('Not found')

def converting2(champ):
    for i in roles_dict.items():
        for s in i[1]:
            if re.findall(champ.lower().capitalize(), s):
                # print('done')
                return i[0]
                
                # break

    else:
        print('Not found')


def get_champions_name(_id):
    """
    this functions takes an _id and returns the associate champions name
    :param _id: any integer from 1 to 555. if there is a champion, it will return the name.
    :return: champions name
    """

    return all_champion_id.get(_id)


def get_bg_elo(_id):
    
    return all_colors.get(_id)


def get_fg_elo(_id):
    
    return all_fonts_colors.get(_id)
