import sys
from urllib2 import Request, urlopen, URLError
from urllib import urlencode

#host = "http://vivek-notebook:3000"
host = "http://pacific-journey-1425.azurewebsites.net"

try:

	request = Request(host + "/evil")

	response = urlopen(request)
	kittens = response.read()
	print kittens

except URLError, e:
	print 0
