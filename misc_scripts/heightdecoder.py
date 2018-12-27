from binascii import b2a_hex



def encodeUNum(n):
 s = bytearray(b'\1')
 while n > 127:
  s[0] += 1
  s.append(n % 256)
  n //= 256
 s.append(n)
 print (s)
 return bytes(s)


def decodeUNum(n):
    number = 0
    s = bytes.fromhex(n)
    for i in range(1,4):
        number = number + s[i] * (256**(i-1))
    return str(number)

#print (b2a_hex(encodeUNum(556460)))
#print (b2a_hex(encodeUNum(556460)))
#print (b2a_hex(encodeUNum(556460)).decode("utf8"))
#print (codeUNum('03ac7d08'))

decodeUNum('037e6508')

#037e6508