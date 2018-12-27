import requests
import json
import sys



if sys.argv[1] == 'm':
    url = 'http://antpool:antpool123@47.75.88.41'

elif sys.argv[1] == 'b':
    url = 'http://antpool:antpool123@47.75.15.141'
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


payload = '{"jsonrpc":"2.0","method":"eth_getWork","params":[12],"id":1}'
headers = headers = {'content-type': 'application/json'}
r = requests.post(url, data=payload, headers=headers)
print (r.content)
dataset = json.loads(r.content)
diff_raw = dataset['result'][2]
print("raw diff is " + diff_raw)
diff = 2**256/int(diff_raw,16)
print ("target diff is " + str(diff))
time = diff / 230000000
print ("it takes "+ str(time) + " to found a new block")
hash = diff / 15
print ("hashrate is "+ str(hash))

#print("diff is "+str(int(diff,16)))
#time = int(diff,16)/230000000
#print ("it takes " + str(time) +" seconds to find a block")

# standard curl :::: curl -X POST http://antpool:antpool123@47.75.88.41:18555 -d '{"jsonrpc": "2.0", "id":"1", "method":"eth_blockNumber", "params": [] }' -H "Content-Type:application/json"