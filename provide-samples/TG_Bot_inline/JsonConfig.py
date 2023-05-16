import json

def jsonInteraction(key=None, value=None, key_2=None, execute=False):

    if not execute:
        json_tweaks = json.load(open('mcf_lib\\GameData.json', 'r'))
        if key_2 is not None:
            json_tweaks[key][key_2] = value
        else:
            json_tweaks[key] = value
        json.dump(json_tweaks, open('mcf_lib\\GameData.json', 'w+'), indent=4)
    else:
        json_tweaks = json.load(open('mcf_lib\\GameData.json', 'r'))
        if key_2 is not None:
            return json_tweaks[key][key_2]
        else:
            return json_tweaks[key]

def jsonDict():
    return json.load(open('mcf_lib\\GameData.json', 'r'))
