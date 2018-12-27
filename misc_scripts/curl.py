import requests
import json
import sys



if sys.argv[1] == 'm':
    url = 'http://username@domain1name'

elif sys.argv[1] == 'b':
    url = 'http://username@domain1name'
else:
    print ("node not supported")
    exit()

if sys.argv[2] == 'BTC':
    url = url + ':18332'
elif sys.argv[2] == 'BCH':
    url = url + ':18362'
else:
    print ("coin not supported")
    exit()

print ("curling url :" + url)
payload = '{"jsonrpc": "2.0", "id":"1", "method":"getdifficulty", "params": [] }'
headers = headers = {'content-type': 'application/json'}
r = requests.post(url, data=payload, headers=headers)
print (r.content)
dataset = json.loads(r.content)
difficulty = dataset['result']
time = int(difficulty)*2**16/(30*10**12)
print ("it takes " + str(time) +" s to find a new block")


#curl -X POST http://antpool:antpool123@47.75.88.41:18332 -d '{"jsonrpc": "2.0", "id":"1", "method":"getdifficulty", "params": [] }' -H "Content-Type:application/json"