import cv2
import numpy as np
import matplotlib as mat

import nltk
from nltk import chunk 

def tokenize(text):
	tokens = nltk.word_tokenize(text) 
	return tokens
	
def pos_tagger(tokens):
	tags = nltk.pos_tag(tokens) 
	return tags
	#print 'tokens: ' , tokens
	#print 'tags: ', tags

from nltk import chunk 

def chunker(tags):  
	chunks = chunk.ne_chunk(tags)
	return chunks 
	 
	 
	 
def test():	
	#print pos_tagger(tokenize("Harry accepted the position of vice chairman of Carlyle Group , a merchant banking concern.")) 
	chunks = chunker(pos_tagger(tokenize("Harry accepted the position of vice chairman of Carlyle Group , a merchent banking concern."))) 
	print chunks 
	chunks.draw() 
#test() 
