from getChampionNameByID import all_champion_id
from PIL import ImageChops, Image, ImageGrab
import os
import re
os.system('cls')

def screenshot():
    screen = ImageGrab.grab()
    #saving = Image.open('screenshot_PIL.png')
    screen.save('mcf_aram_lib\\screenshot_PIL.png')

def cut_from_image(num):
    num = str(num)
    im = Image.open(f'chars_collection\\{num}.png')
    
    if im.size == (1366, 768):
        im = im.resize((1920, 1080))
    
    crop_blue = (
        im.crop((31, 159, 70, 198)),
        im.crop((31, 262, 70, 301)),
        im.crop((31, 365, 70, 404)),
        im.crop((31, 468, 70, 507)),
        im.crop((31, 571, 70, 610))
    )

    crop_red = (
        im.crop((1848, 159, 1886, 198)),
        im.crop((1848, 262, 1886, 301)),
        im.crop((1848, 365, 1886, 404)),
        im.crop((1848, 468, 1886, 507)),
        im.crop((1848, 571, 1886, 610))
    )

    for blue in range(0, 5):
        crop_blue[blue].save(f'chars_collection\\crop_blue\\char_{blue}.png')
    for red in range(0, 5):
        crop_red[red].save(f'chars_collection\\crop_red\\char_{red}.png')


def croping_icons(side='main'):

    if side == 'main':
        for i in all_champion_id.values():
            i = i.lower().capitalize()
            if i != 'Wukong':
                if i == 'Violet':
                    i = 'Vi'
                img = Image.open(f'chars\develo_icons_low\{i}.png')
                new_image = img.crop((9, 12, 32, 28))
                new_image.save(f'chars\max_crop\{i}.png')
    else:
        for i in range(0, 5):
            img = Image.open(f'chars_collection\\crop_{side}\\char_{i}.png')
            # new_image = img.crop((10, 10, 29, 24))
            new_image = img.crop((9, 12, 32, 28))
            new_image.save(f'chars_collection\\crop_{side}\\char_{i}.png')
    
def colors_count(main_, secondary_, team):
    return (ImageChops.difference(
        Image.open(f'chars_collection\\crop_{team}\\char_{secondary_}.png'), 
        Image.open(f"chars_collection\\max_crop\\{main_}.png"))).getdata()


def compare_shorts(team):
    print(f'Team: {team}')
    selection = {}
    for i in range(0, 5):
        for char in all_champion_id.values():
            if char != 'Wukong':
                if char == 'Violet':
                    char = 'Vi'
                colors =  colors_count(char, i, team)
                final_value = sum([sum(i) for i in colors])
                if char == 'Kayn_Dark':
                    char = 'Kayn'
                #selection.append(final_value)
                if final_value < 32000:
                    selection[char] = final_value
                    
        # selection.sort()
    
    for x in selection.copy():
        if re.search('_b', x):
            glide = x[:-2]
            if selection[glide] > selection[x]:
                selection[glide] = selection[x]
                selection.pop(x)
            else:
                selection.pop(x)
    
    
    while len(selection) > 5:
        key_del = max(selection, key=lambda k: selection[k])
        del selection[key_del]
    print(selection)
    return list(selection)

def run():
    # screenshot()
    cut_from_image(32)
    croping_icons('blue')
    croping_icons('red')
    blue_team_list = compare_shorts('blue')
    red_team_list = compare_shorts('red')
    return blue_team_list, red_team_list
# screenshot()
run()