# Connor Parish (connorparish9@gmail.com)
# This is a script to scrape book quotes by authors from good reads


from bs4 import BeautifulSoup
import requests
import re
import csv
import pandas as pd

def scrape_author(author, max_len):
	f_l = author.split()
	url = 'https://www.goodreads.com/search?utf8=%E2%9C%93&q={}+{}&search_type=quotes'.format(f_l[0], f_l[1])

	grURL = requests.get(url)
	soup = BeautifulSoup(grURL.content, 'html5lib')
	quotes = []

	count = 0
	for row in soup.findAll('div', attrs = {'class':'quoteText'}): 
		quote = {}
		if(len(row.text) <= max_len):
			row_split = row.text.split('\n')
			count = 0
			for instance in row_split:
				if(not instance.isspace() and not instance == ''):
					instance = instance.strip()
					if(len(instance) > 3):
						quote[count] = instance
						count += 1
			quotes.append(quote)

	return quotes

    


if __name__ == '__main__':
	authors = ['Judea Pearl', 'Daniel Kahneman', 'Nicholas Taleb', 'Peter Thiel', 'Elon Musk']
	quotes = []
	q_authors = []
	SAVE_FILE = './author_quotes.csv'
	
	for author in authors:
		a_quotes = scrape_author(author, 1000)
		print(author + " has " + str(len(a_quotes)) + " quotes")
		for quote in a_quotes:
			quotes.append(quote[0])
			q_authors.append(quote[1])

	df = pd.DataFrame({
		"Quotes" : quotes,
		"Authors": q_authors
		})

	df.to_csv(SAVE_FILE)

