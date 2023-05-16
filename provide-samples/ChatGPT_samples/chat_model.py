import sys
import openai
from text_colorize import colorize

openai.organization = "org-MB9HPIF9vvXS6JqcEosUqMxM"
openai.api_key = sys.argv[1]

while True:
    string_message = input('Request: ')

    if string_message == 'out':
        print('Chat closed.')
        break
    
    print('Response...')

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": string_message}
        ]
        )

    output = colorize(completion.choices[0]['message']['content'])
    print(output)
