
import urllib.request
import urllib.parse


try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())

except Exception as e:
    print(str(e))

try:
    # overide recognition of python on server side
    # if this is not in place google will say HTTP Error 403: Forbidden
    url = 'https://www.google.com/search?q=test'
	
	# browser info    
	headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17" 
	# empty place after "url" part : q=test
	# headers is default parameter and if not changed do not need to be passed
	req = urllib.request.Request(url, headers = headers)
	resp = urllib.request.urlopen(req)
	respData = resp.read()

	saveFile = open('out.withHeaders.txt','w')
	# change to string 
	saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
	print(str(e))
