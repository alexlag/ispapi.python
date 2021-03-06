# -*- coding: utf-8 -*-
import xmltodict
import requests

class API(object):
  API_URL = 'http://api.ispras.ru/{0}/{1}/'

  def __init__(self, key=False, name=None, ver=None, host=None):
    if host:
      self.apikey = key
      self.url = host
    else:
      import sys
      if len(key) == 40:
        self.serviceName = name
        self.serviceVersion = ver
        self.apikey = key
        self.url = API.API_URL.format(name, ver)
      else:
        print('Please provide proper apikey')
        sys.exit(0)

  def GET(self, path, request_params, format='xml'):
    """Method for invoking Ispras API GET request"""
    url = self.url + path;
    if self.apikey: request_params['apikey'] = self.apikey
    page = requests.get(url, params=request_params, headers=self.__headers(format), timeout=60)
    if page.status_code == 200:
      return self.__parse(page, format)
    else:
      page.raise_for_status()

  def POST(self, path, request_params, form_params, format='xml'):
    """Method for invoking Ispras API POST request"""
    url = self.url + path;
    if self.apikey: request_params['apikey'] = self.apikey
    page = requests.post(url, params=request_params, headers=self.__headers(format), data=form_params, timeout=60)
    if page.status_code == 200:
      return self.__parse(page, format)
    else:
      page.raise_for_status()

  def __parse(self, page, format):
    if format == 'xml':
      return xmltodict.parse(page.text)
    elif format == 'json':
      return page.json()
    else:
      return page.text

  def __headers(self, format):
    headers = {}
    if format == 'xml':
      headers['Accept'] = 'application/xml'
    elif format == 'json':
      headers['Accept'] = 'application/json'
    return headers
