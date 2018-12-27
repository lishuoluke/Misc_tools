from Crypto.Cipher import AES
from Crypto import Random

from binascii import hexlify
from binascii import unhexlify


def aes_dec(key, msg, iv):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    return cipher.decrypt(msg)

key = unhexlify('8000000000000000000000000000000000000000000000000000000000000001')
ciphertext = unhexlify('87F348FF79B811AF3857D6718E5F0F917C3D26F77377635A5E43E9B5CC5D05926E26FFC5220DC7D405F1708670E6E017')
iv = Random.new().read(16)
cipher = AES.new(key, AES.MODE_CBC, iv)

plaintext = aes_dec(key,ciphertext,iv)
print(plaintext)
