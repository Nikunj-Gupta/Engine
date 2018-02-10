from fuzzywuzzy import fuzz 
import nltk 
from nltk.corpus import treebank 

#print fuzz.ratio("yes i am nikunj", "yep i am nikunj") 

sentence = "Harry accepted the position of vice chairman of ", 
"Carlyle Group , a merchent banking concern."

tokens = nltk.word_tokenize(sentence) 
print "Tokens: ", tokens 

tagged = nltk.pos_tag(tokens) 
print "\nTagged: ", tagged

entities = nltk.chunk.ne_chunk(tagged) 
print "\nEntities: ", entities 

entities.draw() 

#t = treebank.parsed_sents('wsj_0001.mrg')[0] 
#t.draw() 
