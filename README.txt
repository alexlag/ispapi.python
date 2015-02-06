1. To install ModisSDK run 'python setup.py install'

2. To use any service of ModisAPI in your project, import subclass of module. 
	For TexterraAPI it looks like this: 
		>>> from modis import texterraapi

3. Now you can create an access object using your Apikey:
		>>> t = texterraapi.TexterraAPI('YOURKEY')
		
	You can also specify service name and version:
		>>> t = texterraapi.TexterraAPI('YOURKEY', 'texterra', 'v3.0')

4. To access different tools just call corresponding method:
		>>> tags = t.posTagging('Hello World')

	* You can also invoke Texterra with custom request:
		>>> result = t.customRequest(path, queryParams) for GET request
		>>> result = t.customRequest(path, queryParams, formParams) for POST request

	You can always check description of each available method with
		help(modis) # For all services
		help(modis.texterraapi) # For desired service, i.e. texterra

5. Methods return dictionary, so you can navigate through it according to documentation:
		>>> for annotation in tags:
				print an['text']

	Use '@' before atrribute names and '#text' to access own text of nodes.
	Use only node name to access its text if there are no attributes or subnodes:
		>>> print an['value']['@class'], an['value']['#text']
