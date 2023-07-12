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

newVoiceRate = 145

using_stt = True

def get_user_input(prompt=None,lang:str=None):
    if using_stt:
        with sr.Microphone() as source:
            got_answer= False
            while not got_answer:
                if prompt != None:
                    say(prompt)
                try:
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    if not lang:
                        lang= 'en'
                    answer =  r.recognize_google(r.listen(source),language=lang)

                    got_answer = True

                except sr.UnknownValueError:
                    say("Google Speech Recognition could not understand audio. Please try again.")
                except sr.RequestError as e:
                    say("Could not request results from Google Speech Recognition service; {0}. Please try again".format(e))
    else:
        if prompt != None:
            say(prompt)
        answer = input()
    print("got: "+ answer)
    return answer

def say(text,lang=None):
    if lang:
        engine.setProperty('voice',lang)
    print(text)
    engine.say(text)
    engine.runAndWait()

            
def language_setter(first_language,second_language):
        
    first_lang_name = get_language(first_language)
    second_lang_name = get_language(second_language)
    speech_line = get_user_input("Person A, you can talk:", lang=first_lang_name)

    translator = Translator()

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

    text_to_translate = translator.translate(speech_line,src=first_lang_name,dest=second_lang_name)
    text_o= text_to_translate.text

    say(text_o,lang=second_lang_name)

    res = re.findall(r'\w+', text_o)
    if(res[0]=='end'):
        return 0
    else:
        language_setter( second_language,first_language)


def listen_for_command():
    speech_line=get_user_input("Talk:")
    res = re.findall(r'\w+', speech_line)
    command = res[0]
    match command:
        case "search":
            say("Got that!")
            print(speech_line)
            say(ask_chatgpt(speech_line))
            listen_for_command()
        case "blind":
            print("HI")
        case"emotions":
            a = emotions()
            print(a)
        case "translate":
            langs =[]
            for word in res:
                if get_language(word) != None:
                    langs.append(word)
            if len(langs) <2:
                say("Sorry, I didn't get your languages! Please try again.")
            else:
                say(f"Translating from {langs[0]} to {langs[1]}!")
                language_setter(langs[0], langs[1])
        case _:
            say("Unknown command! please try again.")
            listen_for_command()
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


def main():
    engine.setProperty('voice', "en")
    engine.setProperty('rate', newVoiceRate)
    should_use_stt = input("using vocal commands?(y/n)")
    if should_use_stt == "y":
        using_stt = True
    else:
        using_stt = False
    record_the_speech()
    

if __name__ == "__main__":
    main()
