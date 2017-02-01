#!/usr/bin/python

import peewee
from peewee import *

db = MySQLDatabase('Repo', user='root', passwd='')


class Repos(Model):
	repoID = IntegerField()
	repoName = CharField()
	repoURL = CharField()
	repoAPI = CharField()
	
	class Meta:
		database = db


def before_request_handler():
	db.connect()

def after_request_handler():
	db.close()
	
def insertRepo(repoid, name, url):
	Repos.create(repoID=repoid, repoName=name, repoURL=url)
		
def insertApi(repoid, api):
	Repos.update(repoAPI=api).where(Repos.repoID==repoid).execute()
	
def checkLastID():
	return Repos.select(fn.Max(Repos.repoID)).get().repoID
	