from IPython.display import Image, display

#reasoning
from openai import OpenAI
from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv(),override=True)
os.getenv('OPENAI_API_KEY')
client=OpenAI()
def ask_ai(prompt):
    response=client.chat.completions.create(
        model='o3-mini',
        reasoning_effort='medium',
        messages=[
            {'role':'user','content':prompt}
        ],
    )

    return response.choices[0].message.content

q=input('what do you want to ask? ')
print(ask_ai(q))
#reacting for images
import base64
# img_pt=r'C:\Users\thota\Downloads\ChatGPT Image Jul 13, 2025, 05_20_04 PM.png'
def encode_image(img_path):
    with open(img_path,'rb') as fi:
        img_bdt=fi.read()
        return base64.b64encode(img_bdt).decode("utf-8")

base64_img=encode_image(image)
sys_message='you are image explainer'
prompt='this boy is saying hi to u'
response=client.chat.completions.create(
    model='gpt-4o',
    messages=[
    {'role':'system','content':sys_message},
    {'role':'user','content':[
        {'type':'text','text':prompt},
        {'type':'image_url','image_url':{
            'url':f'data:image/png;base64,{base64_img}'
        }}
    ]}
    ],
    temperature=0.0
)
print(response.choices[0].message.content)
#converting audio to text
file=r"C:\Users\thota\OneDrive\Pictures\Camera Roll\WIN_20250714_15_45_57_Pro.mp4"
with open(file,'rb') as fi:
    transcript=client.audio.transcriptions.create(
        model='whisper-1',
        file=fi
    )
    print(transcript.text)
#translating voice
file=r"C:\Users\thota\Videos\Screen Recordings\Screen Recording 2025-07-14 162720.mp4"
with open(file,'rb') as fi:
    translate=client.audio.translations.create(
        model='whisper-1',
        file=fi
    )
    print(translate.text)
#text to audio
text='hey hi! how are you? I am your hlepfull assistant.approach me without any fear and I will try to clarify all your doubts  meow meow meow'
with client.audio.speech.with_streaming_response.create(
    model='tts-1',
    voice='alloy',
    input=text
) as response:
    with open('tts2.mp3','wb') as f:
        for chunk in response.iter_bytes():
            f.write(chunk)
#creating images
prompt='create an image of an lonely sad dog roming city in rain with depression?'
response=client.images.generate(
    model='dall-e-3',
    prompt=prompt,
    style='vivid',
    size='1024x1024',
    quality='standard',
    n=1
)

img_url=response.data[0].url
print(img_url)