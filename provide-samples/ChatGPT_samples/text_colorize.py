import re

def colorize(text: str):

    text = text.replace('```python', '\033[32m[----Python code----]\033[0m')
    text = text.replace('```', '\033[32m[----Code----]\033[0m')

    matches_functions = re.findall(r'def (.*?)\(', text)
    matches_classes = re.findall(r'class (.*?):', text)
    matches_methods = re.findall(r'\.(.*?)\(', text)

    for f in matches_functions:
        text = text.replace(f, f"\033[32m\033[1m{f}\033[0m")

    for c in matches_classes:
        text = text.replace(c, f"\033[32m\033[1m{c}\033[0m")

    for mt in matches_methods:
        text = text.replace(mt, f"\033[32m\033[1m{mt}\033[0m")

    text = text.replace('def', "\033[36m\033[1mdef\033[0m")
    text = text.replace('class', "\033[36m\033[1mclass\033[0m")
    text = text.replace('self', "\033[33m\033[1mself\033[0m")
    
    for i in '()':
        text = text.replace(i, f"\033[33m{i}\033[0m")

    for r in ('return', 'for ', 'if ', 'elif ', 'else', 
              'match,' 'case', 'while ', '>', '<', '=', 
              '==', '>=', '<=', 'import ', 'from ', 'break'
              'yield', 'try', 'except'):
        text = text.replace(r, f"\033[31m{r}\033[0m")

    start = "\033[02m\033[1m--AI RESPONSE START--\n\033[0m"
    end = "\033[02m\033[1m--AI RESPONSE END--\033[0m"

    return start + text + '\n' + end
