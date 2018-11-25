from bs4 import BeautifulSoup
import urllib2
from cc_markov import MarkovChain
from random import randint

books = ['http://www.gutenberg.org/files/2638/2638-h/2638-h.htm', 'http://www.gutenberg.org/files/2542/2542-h/2542-h.htm', 'http://www.gutenberg.org/files/11/11-h/11-h.htm', 'http://www.gutenberg.org/files/2701/2701-h/2701-h.htm', 'http://www.gutenberg.org/files/74/74-h/74-h.htm', 'http://www.gutenberg.org/files/76/76-h/76-h.htm' ]

def get_book_data():
	url = books[randint(0, len(books)-1)]
	response = urllib2.urlopen(url)
	soup = BeautifulSoup(response, 'html.parser')
	html_as_string = '' 
	#print html.get_text()
	paragraphs = soup.find_all('p')
	for par in paragraphs:
		html_as_string += par.get_text()
	title = soup.title.get_text().split(',')[0].strip()
	author = soup.title.get_text().split(',')[1].strip().replace('by', '')
	author_initials =  '.'.join([x[0] for x in author.split(" ")])
	passage = paragraphs[randint(0, len(paragraphs)-1)].get_text()
	#mc = MarkovChain()
	#mc.add
	# print html_as_string
	return { 'text': html_as_string,
			 'title': title,
			 'author': author,
			 'author_initials': author_initials,
			 'passage': passage	 }			 
	






"""

#from io import BytesIO
#from gtts import gTTS
#import facebook
#import requests
#import ssl 
token = 'EAADzT03XrgYBACW4m3hvqIlRGecMr0YunnNoTPZBap57IfoGf3JBIZB6BkZCe7Yr50YZBYkomTZCrRcg6mUQPpZAsUE2fWVOUCV0YtvAHdV0V0dMKy5M5xwxlcsk3aFAb0t9pDvfFPK0x8xFJc3DQ2QUgu00XV6vTtHG5GphlHMkpepYF9q7teJRfvo3BOjhOtLmkqZAWq881lq5pMpOQJEARF8AIU6jmWKknBQuiPpzwZDZD'

graph = facebook.GraphAPI(access_token=token, version = 3.1)

user = graph.request('/me?fields=id,name,first_name, last_name, picture')

print user
#print mc.generate_text(10)

# testing change + Testing chaning in push directory
mp3_fp = BytesIO()
tts = gTTS('Hello', 'en')
tts.write_to_fp(mp3_fp)

"""