#!/usr/bin/python

import database
import requests

try:
	from bs4 import BeautifulSoup
except ImportError:
	from BeautifulSoup import BeautifulSoup

def getfiles():
	lastID = database.checkLastID() or 0
	repoURL = database.getUrlByID(lastID)
	print repoURL
	
	html = requests.get(repoURL).text
	soup = BeautifulSoup(html, "lxml")
	
	#print soup.prettify()
	
getfiles()