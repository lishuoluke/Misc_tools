import binascii as b
from collections import Counter

s = "161d0c56130b17493e2145625800514555596b52140116457942115d2c0b071b"
print len(s)


def strxor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

print (strxor(strxor(s.decode('hex'), "Student ID 1000000 gets 0 points"), "Student ID 1000000 gets 6 points").encode('hex'))