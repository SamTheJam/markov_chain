list_exclude_sign = ['"', "'", '""', ')', '(', ' " "', '-', '-" "', ' " ',' "', '" ']

def textify_markov(generated_text):
	generated_text = [x for x in generated_text if x not in list_exclude_sign]
	generated_text.append('...')
	for i in range(len(generated_text)):
		if generated_text[i] == 'i':
			generated_text[i] = 'I'
	string = ' '.join(generated_text)
	return string.capitalize()