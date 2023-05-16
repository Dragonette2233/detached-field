from PIL import Image, ImageChops
from getChampionNameByID import all_champion_id
import os
import numpy
import math

# http://ddragon.leagueoflegends.com/cdn/13.6.1/img/champion/Aatrox.png

os.system('cls')

# Coordinates
# 1 -- 31/158 | 70/197 # 6 -- 1847/158 | 1886/197
# 2 -- 31/261 | 70/300 # 7 -- 1847/261 | 1886/300
# 3 -- 31/364 | 70/403 # 8 -- 1847/364 | 1886/403
# 4 -- 31/467 | 70/506 # 9 -- 1847/467 | 1886/510
# 5 -- 31/570 | 70/609 # 0 -- 1847/570 | 1886/613

# temp crop 10, 10 | 29, 24

'''def calcdiff(im1, im2):
    dif = ImageChops.difference(im1, im2)
    return numpy.mean(np.array(dif))'''

# Image.open('chars\\develo_icons_low\\Pyk2e.png').show()

def temp_crop(side='none', single='none'):

    if side == 'main':
        for i in all_champion_id.values():
            if i != 'Wukong':
                if i == 'Violet':
                    i = 'Vi'
    elif single == 'single':
        img = Image.open(f'chars\develo_icons_low\Tryndamere.png')
        new_image = img.crop((10, 12, 33, 28))
        new_image.save(f'chars\max_crop\Tryndamere2.png')
    else:
        for i in range(0, 5):
            img = Image.open(f'chars\\{side}\\char_{i}.png')
            # new_image = img.crop((10, 10, 29, 24))
            new_image = img.crop((8, 12, 31, 28))
            new_image.save(f'chars\\{side}\\char_{i}.png')

def resize_icons():
    # champions_list = tuple(open('new_list.txt', 'r').read().split('\n'))
    # for i in champions_list:
    img = Image.open(f'chars\\develo_icons\\Milio.png')
    # new_image = img.crop((3, 0, 16, 34))
    # new_image = img.resize((38, 38))
    new_image = img.resize((19, 20))
    new_image.save(f'chars\develo_38\Milio_2.png')


def differense(char, mains, show='0'):
    im1 = Image.open(f"char_{char}.png")
    im2 = Image.open(f"chars_collection\\new_crop\\red_l\{mains}.png")
    
    diff = ImageChops.difference(im1, im2)
    if show != '0':
        diff.show()
    # print(len(diff.getdata()))
    total_colors = 0
    for i in diff.getdata():
        x = sum(i)
        total_colors += x
    print(total_colors)

def cut_elo():

    elo_t = ('Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Master', 'Grandmaster', 'Challenger', 'Iron')

    for i in elo_t:
        im = Image.open(f'ranked-emblems\\Emblem_{i}.png')
        im2 = im.resize((70, 70))
        im2.save(f'{i}.png')

def cut_screen():
    # cut - 668, 43, 2421, 1516
    im = Image.open('ProjectVayne.jpg')
    crop = im.crop((668, 43, 2421, 1516))
    crop2 = crop.resize((500, 420))
    # crop = im.resize((500, 400))
    crop2.save('CustomVayne.png')

def cut_from_image(val):
    val = str(val)
    im = Image.open(f'chars_collection\\{val}.png')
    # way 1
# 1 -- (42, 160, 68, 195) 5 -- (1851, 160, 1874, 195)
# 2 -- (42, 263, 68, 298) 6 -- (1851, 263, 1874, 298)
# 3 -- (42, 366, 68, 401) 7 -- (1851, 366, 1874, 401)
# 4 -- (42, 469, 68, 504) 8 -- (1851, 478, 1874, 504)
# 5 -- (42, 572, 68, 607) 9 -- (1851, 572, 1874, 607)
    crop_blue = (
        im.crop((42, 160, 68, 195)),
        im.crop((42, 263, 68, 298)),
        im.crop((42, 366, 68, 401)),
        im.crop((42, 469, 68, 504)),
        im.crop((42, 572, 68, 607)),
    )

    crop_red = (
        im.crop((1851, 160, 1874, 195)),
        im.crop((1851, 263, 1874, 298)),
        im.crop((1851, 366, 1874, 401)),
        im.crop((1851, 469, 1874, 504)),
        im.crop((1851, 572, 1874, 607))
    )

    
    for blue in range(0, len(crop_blue)):
        crop_blue[blue].save(f'chars_collection\\crop_blue\char_{blue}.png')
    for red in range(0, len(crop_red)):
        crop_red[red].save(f'chars_collection\\crop_red\char_{red}.png')
    
def rename_imgs():
    for i in range(1, 19):
        im = Image.open(f'gifs_library\\Слой {i}.png')
        im.save(f'gifs_renamed\\load_{i}.png')

def convertOne():

    img = Image.open('Di.png')
    print(img.getdata())
    # cells = ImageChops.
    
    img.save('di_APP.webp')


# convertOne()
# rename_imgs()
# print(x)
# cut_elo()
# cut_screen()
# cut_from_image(109)
# differense('3', 'Kayle', show=1)
resize_icons()
# temp_crop(single='single')
# temp_crop(side='blue')