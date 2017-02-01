#!/usr/bin/python

import sys
import json
import requests
import time
from database import *

'''
Github unsecure API crawler
@author Misha Frenkman
@version 0.1

'''


githubURL = "https://api.github.com/repositories?since="


def crawler():
	startID = 0
	lastID = 0
	while True:	
		startID = checkLastID()
		req = githubURL+str(startID)
		res = requests.get(req).json()
		
		#Check for the right Github response
		if type(res) is list:
			# Check for private
			for repo in res:
				if repo[u'private'] == False:
					insertRepo(repo[u'id'], repo[u'full_name'], repo[u'html_url'])
					
			lastID = res[-1][u'id']
		else:
			print "Github kicked me out :( waiting 1min to reconnect :("
			print "Timestamp: %s" % (time.strftime("%d.%m.%Y %H:%M"))
			time.sleep(60)

crawler()
	