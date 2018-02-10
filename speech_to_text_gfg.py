#Python 2.x program to transcribe an Audio file
import speech_recognition as sr
 
import pyaudio
import wave
import sys 

from pos_tagging import tokenize
from pos_tagging import pos_tagger
from pos_tagging import chunker 
import keyboard 

def record(): 
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = 5 
	WAVE_OUTPUT_FILENAME = "output.wav"

	if sys.platform == 'darwin':
		CHANNELS = 1

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
		            channels=CHANNELS,
		            rate=RATE,
		            input=True,
		            frames_per_buffer=CHUNK)

	print("* recording")

	# Recording Input
	frames = []
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)
		#if key == keyboard.Key.esc:
		if keyboard.is_pressed('space'): 
			#raw_input() 
			break 

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS) 
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

	AUDIO_FILE = ("output.wav")
	return AUDIO_FILE  

def text():
	try: 
		AUDIO_FILE = record() 
		# use the audio file as the audio source
		r = sr.Recognizer()	
		with sr.AudioFile(AUDIO_FILE) as source:
		#reads the audio file. Here we use record instead of listen 
			audio = r.record(source) 
		text = r.recognize_google(audio) 
		print("The audio file contains: " + text)
		
		return text 
		'''
		root = formtree() 
		user(root, text) 
		'''
		
		'''
		tokens = tokenize(text) 
		tags = pos_tagger(tokens) 
		chunks = chunker(tags)
		chunks.draw()
		print chunks 
		'''
	
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech  Recognition service; {0}".format(e))
		
if __name__ == "__main__": 
	print "Hello LiNi" 
	text()
