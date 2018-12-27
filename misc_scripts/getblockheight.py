import requests
import json
import sys

if sys.argv[1] == "BTC":
    port = ':18332'
elif sys.argv[1] == "BCH":
    port = ':18362'




if sys.argv[1] == 'm':
    url = 'http://username@domain1name'

elif sys.argv[1] == 'b':
    url = 'http://username@domain1name'
else:
    print ("node not supported")
    exit()



print ("curling url :" + url)
data = {"id": 0, "method": "getblockchaininfo"}
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)
result =json.loads (r.text)
print (result)
#difficulty = result['result']
#print (difficulty)
#
#time = 2**32*difficulty/(27*10**12)
#
#print (" it takes " + str(time) + ' s to find a new block')


#47.75.88.41
#47.75.15.141clea
