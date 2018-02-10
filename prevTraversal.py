from speech_to_text_gfg import text
import string
import csv
from operator import add
import ast 
import fileinput 
from gtts import gTTS 
from playsound import playsound 
import warnings 

warnings.filterwarnings("ignore") 

class Frequency(object): 
	
	def __init__(self,n):
		self.f = []
        
	def init_to_zero(self, n): 
		for i in range(n): 
			self.f.append(0) 
	def increment(self, node): 
		self.f[node] = self.f[node] + 1 
				
f = Frequency(26) 

class Tree(object):
	counter=-1
	overallFreq=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	def __init__(self,taskName):
		self.childList=[]
		self.task=taskName
		self.past=0
		self.freq=0
		Tree.counter=Tree.counter+1
		self.index=Tree.counter
    #Take userNode and check in childList and returns 
    # childnode if node found 
    # None if node not found
    # None if leaf node found


'''
def write_data(number, path, freq): 
	flag = 0 
	with open('file.csv', 'rb') as csvfile: 
		#reader = csv.DictReader(csvfile)
		reader = csv.reader(csvfile, delimiter=',') 
		for row in reader: 
			#bits = row.spilt(',') 
			if(row[0] == number): 
				row[1] = path
				row[2] = map(add, row[2], freq) 
			with open('file.csv', 'a') as csvfile: 
				writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL) 
				writer.writerow(','.join(row)) 
			flag = 1 
			break

	if(flag==0): 
		with open('file.csv', 'a') as csvfile: 
			writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL) 
			writer.writerow([number, path, freq]) 
			#writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam']) 
'''

'''
def write_frequency(path): 
	for i in path: 
		for line in fileinput.FileInput("freq_file.csv",inplace=1):
			if str.lower(str(i).strip()) in line:
				update = ast.literal_eval(line) 
				line=line.replace(str(update[1]),str(update[1]+1)) 
			print line, 
	
'''
def read_freq():
	with open('file1.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			overallfreq=row
	return overallfreq
def write_freq(overallfreq):
	with open('file1.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(overallfreq)
def write_data(number, path, freq, shortcode): 
	updaterow = [] 
	updaterow = read_data(number) 
	update = [] 
	#print updaterow 
	
	# if(len(updaterow)!=0): 
	# 	update = ast.literal_eval(updaterow[2])
	# 	#print update 
	# 	update =  map(add, update, freq) 
	# 	freq = update 	
	with open('file.csv', 'a') as csvfile: 
		writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL) 
		writer.writerow([number, path, freq, "1"]) 
		#writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam']) 
		


def read_data(number): 
	with open('file.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		last_call = [] 
		for row in reader:
			if (row[0] == str(number)): 
				last_call = row 
	return last_call

def traverse(tree, task): 
	tree.past = 1 
	if len(tree.childList)==0: 
		return None  
	for child in tree.childList: 
		if child.task==task: 
			child.past = 1 
			return child 
	return None

def getChildwithIndex(node,option):
	for i in range(len(node.childList)):
		#print "opt",option
		#print "i",i+1 
		#print option 
		#print type(option) 
		
		if str(option)==str(i+1):
			return node.childList[i] 
	 
	return None 
def printChildren(arr): 
	lst = [] 
	for i in arr: 
		lst.append(i.task)
		print i.task
	return lst  

def speakChildren(arr): 
	#sent = ' '.join(arr) 
	for i in arr: 
		#print  
		speak(i) 

def speak(sent): 
	tts = gTTS(text=sent, lang='en') 
	tts.save('speak.mp3') 
	playsound('speak.mp3') 


path = [] 
def user(root, prevPath,freq,overallfreq): 
	if (root == None): 
		return None 
	
	if len(root.childList)==0: 
		return None 
	
	if (len(prevPath) != 0): 
		for i in prevPath: 
			if len(root.childList)==0: 
				break 	
			inp = i 
			inp = str(inp) 
			#print i
			path.append(inp) 
			ch=getChildwithIndex(root,inp) 
			index=ch.index
			#print index
			child = takeUserinput(root,str(index),freq,overallfreq) 
			#print "Hellooooooooooooooooooooo ", inp
			if (child != None): 
				print child.task, "\tDone " 	
			else: 
				print "Option Unavailable" 
			user(child,prevPath[1:],freq,overallfreq) 
			return path 
	else: 	
		lst = printChildren(root.childList) 
		#print "Helloooooooooooooooooooo ", str(lst)
		speakChildren(lst)

		#inp = raw_input("Enter Next Task: " + " : ") 

		while(1): 
			inp = text() 

			#inp = inp.strip()  
			
			#print "hi: ", path
			#print "Type: ", type(inp)
			ch=getChildwithIndex(root,inp) 
			#print "hello ch ", ch 
			if(ch != None): 
				break 
			speak("Please repeat") 

		path.append(inp) 
	
		index=ch.index
		child = takeUserinput(root,str(index),freq,overallfreq) 
	

		#print "Hellooooooooooooooooooooo "
		if (child != None): 
			print child.task, "\tDone " 
		else: 
			print "Option Unavailable"
			path.pop() 
	
		if (child == None): 
			return None 
	
		if len(child.childList)==0: 
			return None 

		user(child,[],freq,overallfreq)  
		return path

'''
def user(root): 
	while(len(root.childList)!=0): 
		inp = raw_input("Enter Task: ") 
		child = takeUserinput(root, inp) 
		print child.task, "Done "  
'''
path=[]
def repeatMaxTask(userNode,freq,overallfreq):
	if userNode==None: 
		return None 
	maximum=0
	node=userNode
	if len(node.childList)==0:
			return None
	count=0
	nodeindex=0
	for child in node.childList: 
		#print child.index
		count=count+1
		if overallfreq[child.index]>maximum:
			maximum=overallfreq[child.index]
			nodeindex=count
			node=child
	path.append(str(nodeindex))
	freq[node.index]=freq[node.index]+1
	overallfreq[node.index]=overallfreq[node.index]+1
	print "Task: ", node.task, "done" 
	repeatMaxTask(node,freq,overallfreq)
	return path

def takeUserinput(userNode,userTask,freq,overallfreq): 
	userTask = str.lower(userTask) 
	#userNode.past = 1
	node=userNode
	#print node.task
	#print userTask
	flag = 0 
	if(node!=None): 
		if len(node.childList)==0:
			#print "check1"
			return None
		for child in node.childList:
			#print child.index
			if int(userTask) ==child.index:
			#if str.lower(child.task.strip())==userTask:
				#child.past=1
				#child.freq = child.freq + 1
				#print userTask 
				freq[child.index]=freq[child.index]+1
				overallfreq[child.index]=overallfreq[child.index]+1
				flag = 1 
				ans1=child 
			else: 
				#print "check2"
				ans = None  
	if flag==1:
		return ans1
	else:
		return ans

def repeatTask(node): 
	if node==None: 
		return 
	for child in node.childList: 
		#print child.data 
		if child.past==1:  
			print "Task: ", child.task, "  Freq: ", child.freq, "Past: ", child.past  
			repeatTask(child) 
	return None 
	
def formtree(): 
	
	root = Tree("Airtel") #1 
	
	root.childList.append(Tree("Press 1 for For Special Call Rates and Full talk Time rates")) 
	root.childList.append(Tree("Press 2 for Hello Tunes and Value Added Services")) 
	root.childList.append(Tree("Press 3 to know your mobile validity, reasons for balance deduction")) 
	root.childList.append(Tree("Press 4 for Airtel Money")) 
	root.childList.append(Tree("Press 5 for Information on Data Services like Three G,Mobile, Internet, Dongle, Blackberry")) 
	root.childList.append(Tree("Press 6 for questions on MNP,Postpaid, FixedLine, Broadband, DTH, Change of IVR language & Telephone bill password")) 
	
	
	#2.mp3 
	root.childList[0].childList.append(Tree("Specialised offers for you. Press 1 to exit. ")) 
	#root.childList[0].childList[0].childList.append(Tree(None))

	#3.mp3 
	root.childList[1].childList.append(Tree("Press 1 for Hello Tunes")) 
	root.childList[1].childList.append(Tree("Press 2 To start any other Value Added Service")) 
	root.childList[1].childList.append(Tree("Press 3 To stop a Value Added Service")) 
	root.childList[1].childList.append(Tree("Press 4 To receive a text on how to start/stop a VAS")) 

	#4.mp3 
	root.childList[2].childList.append(Tree("Press 1 to know your Mobile Balance and Validity")) 
	root.childList[2].childList.append(Tree("Press 2 for details on balance deduction")) 
	root.childList[2].childList.append(Tree("Press 3 for information on special 5")) 

	#5.mp3 
	root.childList[3].childList.append(Tree("Press 1 For information on Airtel Money")) 
	root.childList[3].childList.append(Tree("Press 2 if you are an aitel money customer")) 

	#6.mp3 	
	root.childList[4].childList.append(Tree("Press 1 to start Three G, Mobile Internet & blackberry & Data Plan Change")) 
	root.childList[4].childList.append(Tree("Press 2 to stop Three G, Mobile Internet & blackberry ")) 
	root.childList[4].childList.append(Tree("Press 3 to get settings of Three G, Mobile Internet & MMS ")) 
	root.childList[4].childList.append(Tree("Press 4 for information on Data card or Dongle details")) 
	root.childList[4].childList.append(Tree("Press 5 for information on PC connectivity procedure")) 
	root.childList[4].childList.append(Tree("Press 6 for questions & technical help on Three G, Mobile Internet & Blackberry")) 

	#7.mp3 	
	root.childList[1].childList[0].childList.append(Tree("Press 1 to start Hello Tunes")) 
	root.childList[1].childList[0].childList.append(Tree("Press 2 to stop Hello Tunes")) 

	#8.mp3
	root.childList[1].childList[1].childList.append(Tree("Press 1 for Astrolgy on Demand")) 
	root.childList[1].childList[1].childList.append(Tree("Press 2 for Airtel Talkies")) 
	root.childList[1].childList[1].childList.append(Tree("Press 3 for Hello tunes")) 
	root.childList[1].childList[1].childList.append(Tree("Press 4 for Missed Call Alerts")) 
	root.childList[1].childList[1].childList.append(Tree("Press 5 for Job Alerts")) 
	root.childList[1].childList[1].childList.append(Tree("Press 6 for information on more services")) 

	#9.mp3 
	root.childList[1].childList[2].childList.append(Tree("No Value Added Service has been started on your number")) 

	#10.mp3	
	root.childList[1].childList[3].childList.append(Tree("Thank you! details will be shared soon via sms. Press 1 to exit ")) 

	#11.mp3 
	root.childList[2].childList[0].childList.append(Tree("Thank you! You will get this information via sms. Press 1 to exit ")) 

	#12.mp3 
	root.childList[2].childList[1].childList.append(Tree("Press 1 for last 5 VAS Debits ")) 
	root.childList[2].childList[1].childList.append(Tree("Press 2 for last 5 Voice call debits ")) 
	root.childList[2].childList[1].childList.append(Tree("Press 3 for last 5 outgoing sms/mms debits ")) 
	root.childList[2].childList[1].childList.append(Tree("Press 4 for lst 5 Mobile Internet usage details ")) 

	#13.mp3 	
	root.childList[2].childList[2].childList.append(Tree("Thank you! You will receive this information via sms. Press 1 to exit ")) 

	#14.mp3 
	root.childList[3].childList[0].childList.append(Tree("Press 1 for knowing what is Airtel Money")) 
	root.childList[3].childList[0].childList.append(Tree("Press 2 for informationon on how to become Airtel Money customer")) 
	root.childList[3].childList[0].childList.append(Tree("Press 3 to know about airtel money offers and terms and conditions ")) 

	#15.mp3 	
	root.childList[3].childList[1].childList.append(Tree("Press 1 if you know your MPIN  ")) 
	root.childList[3].childList[1].childList.append(Tree("Press 2 if you forgot your MPIN  ")) 

	#16.mp3 
	root.childList[4].childList[0].childList.append(Tree("Press 1 to start Three G services ")) 
	root.childList[4].childList[0].childList.append(Tree("Press 2 to start Mobile Internet Services  ")) 
	root.childList[4].childList[0].childList.append(Tree("Press 3 to start Blackberry Services ")) 

	#17.mp3 	
	root.childList[4].childList[1].childList.append(Tree("Press 1 to stop Three G services ")) 
	root.childList[4].childList[1].childList.append(Tree("Press 2 to stop mobile internet services  ")) 
	root.childList[4].childList[1].childList.append(Tree("Press 3 to stop balckeberry services ")) 
	
	#18.mp3 
	root.childList[4].childList[2].childList.append(Tree("Press 1 to get settings for Three G or Mobile Internet ")) 
	root.childList[4].childList[2].childList.append(Tree("Press 2 to get settings for MMS ")) 

	#19.mp3 	
	root.childList[4].childList[3].childList.append(Tree("Press 1  for information on Installation Procedure ")) 
	root.childList[4].childList[3].childList.append(Tree("Press 2 talking to executive ")) 

	#20.mp3 	
	root.childList[4].childList[4].childList.append(Tree("Press 1  for information on how to connect PC through bluetooth")) 
	root.childList[4].childList[4].childList.append(Tree("Press 2 for information on how to connect PC through infrared  ")) 
	root.childList[4].childList[4].childList.append(Tree("Press 3 for information on how to connect PC through cable ")) 

	#21.mp3 
	root.childList[4].childList[5].childList.append(Tree("Press 1 for any questions ")) 
	root.childList[4].childList[5].childList.append(Tree("Press 2 for technical help on mobile internet and blackberry ")) 

	#22.mp3 
	root.childList[4].childList[3].childList[0].childList.append(Tree("Press 1 for information on how to install data card or Dongle with Windows Operatiog System ")) 
	root.childList[4].childList[3].childList[0].childList.append(Tree("Press 2 for information on how to install data card or Dongle with Linux Operating System ")) 
	root.childList[4].childList[3].childList[0].childList.append(Tree("Press 3 for information on how to install data card or Dongle with Mac Book ")) 
	root.childList[4].childList[3].childList[0].childList.append(Tree("Press 4 for information on how to install data card or Dongle with Mac Book Pro ")) 

	'''	
	root = Tree("ABCD")
	
	root.childList.append(Tree("press 1 for check balance"))
	root.childList.append(Tree("press 2 for enquiry"))
	
	root.childList[0].childList.append(Tree("press 1 for talk to person"))
	root.childList[0].childList.append(Tree("press 2 for menu again"))
	root.childList[1].childList.append(Tree("E"))
	root.childList[1].childList.append(Tree("F"))

	root.childList[0].childList[0].childList.append(Tree("repeat current menu"))
	root.childList[0].childList[0].childList.append(Tree("H"))
	root.childList[0].childList[1].childList.append(Tree("I"))
	root.childList[0].childList[1].childList.append(Tree("J"))
	root.childList[1].childList[0].childList.append(Tree("K"))
	root.childList[1].childList[0].childList.append(Tree("L"))
	root.childList[1].childList[1].childList.append(Tree("M"))
	root.childList[1].childList[1].childList.append(Tree("N"))
	root.childList[1].childList[1].childList.append(Tree("O"))

	root.childList[0].childList[1].childList[0].childList.append(Tree("P"))
	root.childList[0].childList[1].childList[0].childList.append(Tree("Q")) 
	root.childList[0].childList[1].childList[0].childList[0].childList.append(Tree("R")) 
	root.childList[0].childList[1].childList[0].childList[1].childList.append(Tree("S")) 
	root.childList[1].childList[1].childList[1].childList.append(Tree("T")) 
	root.childList[1].childList[1].childList[1].childList.append(Tree("U")) 
	root.childList[1].childList[1].childList[1].childList[0].childList.append(Tree("V")) 
	root.childList[1].childList[1].childList[1].childList[0].childList.append(Tree("Z")) 
	root.childList[1].childList[1].childList[1].childList[1].childList.append(Tree("W")) 
	root.childList[1].childList[1].childList[1].childList[1].childList.append(Tree("X")) 
	root.childList[1].childList[1].childList[1].childList[1].childList[0].childList.append(Tree("Y")) 
	'''
	
	'''
	root = Tree("hello creator")
	# root.left = Tree()
	# root.left.data = "left"
	# root.right = Tree()
	# root.right.data = "right"
	
	# Tree 
	root.childList.append(Tree("hello man"))
	root.childList.append(Tree("hello woman"))
	root.childList[0].childList.append(Tree("hello boy"))
	root.childList[0].childList.append(Tree("hello girl"))
	root.childList[0].childList[1].childList.append(Tree("hello kid"))
	root.past = 1
	'''
	return root 
def printShortcodes(prevPaths):
	for i in range(len(prevPaths)):
		print i+1,":",prevPaths.items()[i]
def test():

	tree = formtree()
	root = tree  
	'''
	node = Tree("")
	node = takeUserinput(root, "task 2")
	if (node!=None):
		print "Test Case: ", node.task 
	else: 
		print "Option Unavailable" 
	'''
	#takeUserinput(root.childList[0],"Task 5")
	#takeUserinput(root.childList[0].childList[1],"Task 6") 
	number = raw_input("Phone Number: ") 
	while(len(number)!=10):
		speak("Invalid Number. Enter again.") 
		number = raw_input("Phone Number: ") 
	freq=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
	f.init_to_zero(26) 
	last_call = [] 
	prevPaths=dict()
	prevPath = [] 
	last_call = read_data(number) 
	overallfreq=ast.literal_eval(read_freq()[0])
	#print overallfreq
	if(len(last_call)!=0): 
		prevPaths = ast.literal_eval(last_call[1])
		freq= ast.literal_eval(last_call[2])
	#print prevPath
	newpath = []
	
	if(last_call and last_call[3] == "1"): 
		speak("Do you want to run your short code ? Press  (y/n): ")
		short = raw_input("Do you want to run your short codes ? Press (y/n): ") 
		
		if(str.lower(short.strip()) == 'y'): 
			printShortcodes(prevPaths)
			#option=raw_input("Which one would you like to select?")
			speak("Which one would you like to select?") 
			option = text() 
			while (str(option) not in prevPaths.keys()): 
				speak("Please repeat") 
				option = text() 
			
			option = str.lower(str(option.strip())) 
			prevPath=prevPaths[option]
			newpath = user(root,prevPath,freq,overallfreq) 
		else: 
			speak("Do you want to hit the most frequent topic ? Press (y/n): ")
			globalshort = raw_input("Do you want to hit the most frequent topic ? Press (y/n): ") 
			if(str.lower(globalshort.strip())=='y'): 
				newpath=repeatMaxTask(root,freq,overallfreq) 
				speak("Do you want to save this as your shortcode ? Press (y/n): ")
				shortcode = raw_input("Do you want to save this as your shortcode ? Press (y/n): ") 
				if(str.lower(shortcode.strip()) == 'y'): 
					if newpath not in prevPaths.values():
						speak("How would you like to save it? ")
						print "How would you like to save it: " 
						key = text() 
						#key = raw_input("How would you like to save it: ") 
						prevPaths[key]=newpath
						write_data(number, prevPaths, freq,str.lower(shortcode.strip())) 
			else:
				newpath = user(root,[],freq,overallfreq) 
				print "Path taken this time: ", newpath
				#print "Hellooooooooooooooooooooo newpath", newpath, prevPath 
				speak("Do you want to save this as your shortcode ? Press (y/n): ") 
				shortcode = raw_input("Do you want to save this as your shortcode ? Press (y/n): ") 
		
				if(str.lower(shortcode.strip()) == 'y'): 
					if newpath not in prevPaths.values(): 
						speak("How would you like to save it? ")
						print "How would you like to save it: " 
						key = text() 
						#key = raw_input("How would you like to save it: ") 
						prevPaths[key]=newpath
						write_data(number, prevPaths, freq, str.lower(shortcode.strip())) 


			'''
			confirm = "n" 
			a = 1
			if(len(prevPath) > 3): a=3   
			if(len(prevPath) != 0): 
				confirm = raw_input('Do you want to continue from previous (task ' + str(prevPath[a-1]) + ') task? (y/n): ') 
			if(str.lower(confirm.strip())=="y"): 
				newpath = user(root, prevPath[:a]) 
			else: 
				newpath = user(root, []) 
			'''
	else: 
		speak("Do you want to hit the most frequent topic ? Press (y/n): ") 
		globalshort = raw_input("Do you want to hit the most frequent topic ? Press (y/n): ") 
		if(globalshort=='y'):
			newpath=repeatMaxTask(root,freq,overallfreq) 
			speak("Do you want to save this as your shortcode ? Press (y/n): ") 
			shortcode = raw_input("Do you want to save this as your shortcode ? Press (y/n): ") 
		
			if(str.lower(shortcode.strip()) == 'y'): 
				if newpath not in prevPaths.values():
						speak("How would you like to save it? ")
						print "How would you like to save it: " 
						key = text() 
						#key = raw_input("How would you like to save it: ") # speak 
						prevPaths[key]=newpath
						write_data(number, prevPaths, freq, str.lower(shortcode.strip())) 
		else:	
			newpath = user(root,[],freq,overallfreq) 
			print "Path taken this time: ", newpath 
			speak("Do you want to save this as your shortcode ? Press (y/n): ") 
			shortcode = raw_input("Do you want to save this as your shortcode ? Press (y/n): ") 
			#shorcode = shortcode[len(shortcode)-1] 
			if(str.lower(shortcode.strip()) == 'y'): 
				if newpath not in prevPaths.values():
						speak("How would you like to save it? ")
						print "How would you like to save it: " 
						key = text() 
						prevPaths[key]=newpath
						write_data(number, prevPaths, freq, str.lower(shortcode.strip())) 
	write_freq([overallfreq]) 

	
	#print "Frequency: ", f.f
	
	'''
	while(1):
		uin = raw_input("Do you want to quit? ") 
		if( uin == "y"): 
			print uin
			break
		else: 
			print uin 
			root = tree 
			user(root) 	
	''' 		
	#print "Past: ", root.childList[0].childList[1].past
	#repeatTask(root)
	#print last_call
		
if __name__ == "__main__": 
	test() 
