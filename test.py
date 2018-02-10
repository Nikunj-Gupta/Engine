import fileinput
import ast 

for line in fileinput.FileInput("freq_file.csv",inplace=1):
	if "A" in line:
		update = ast.literal_eval(line) 
		#print str(update[1]) 
		line=line.replace(str(update[1]),str(update[1]+1)) 
	print line, 
