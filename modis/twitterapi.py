# -*- coding: utf-8 -*-
import modisapi as modis
class TwitterAPI(modis.ModisAPI):
	"""This class provides methods to work with Twitter NLP REST via OpenAPI"""
	
	# Default Twitter NLP path
	twitterName = 'twitter-nlp'
	twitterVersion = '1.0'

	specs = {
		'path': 'extract',
		'params': {}
	}

	def __init__(self, key, name=None, ver=None):
		"""Provide only apikey to use default Twitter NLP service name and version."""
		if name == None:
			name = TwitterAPI.twitterName
		if ver == None:
			ver = TwitterAPI.twitterVersion
		modis.ModisAPI.__init__(self, key, name, ver)

	def extractDDE(self, lang, username, screenname, description, tweets):
		"""Extracts demographic attributes from provided Twitter info. All info is required, but can be empty"""
		if isinstance(tweets, list):
			tweets = ' '.join(tweets)
		form = {
				'lang': lang,
				'username': username,
				'screenname': screenname,
				'description': description,
				'tweet': tweets
		}
		return self.POST('extract', {}, form)

	def customQuery(self, path, query, form=None):
		"""Invoke custom request to Twitter NLP"""
		if form:
			return self.POST(path, query, form)
		else:
			return self.GET(path, query)