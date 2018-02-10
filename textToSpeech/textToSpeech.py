from gtts import gTTS 
import os 
import sys 

sent =  sys.argv[2:] 
sent =  ' '.join(sent) 
name = str(sys.argv[1]) + '.mp3' 
 
tts = gTTS(text=sent, lang='en') 
tts.save(name) 
#os.system("mpg321 hello.mp3") 



'''
import pyttsx
import os
os.system("espeak 'Press 6 for questions on MNP,Postpaid, FixedLine, Broadband, DTH, Change of IVR language & Telephone bill password'")
'''
''' 
engine = pyttsx.init()
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait() 
''' 
