from time import sleep
from random import randint


def game_run(book_input, num_runs=0): 
	solution = str(book_input['title'] + " " + book_input['author'] + " " + book_input['author_initials']).lower()
	num_runs = num_runs
	#solution = solution.split(' ')
	#solution = [x for x in solution x]
	#print solution  
	option = raw_input('To guess press G, to get a hint press H, to quit press Q: ').upper()
	if option == 'G':
		sleep(2)
		guess = raw_input('Guess: ')
		if guess.strip().lower() in solution:
			print 'Correct, the book is ' + book_input['title'] + 'written by ' + book_input['author']
			#return 0
		else:
			print "Wrong..."
			num_runs += 1
			game_run(book_input)		
	elif option == 'H':
		print 'Passage: \n' + book_input['passage'] + '\n'
		print 'Initials:' + book_input['author_initials'] + '\n'
		num_runs += 1
		sleep(4)
		guess = raw_input('Guess: ').strip().lower()
		#print guess, solution
		if guess in solution:
			print 'Correct, the book is ' + book_input['title'] + ' written by ' + book_input['author']
			#print num_runs
			return num_runs
		else:
			print 'Wrong....'
			game_run(book_input, num_runs)			
	elif option == "Q":
		print "quitting"
		pass
	else:
		print "error..running again"
		game_run(book_input, num_runs)