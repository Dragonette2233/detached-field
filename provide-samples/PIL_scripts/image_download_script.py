import requests
import os
from getChampionNameByID import all_champion_id
import re
os.system('cls')

# link - http://ddragon.leagueoflegends.com/cdn/12.18.1/img/champion/Aatrox.png

def download():

    for i in all_champion_id.values():
        if i == 'Violet':
            i = 'Vi'
        p = requests.get(f'http://ddragon.leagueoflegends.com/cdn/12.18.1/img/champion/{i}.png')
        out = open(f'chars\develo_icons\{i}.png', 'wb')
        out.write(p.content)
        out.close()
        print(f'{i} downloaded')

for i in all_champion_id.values():
    open('champions_list.txt', 'a+').writelines(i + '\n')