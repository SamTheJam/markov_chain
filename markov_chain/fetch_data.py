from bs4 import BeautifulSoup
import urllib2
import ssl

context = ssl._create_unverified_context()
response = urllib2.urlopen('http://www.qz.com', context=context)
html = BeautifulSoup(response, 'html.parser')

print html.get_text()


# testing change + Testing chaning in push directory