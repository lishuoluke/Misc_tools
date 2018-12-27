from Crypto.Cipher import AES

def aes_enc(key, msg):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(msg)

key = '\x00'*16
infile = open('BLK.BMP','rb').read()
infile = infile + (16 -(len(infile)%16))*b'\x00'
outfile = open('BLK.ENC','wb')
outfile.write(aes_enc(key,infile))
