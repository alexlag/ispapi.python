# -*- coding: utf-8 -*-
import xmltodict
import requests

class ModisAPI(object):
  ROOT_URL = 'http://api.ispras.ru/{0}/{1}/'

  def __init__(self, key, name, ver):
    import sys
    if len(key) == 40:
      self.serviceName = name
      self.serviceVersion = ver
      self.apikey = key
      self.url = ModisAPI.ROOT_URL.format(name, ver)
    else:
      print('Please provide proper apikey')
      sys.exit(0)

  def GET(self, path, request_params):
    """Method for invoking ModisAPI GET request"""
    url = self.url + path;
    request_params['apikey'] = self.apikey
    page = requests.get(url, params=request_params, timeout=20)
    if page.status_code == 200:
      xmldict = xmltodict.parse(page.text)
      return xmldict
    else:
      page.raise_for_status()

  def POST(self, path, request_params, form_params):
    """Method for invoking ModisAPI POST request"""
    url = self.url + path;
    request_params['apikey'] = self.apikey
    page = requests.post(url, params=request_params, data=form_params, timeout=20)
    if page.status_code == 200:
      xmldict = xmltodict.parse(page.text)
      return xmldict
    else:
      page.raise_for_status()
