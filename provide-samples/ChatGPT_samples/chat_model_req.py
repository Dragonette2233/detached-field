import requests
import json

url = 'https://api.openai.com/v1/chat/completions'

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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",
    "OpenAI-Organization": "org-MB9HPIF9vvXS6JqcEosUqMxM"
}

data = '''{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "OpenAI расскажи шутку"}],
     "temperature": 0.7
   }'''

result = requests.post(url=url, headers=headers, data=data.encode('utf-8'))
# print(result.json())

print(result.json()['choices'][0]['message']['content'])