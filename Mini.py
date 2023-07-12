import pyttsx3
import time 
import random
def ask_mini():
	
	engine=pyttsx3.init()
	engine.setProperty('rate','6')
	voices=engine.getProperty('voices')
	random_number = random.randint(1, 100)
	print(random_number)
	if random_number%2==0:
		time.sleep(1)
		engine.say("Hey Mini. ")
		time.sleep(1)
		engine.runAndWait()
		engine.say("Can you dance?.")
		engine.runAndWait()
	elif random_number%5==0:
		time.sleep(3)
		engine.say("Hey Mini. ")
		engine.runAndWait()
		time.sleep(3)
		engine.say("What do you think about China.")
		
	elif random_number%2==1:
		time.sleep(1)
		engine.say("Hey Mini.")
		engine.runAndWait()
		time.sleep(1)
		engine.say("Sing little star.")
		engine.runAndWait()

