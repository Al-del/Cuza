import speech_recognition as sr
import re
import pyttsx3
from googletrans import Translator
import openai
from monodb import emotions


## Constants
r = sr.Recognizer()
engine = pyttsx3.init()
openai.api_key = "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"
model_engine = "gpt-3.5-turbo"
newVoiceRate = 145

def record():
    with sr.Microphone() as source:
            engine.say("TALK")
            engine.runAndWait()
            audio = r.listen(source)
    return audio
            
def language_setter(first_language,second_language):
        
        First=get_language(first_language)
        Second=get_language(second_language)
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
                    reord_the_speech()
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
def get_language(language):
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


def main():
    engine.setProperty('voice', "en")
    engine.setProperty('rate', newVoiceRate)
    record_the_speech()


if __name__ == "__main__":
    main()
