from fetch_data import get_book
from cc_markov import MarkovChain
from time import sleep


def textify_markov_text(generated_text):
	generated_text.append('.')
	string = ''
	for word in generated_text:
		string += word
	#string[0].upper()
	return 

book = get_book()
mc = MarkovChain()
mc.add_string(book['text'])

#print textify_markov_text(mc.generate_text(10))

print str(mc.generate_text(10))




#print book['title'], book['author']

"""
print 'If you can guess the title of this book, I must admit you are good.'

sleep(1)

print "you will be given a generated text, based on the style of an author in a particular book. Guess the right book or author and you win"
user 
"""

"""
mc = MarkovChain()

mc.add_string(book.text)

mc.generate_text(10)
"""
"""
print "If you can guess the title of this book, I must admit you are good. \n I will give you the change to talk to the man himself, and maybe you will find yourself....."



print h
guess = raw_input(
print mc.generate_text(10)
"""
