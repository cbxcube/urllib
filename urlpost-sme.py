##bla
##x = 
###x = urllib.request.urlopen('https://www.google.cz/?gws_rd=ssl#safe=off&q=praha'##x = )##x = 
##blax x x x x xxx xx    
##x = 

import urllib.request
import urllib.parse

#url = 'https://www.google.cz/?gws_rd=ssl#safe=off&q=praha'
#url = 'http://www.sme.sk/search/'
url = 'http://www.sme.sk/'
#url = 'http://pythonprogramming.net/search'

# productionextraurl = https://pythonprogramming.net/search/?q=basic
# expression with space in string = https://pythonprogramming.net/search/?q=python+veritas
# tutorialextraurl = https://pythonprogramming.net/search/?s=basic&submit=Search


# tutorial values:
#values = {'s':'basic',
#	  'submit':'search'}

# production values:
values = {'q':'bratislava',
	  'period':'90'}

# encode hardcoded url to url encoding (search+this+word >> search%20this%20word)
data = urllib.parse.urlencode(values)
# code as utf-8 encoding ==> put data in bytes
data = data.encode('utf-8')
# do request
req = urllib.request.Request(url,data)

# finally open desired url
resp = urllib.request.urlopen(req)
# prepare response data 
respData = resp.read()

# print output
print(respData)

# write to file if required
#with open('sme.html', 'w') as out:
#    out.write(respData + '\n')
f = open('sme.html','w')
# convert bytes to string
fileout = str(respData)
# write the file
f.write(fileout)

