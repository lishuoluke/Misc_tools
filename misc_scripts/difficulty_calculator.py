##   0x0000000087a42f8e294cac06e8c97da8148f10a4bfeb6aa025120b2b74e9306e

diff_raw = "0x0000000084a5f9551d7b3ca5dd944084ac356326c19c9fee0efbdbb981bc341f"
print("raw diff is " + diff_raw)
diff = 2**256/int(diff_raw,16)
print ("target diff is " + str(diff))
time = diff / 230000000
print ("it takes "+ str(time) + " to found a new block")
hash = diff / 15
print ("hashrate is "+ str(hash))