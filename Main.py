import speech_recognition as sr
import re
import json
import pyttsx3
from googletrans import Translator
import openai
from monodb import emotions
r = sr.Recognizer()
engine=pyttsx3.init()
openai.api_key = "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"
model_engine = "gpt-3.5-turbo"
engine.setProperty('voice',"en")

newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)
def record():
    with sr.Microphone() as source:
            engine.say("TALK")
            engine.runAndWait()
            audio = r.listen(source)
    return audio
            
def language_setter(first_language,second_language):
        
        First=get_language_code(first_language)
        Second=get_language_code(second_language)
        recog1 = sr.Recognizer()
        mc = sr.Microphone()
        with mc as source:
                recog1.adjust_for_ambient_noise(source, duration=0.2)
                audio = recog1.listen(source)
                get_sentence = recog1.recognize_google(audio,language=str(First))
                translator = Translator()
                print(get_sentence)
                print(First)
                print(Second)
                engine.setProperty('voice',Second)
                text_to_translate = translator.translate(get_sentence,src=First,dest=Second)
                text_o= text_to_translate.text
                voices=engine.getProperty('voices')
                engine.say(text_o)
                engine.runAndWait()
                res = re.findall(r'\w+', text_o)
                number_of_the_vector=len(res)
                if(res[0]=='end'):
                    return 0;
                else:
                    language_setter( second_language,first_language)
                        
def record_the_speech():
        
        audio=record()

        
        try:
                your_words_is=r.recognize_google(audio)
                res = re.findall(r'\w+', your_words_is)
                print(res[0])
                if res[0]=="search":
                    
                    engine.say("Got that")
                    engine.runAndWait()
                    print(your_words_is)
                    print(ask_chatgpt(your_words_is))
                    anwort=ask_chatgpt(your_words_is)
                    record_the_speech()
                   #engine.setProperty('voice',Second)
                    

                    engine.say(anwort)
                    engine.runAndWait()
                elif res[0]=="blind":
                    print("HI")
                elif res[0]=="emotions":
                    a=emotions()
                    print(a)
                else:
                    engine.say("Now you can talk")
                    engine.runAndWait()
                    print(res[0],res[1])
                    language_setter(res[0],res[1])
        except sr.UnknownValueError:
                engine.say("Google Speech Recognition could not understand audio")
                record_the_speech()
        except sr.RequestError as e:
                engine.say("Could not request results from Google Speech Recognition service; {0}".format(e))
                record_the_speech()
def ask_chatgpt(question):
    print(question)
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        n=1,
         messages=[
            {"role": "system", "content": "You are a helpful assistant with exciting, interesting things to say."},
             {"role": "user", "content": question},
        ])
    message = response.choices[0]['message']
    return message['content']


supported_languages_info = json.load(open('supported_languages.json'))['text']


def get_language_code(language_name):
    for language in supported_languages_info:
        if language['language'].lower() == language_name.lower():
            return language['code']
    return None


record_the_speech()
    
