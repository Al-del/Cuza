import speech_recognition as sr
import re
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
def get_language(language) -> str:
    if language=="Afrikaans":
       return "af"
    if language=="Arabic":
       return "ar"
    if language=="Bengali":
       return "bn"
    if language=="Bulgarian":
       return "bg"
    if language=="Mandarin":
       return "zh"
    if language=="Greek":
       return "el"
    if language=="Danish":
       return "da"
    if language=="Dutch":
       return "nl"
    if language=="English":
       return "en"
    if language=="Estonian":
       return "et"
    if language=="Filipino":
       return "fil"
    if language=="Finnish":
       return "fi"
    if language=="French":
       return "fr"
    if language=="Galician":
       return "gl"
    if language=="Georgian":
       return "ka"
    if language=="German":
       return "de"
    if language=="Gujarati":
       return "gu"
    if language=="French":
       return "fr"
    if language=="Hebrew":
       return "iw"
    if language=="Hindi":
       return "hi"
    if language=="Hungarian":
       return "hu"
    if language=="Icelandic":
       return "is"
    if language=="Indonesian":
       return "id"
    if language=="Italian":
       return "it"
    if language=="Japanese":
       return "ja"
    if language=="Javanese":
       return "jv"
    if language=="Kannada":
       return "kn"
    if language=="Kazakh":
       return "kk"
    if language=="Khmer":
       return "km"
    if language=="Korean":
       return "ko"
    if language=="Lao":
       return "lo"
    if language=="Latvian":
       return "lv"
    if language=="Lithuanian":
       return "lt"
    if language=="Macedonian":
       return "mk"
    if language=="Malay":
       return "ms"
    if language=="Marathi":
       return "mr"
    if language=="Mongolian":
       return "mn"
    if language=="Nepali":
       return "ne"
    if language=="Norwegian":
       return "no"
    if language=="Persian":
       return "fa"
    if language=="Polish":
       return "pl"
    if language=="Portuguese":
       return "pt"
    if language=="Punjabi":
       return "pa"
    if language=="Romanian":
       return "ro"
    if language=="Russian":
       return "ru"
    if language=="Serbian":
       return "sr"
    if language=="Sinhala":
       return "si"
    if language=="Slovak":
       return "sk"
    if language=="Spanish":
       return "es"
    if language=="Sundanese":
       return "su"
    if language=="Swahili":
       return "sw"
    if language=="Swedish":
       return "sv"
    if language=="Tamil":
       return "ta"
    if language=="Telugu":
       return "te"
    if language=="Thai":
       return "th"
    if language=="Turkish":
       return "tr"
    if language=="Ukrainian":
       return "uk"
    if language=="Urdu":
       return "ur"
    if language=="Vietnamese":
       return "vi"

should_use_stt = input("using vocal commands?(y/n)")
if should_use_stt == "y":
    using_stt = True
else:
    using_stt = False

listen_for_command()
    
