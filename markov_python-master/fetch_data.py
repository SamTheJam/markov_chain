from bs4 import BeautifulSoup
import urllib2
from cc_markov import MarkovChain

#import ssl


url = 'http://www.gutenberg.org/files/2638/2638-h/2638-h.htm'
#context = ssl._create_unverified_context()

response = urllib2.urlopen(url)
html = BeautifulSoup(response, 'html.parser')



print html.get_text()

mc = MarkovChain()

mc.add_string(html.get_text())

print mc.generate_text(10)

# testing change + Testing chaning in push directory