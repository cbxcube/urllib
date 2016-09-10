import urllib.request
import urllib.parse


try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())

except Exception as e:
    print(str(e))
try:
    url = 'https://www.google.com/search?q=python'

    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

	# generating file
    saveFile = open('out.withHeadersgoogle.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
#   I can not print this string! what is screwed?
#	print(str("Generating out.withHeadersgoogle.txt"))

except Exception as e:
    print(str(e))
