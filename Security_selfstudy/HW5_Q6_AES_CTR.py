from binascii import unhexlify
def numToWord(n):
    hexvalue = hex(n)[2:]
    return "".join([chr(int(s, 16)) for s in [hexvalue[i:i+2] for i in range(0,len(hexvalue),2)]])




C  = 0x4664DC0697BBFE69330715079BA6C23D
Ct = 0x517ECC05C3BDEA3B33570E1BD897D530
P  = 0x43727970746F67726170687920437279

K_string = hex(C ^ P)
print (K_string)


K = 0x516a576e3d4991b52777d7ebbe5b044

Pt = hex(Ct ^ K)

print(Pt)

Pt = 0x54686973206973206120736563726574

print (numToWord(Pt))

