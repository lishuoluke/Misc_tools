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


if sys.argv[2] == 'ETH':
    url = url + ':18545'
elif sys.argv[2] == 'ETC':
    url = url + ':18555'
else:
    print ("coin not supported")
    exit()


payload = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest", true],"id":1}'
headers = headers = {'content-type': 'application/json'}
r = requests.post(url, data=payload, headers=headers)
print (r.content)
dataset = json.loads(r.content)
diff = dataset['result']['difficulty']
print("diff is "+str(int(diff,16)))
time = int(diff,16)/230000000
print ("it takes " + str(time) +" seconds to find a block")

# standard curl :::: curl -X POST http://antpool:antpool123@47.75.88.41:18555 -d '{"jsonrpc": "2.0", "id":"1", "method":"eth_blockNumber", "params": [] }' -H "Content-Type:application/json"