from fetch_data import Get_book_data
from cc_markov import MarkovChain
from textify import Textify_markov
from time import sleep
from random import randint
from round import Game_run
import sys

#adding books from gutenberg.org -- ones that fit the format. Correct format is usually ones from the popular list. 
#Format compatibility can easily be "tested" with the fetch_data function, by printing the return object. 	
books_list = ['http://www.gutenberg.org/files/11/11-h/11-h.htm', 'http://www.gutenberg.org/files/2701/2701-h/2701-h.htm', 'http://www.gutenberg.org/files/1342/1342-h/1342-h.htm', 'http://www.gutenberg.org/files/76/76-h/76-h.htm', 'http://www.gutenberg.org/files/1080/1080-h/1080-h.htm', 'http://www.gutenberg.org/files/1497/1497-h/1497-h.htm', 'http://www.gutenberg.org/files/1322/1322-h/1322-h.htm', 'http://www.gutenberg.org/files/1184/1184-h/1184-h.htm']

def status(user, score):
	return str(user) + "'s score is: " + str(sum(score))	

def program():
	score = [0]
	run = True	
	while run:
		book_url = books_list[randint(0, len(books_list)-1)]
		print len(books_list)
		book = Get_book_data(book_url)
		user = raw_input("Hi and welcome....please enter your name: " ).capitalize()
		rules = 'You start off with 0 points. The goal of the game is to guess the correct book and/or author. For each guess that is incorrect, your score will be increased by one point. You will also add points everytime you request a hint. Good luck ' + user + "\n"
		sleep(1)
		print "The rules are as follows:\n\n" + rules
		sleep(1)
		print "Let's go! " + status(user, score) + "\n"
		sleep(1)
		print "First genereated text, try to guess the author and/or the book \n"
		sleep(1)
		mc = MarkovChain()
		mc.add_string(book['text'])
		print '"' + Textify_markov(mc.generate_text(15)) + '" \n'
		#result = Game_run(book, 0) 
		score.append(Game_run(book, 0))
		sleep(1)
		print status(user, score)
		option = raw_input('Want to run another round with a different book? Enter Y/N: ').upper()
		while option == 'Y':
			books_list.remove(book_url)
			book_url = books_list[randint(0, len(books_list)-1)]
			book = Get_book_data(book_url)
			mc = MarkovChain()				
			mc.add_string(book['text'])
			print '"' + Textify_markov(mc.generate_text(15)) + '"'
			#result = Game_run(book)
			score.append(Game_run(book, 0))
			option = raw_input('Want to run another round with different books? Enter Y/N: ').upper()
		else:
			print status(user, score)
			run = False			
		print len(books_list)
	else:
		print "Ending game..."
		sys.exit()
			
program()





"""
mc = MarkovChain()
mc.add_string(book['text'])

print textify_markov(mc.generate_text(15))
"""

#print textify_markov_text(mc.generate_text(10))
#print book['title'], book['passage']

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