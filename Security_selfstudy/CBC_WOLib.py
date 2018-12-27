from Crypto.Cipher import XOR
from Crypto.Cipher import AES
from binascii import hexlify
from binascii import unhexlify
from datetime import datetime


def padding(msg):
    if len(msg) % 16 is not 0:
        msg += (16 - len(msg) % 16) * b'\x00'
    return msg


def aes_cbc_enc(key, msg, iv):
    msg = padding(msg)
    cipher = b''
    aes = AES.new(key, AES.MODE_ECB)

    for i in range(int(len(msg) / 16)):
        xor = XOR.new(iv)
        xcipher = xor.encrypt(msg[i * 16:i * 16 + 16]) #xor with IV
        icipher = aes.encrypt(xcipher) #icipher is result of ECB
        cipher += icipher              # all the icipher add together is ciphertext
        iv = icipher                   #iv is updated with result from previous ECB
    return cipher

key = '\x00'*16
iv = '\x00'*16
msg = "\x00"*int(1.6*10**8)

start_time = datetime.now()
mycipher = hexlify(aes_cbc_enc(key,msg,iv))
print(mycipher)
time_elapsed = datetime.now() - start_time
print('time_elapsed for self implemented: ', time_elapsed)