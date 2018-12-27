from Crypto.Cipher import AES
from binascii import unhexlify


def aes_enc(key, msg):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(msg)

def aes_dec(key,msg):
    decipher = AES.new(key, AES.MODE_ECB)
    return decipher.decrypt(msg)

key = '\x00'*16
message = 'SUTD-MSSD-51.505*Foundations-CS*'
ciphertext = aes_enc(key,message)
print(ciphertext)







cipher = b'\x88\\L\xe8F\x07\x8d\xea\x93\xb7\x99\xe0\xba\xb3\xe7\x10\xc9{.d\x00\xa3K\xbd\xe3oHhCv\xdd\xa8'
deciphertext = aes_dec(key,cipher)
print(deciphertext)

#swap the first 128 bit to form a new one
swapcipher =b'\xc9{.d\x00\xa3K\xbd\xe3oHhCv\xdd\xa8\x88\\L\xe8F\x07\x8d\xea\x93\xb7\x99\xe0\xba\xb3\xe7\x10'
decipherswaptext = aes_dec(key,swapcipher)
print(decipherswaptext)


#corrupt the last bit to form a new one
corruptcipher =b'\xc9{.d\x00\xa3K\xbd\xe3oHhCv\xdd\xa8\x88\\L\xe8F\x07\x8d\xea\x93\xb7\x99\xe0\xba\xb3\xe7\x11'
deciphercorrupttext = aes_dec(key,corruptcipher)
print(deciphercorrupttext)

