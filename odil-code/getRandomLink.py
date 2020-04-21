import sys
import random
from urllib.parse import urlparse
import httplib2 # python3 -m pip install httplib2
from bs4 import BeautifulSoup, SoupStrainer # python3 -m pip install beautifulsoup4

# pass this in as an argument
url = sys.argv[1]

# this is to get the hostname from the url
o = urlparse(url)
host = o.scheme + '://' + o.hostname + '/'

# empty list to store links
links = []

for i in range(1, 5):

	# getting the html
	http = httplib2.Http()
	status, response = http.request(url + '/' + str(i) + '/')

	# setting up BeautifulSoup
	soup = BeautifulSoup(response, 'html.parser')

	# find all tags with id = "gab1"
	for content in soup.find_all(id = "gab1"):

		# for each child element
		for findArticle in content.children:

			# check if it is an article tag
			if findArticle.name == 'article':

				# for each child element
				for findLink in findArticle.children:

					# check if it is an a tag
					if findLink.name == 'a':

						# append link to list
						links.append(host + findLink['href'])


file = open(sys.argv[2], 'w')
file.write(random.choice(links))
file.close()
