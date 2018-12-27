import requests
import json
import sys

port = ':19332'




if sys.argv[1] == 'm':
    url = 'http://username@domain1name'

elif sys.argv[1] == 'b':
    url = 'http://username@domain1name'
else:
    print ("node not supported")
    exit()




print ("curling url :" + url)
data = {"id": 0, "method": "getdifficulty"}
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)
result =json.loads (r.text)
print (result)
difficulty = result['result']
print (difficulty)
#
time = 2**31*difficulty/(600*10**6)
#
print (" it takes " + str(time) + ' s to find a new block')


#47.75.88.41
#47.75.15.141clea
