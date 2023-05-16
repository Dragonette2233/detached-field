from PIL import Image, ImageChops
from os import system
system('cls')

# way 1
# 1 -- (41, 169, 57, 194) 5 -- (1858, 169, 1874, 194)
# 2 -- (41, 272, 57, 297) 6 -- (1858, 272, 1874, 297)
# 3 -- (41, 375, 57, 400) 7 -- (1858, 375, 1874, 400)
# 4 -- (41, 478, 57, 503) 8 -- (1858, 478, 1874, 503)
# 5 -- (41, 581, 57, 606) 9 -- (1858, 581, 1874, 606)

# way 2
'''im.crop((41, 163, 59, 193)),
        im.crop((41, 266, 59, 296)),
        im.crop((41, 369, 59, 399)),
        im.crop((41, 472, 59, 502)),
        im.crop((41, 575, 59, 610)),
        im.crop((1857, 163, 1874, 193)),
        im.crop((1857, 266, 1874, 296)),
        im.crop((1857, 369, 1874, 399)),
        im.crop((1857, 472, 1874, 502)),
        im.crop((1857, 575, 1874, 605))'''

champs_dict = {
    5: 'XinZhao',
    12: 'Alistar',
    20: 'Nunu',
    21: 'MissFortune',
    22: 'Ashe',
    37: 'Sona',
    43: 'Karma',
    42: 'Corki',
    84: 'Akali',
    86: 'Garen',
    119: 'Draven',
    126: 'Jayce',
    127: 'Lissandra',
    143: 'Zyra',
    266: 'Aatrox',
    498: 'Xayah',
    518: 'Neeko',
    555: 'Pyke',
    777: "Yone",
    7: 'LeBlanc',
    1: 'Annie',
    18: 'Tristana',
    56: 'Nocturne',
    69: 'Cassiopeia',
    80: 'Pantheon',
    81: 'Ezreal',
    157: 'Yasuo',
    45: 'Veigar',
    8: 'Vladimir',
    32: 'Amumu',
    33: 'Rammus',
    15: 'Sivir',
    166: "Akshan",
    245: 'Ekko',
    202: 'Jhin',
    110: 'Varus',
    115: 'Ziggs',
    38: 'Kassadin',
    89: 'Leona',
    76: 'Nidalee',
    96: "KogMaw",
    107: 'Rengar',
    427: 'Ivern',
    876: "Lillia",
    23: 'Tryndamere',
    17: 'Teemo',
    59: 'JarvanIV',
    61: 'Orianna',
    74: 'Heimerdinger',
    82: 'Mordekaiser',
    90: 'Malzahar',
    133: 'Quinn',
    9: 'Fiddlesticks',
    112: 'Viktor',
    120: 'Hecarim',
    99: 'Lux',
    142: 'Zoe',
    161: "VelKoz",
    223: "TahmKench",
    517: 'Sylas',
    526: 'Rell',
    30: 'Karthus',
    35: 'Shaco',
    58: 'Renekton', 
    63: 'Brand',
    103: 'Ahri', 
    222: 'Jinx', 
    234: 'Viego',
    234: 'Viego',
    11: 'MasterYi',
    29: 'Twitch',
    432: 'Bard',
    31: "ChoGath",
    711: "Vex",
    55: 'Katarina',
    113: 'Sejuani',
    75: 'Nasus',
    77: 'Udyr',
    104: 'Graves',
    164: 'Camille',
    203: 'Kindred',
}


def cut_from_image(first, second):
    im = Image.open(f'chars_collection\\main_icons\\{first}.png')
    im2 = Image.open(f'chars_collection\\main_icons\\{second}.png')
    '''im = Image.open(f'{first}.png')
    im2 = Image.open(f'{second}.png')'''
    
    crop_chars = (
        im.crop((41, 163, 59, 193)),
        im.crop((41, 266, 59, 296)),
        im.crop((41, 369, 59, 399)),
        im.crop((41, 472, 59, 502)),
        im.crop((41, 575, 59, 610)),
        im.crop((1857, 163, 1874, 193)),
        im.crop((1857, 266, 1874, 296)),
        im.crop((1857, 369, 1874, 399)),
        im.crop((1857, 472, 1874, 502)),
        im.crop((1857, 575, 1874, 605))
    )
    # from black line -- left 9, up 12, down - 5, right 15

    #good one--
    # crop_left = im.crop((41, 169, 57, 194))
    # crop_right = im2.crop((1858, 375, 1874, 400))
    #good one--
    #crop_left = im.crop((41, 266, 59, 296))
    #crop_right = im2.crop((1857, 369, 1874, 399))

    # print(crop_left.size)
    # print(crop_right.size)

    diff = ImageChops.difference(im, im2)
    # diff.show()
    total_colors = 0
    for i in diff.getdata():
        x = sum(i)
        total_colors += x
    return total_colors

def tuple_creation_single():
    big_set = []
    for i in champs_dict.values():
        final_set = []
        for x in champs_dict.values():
            element = cut_from_image(x.lower().capitalize(), i.lower().capitalize())
            final_set.append(element)
        final_set.sort()
        big_set.append(final_set[1])
    big_set.sort()
    print(big_set)
    print(len(big_set))
    pass

def tuple_creation_all():
    big_set = []
    for i in champs_dict.values():
        final_set = []
        for x in champs_dict.values():
            element = cut_from_image(x.lower().capitalize(), i.lower().capitalize())
            final_set.append(element)
        final_set.sort()
        if final_set[1] > 0 and final_set[1] < 45000:
            print(i, x)
        big_set.append(final_set[1])
    big_set.sort()
    print(big_set)
    print(len(big_set))

def comparing_icons(first):
    big_set = []
    for i in champs_dict.values():
        i = i.lower().capitalize()
        im = Image.open(f'char_{first}.png')
        im2 = Image.open(f'chars_collection\\main_icons\\{i}.png')
        diff = ImageChops.difference(im, im2)
        #diff.show()
        total_colors = 0
        for i in diff.getdata():
            x = sum(i)
            total_colors += x
        big_set.append(total_colors)
    big_set.sort()
    print(big_set)



# tuple_creation_all()
# comparing_icons('5')
# cut_from_image('left_4', 'right_3')
# check_size()
# tuple_creation()