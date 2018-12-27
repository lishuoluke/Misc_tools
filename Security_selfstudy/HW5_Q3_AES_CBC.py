from Crypto.Cipher import AES

from binascii import hexlify
from binascii import unhexlify
from datetime import datetime

def aes_enc(key,msg,iv):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    return cipher.encrypt(msg)

key = '\x00'*16
iv = '\x00'*16
plain = "\x00"*int(1.6*10**8)

start_time = datetime.now()
mycipher = hexlify(aes_enc(key,plain,iv))
print(mycipher)
time_elapsed = datetime.now() - start_time
print('time_elapsed for library CBC: ', time_elapsed)
# last 128 bit is 3dfeb5f006b7210c8d6a98b0d9aad38f

