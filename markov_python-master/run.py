from fetch_data import get_book_data
from cc_markov import MarkovChain
from textify import textify_markov
from time import sleep
	
book = get_book_data()

mc = MarkovChain()
mc.add_string(book['text'])

print textify_markov(mc.generate_text(15))

#print textify_markov_text(mc.generate_text(10))


print book['title'], book['passage']

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

"""
	for i in range(len(generated_text):
		if generated_text[i] in exclude_word:
			generated_text[i].pop()
		elif word == 'i' and len(word) < 2:
			string += word.upper() + ' '
		else:
			string += word + ' '
		print string
	
	re.sub(u"(\u2018|\u2019)", "'", string)
	return string.capitalize()
	"""
