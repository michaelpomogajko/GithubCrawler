#!/usr/bin/python

import database
import requests

try:
	from bs4 import BeautifulSoup
except ImportError:
	from BeautifulSoup import BeautifulSoup

def getfiles():
	
	fileLinks = []
	
	lastID = database.checkLastID() or 0
	repoURL = database.getUrlByID(lastID)
	
	html = requests.get(repoURL).text
	soup = BeautifulSoup(html, "lxml")
	arr = soup.find_all("a", { "class" : "js-navigation-open" })
	for link in arr:
		files = link["href"]
		if "master/" in files:
			fileLinks.append(files)
	print fileLinks
		
	
getfiles()