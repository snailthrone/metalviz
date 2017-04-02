#/usr/bin/python
# -*- coding: utf-8 -*-
import bs4
import csv

fileName = 'grindcore'
inputFile = open(''+fileName+'.html')
soup = bs4.BeautifulSoup(inputFile, 'html.parser')

outputFile = open(''+fileName+'.csv', 'w', encoding='utf-8')
outputWriter = csv.writer(outputFile, delimiter=',', quotechar='"')
outputWriter.writerow(['id','artist','album','date','genres','ratings'])

def parseData():
	artists = soup.findAll('a', {'class':'artist'})
	albums = soup.findAll('a', {'class':'album'})
	dates = soup.findAll('span', {'class':'chart_year'})
	genres = soup.findAll('span', {'class':'chart_genres'})
	ratings = soup.findAll('div', {'class':'chart_stats'})
	writeData(artists, albums, dates, genres, ratings)

def writeData(art, alb, dat, gen, rat):
	if len(art) == len(alb):
		x = 0
		id1 = 1
		while x < len(art):
			#Correcting id:s if there are more than one genre in input file
			if id1 == 201:
				id1 = 1
			artist = art[x].get_text()
			album = alb[x].get_text()
			date = dat[x].get_text()
			genre = gen[x].get_text()
			rating = rat[x].find('a').get_text()
			outputWriter.writerow([id1, artist.strip(),album.strip(),date.strip(),genre.strip(),rating.strip()])
			id1 += 1
			x += 1

	else:
		print('Error: Length of artist and albums does not match.')
		debug(art, alb, dat, gen, rat)

def debug(a, b, c, d, e):
	print(len(a))
	print(len(b))
	print(len(c))
	print(len(d))
	print(len(e))
	x = 0
	while x < len(b):
		print(str(x+1) + '. ' +str(a[x].get_text()) + ' - ' + str(b[x].get_text()))
		x += 1

parseData()

inputFile.close()
outputFile.close()
