import urllib
import json

email =('david.piprof@seznam.cz')
pwd  = ('testik')
data = urllib.parse.urlencode({'email': email, 'pwd':pwd, 'service': 'nudge'})
data = data.encode('utf-8')
request = urllib.request.Request("https://jawbone.com/user/signin/login")
# adding charset parameter to the Content-Type header.
request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
f = urllib.request.urlopen(request, data)

#print(f.read().decode('utf-8'))
j=(f.read().decode('utf-8'))
b=json.loads(j)