import requests
import json
from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv(),override=True)



# response=requests.get(url)
#
# print(response.headers)
# print(response.text)
# print(response.json())


try:
    url = 'https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m'
    response = requests.get(url,timeout=5)
    response.raise_for_status()
    # print(json.dumps(response.json(),indent=4))
except requests.exceptions.RequestException as e:
    print(f'RequestException: {e}')


api_key=os.getenv('OPENAI_API_KEY')
url='https://api.openai.com/v1/chat/completions'
headers={
    'Authorization':f'Bearer {api_key}',
    'Content-Type':'application/json'
}

data={
    'model':'gpt-4o-mini',
    'messages':[
    {'role':'system','content':'your helpful assistant'},
    {'role':'user','content':input('enter your question: ')}
],
'temperature':0.8
}

respnose=requests.post(url,headers=headers,json=data)
try:
    respnose.raise_for_status()
    reply=respnose.json()['choices'][0]['message']['content']
    print(reply)
except requests.exceptions.HTTPError as he:
    print(f'an HTTP error occurred: {he}')
except Exception as e:
    print(f'an unexpected error occurred: {e}')