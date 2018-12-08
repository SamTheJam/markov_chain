from time import sleep
from random import randint


def Game_run(book_input, num_runs=0): 
	solution = str(book_input['title'] + " " + book_input['author'] + " " + book_input['author_initials']).lower()
	num_runs = num_runs
	option = raw_input('To guess press G, to get a hint press H, to quit press Q: ').upper()
	if option == 'G':
		sleep(2)
		guess = raw_input('Guess: ')
		if guess.strip().lower() in solution:
			print 'Correct, the book is ' + book_input['title'] + 'written by ' + book_input['author']
			return num_runs
		else:
			print "Wrong..."
			num_runs += 1
			Game_run(book_input, num_runs)		
	elif option == 'H':
		print 'Passage: \n' + book_input['passage'] + '\n'
		print 'Initials:' + book_input['author_initials'] + '\n'
		num_runs += 1
		sleep(1)
		guess = raw_input('Guess: ').strip().lower()
		if guess in solution and len(guess) > 1:
			print 'Correct, the book is ' + book_input['title'] + ' written by ' + book_input['author']
			return num_runs
		else:
			print 'Wrong....'
			num_runs += 1
			Game_run(book_input, num_runs)			
	elif option == "Q":
		print "Quitting round...."	
		return num_runs
	else:
		print "error...running again"
		Game_run(book_input, num_runs)
		
		
#print solution 
