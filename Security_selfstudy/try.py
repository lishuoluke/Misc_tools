from Crypto.Cipher import AES

from binascii import hexlify
from binascii import unhexlify

def aes_enc(key,msg,iv):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    return cipher.encrypt(msg)

def aes_dec (key,msg,iv):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    return cipher.decrypt(msg)



key = unhexlify('56e47a38c5598974bc46903dba290349')
iv = unhexlify('8ce82eefbea0da3c44699ed7db51b7d9')
plain = unhexlify('a0a1a2a3a4a5a6a7a8a9aaabacadaeaf\
b0b1b2b3b4b5b6b7b8b9babbbcbdbebf\
c0c1c2c3c4c5c6c7c8c9cacbcccdcecf\
d0d1d2d3d4d5d6d7d8d9dadbdcdddedf')

mycipher = hexlify(aes_enc(key,plain,iv))
print(mycipher)

decipher = aes_dec(key,mycipher,iv)
print('cao mi ma de')
print(decipher)

testvector = b'c30e32ffedc0774e6aff6af0869f71aa\
0f3af07a9a31a9c684db207eb0ef8e4e\
35907aa632c3ffdf868bb7b29d3d46ad\
83ce9f9a102ee99d49a53e87f4c3da55'

if mycipher == testvector:
    print("mycipher matched the testvector")
