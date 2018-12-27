from Crypto.Util import number
import matplotlib.pyplot as plt
from datetime import datetime
from timeit import default_timer as timer


class RSA(object):
    def Gen(minPrime):
        p = number.getPrime(minPrime)
        q = number.getPrime(minPrime)

        while q == p:
            q = number.getPrime(minPrime)
        n = p * q
        phi = (p - 1) * (q - 1)
        bits = int(minPrime / 2)
        e = 2 ** (bits) - 1
        d = number.inverse(e, phi)
        return (n, e), (p, q, phi, d)

    def Gen1(minPrime):
        p = number.getPrime(minPrime)
        q = number.getPrime(minPrime)

        while q == p:
            q = number.getPrime(minPrime)
        n = p * q
        phi = (p - 1) * (q - 1)

        e = 65537
        d = number.inverse(e, phi)
        return (n, e), (p, q, phi, d)

    def Enc(pk, plain):
        n, e = pk
        cipher = (plain ** e) % n
        # pow(cipher,d,n)
        return cipher

    def Dec(pk, cipher):
        p, q, phi, d = pk
        n = p * q
        plain = (cipher ** d) % n
        # pow(cipher,d,n)
        return plain


def showfig(bits, time, keylen):
    plt.xlabel('message bit-length')
    plt.ylabel('time')
    plt.title('For keylength of bits: ' + str(keylen))
    plt.plot(bits, time)
    plt.show()


def showfigdiffcont(bits, time, keylen):
    plt.xlabel('No. of 1s')
    plt.ylabel('time')
    plt.title('For messagelength 1024bit keylength of bits: ' + str(keylen))
    plt.plot(bits, time)
    plt.show()


# showing that longer messages will take longer to encrypt
pubkey, prikey = RSA.Gen1(512)
print(pubkey)
print(prikey)

msgtime = []
msgbits = []
for i in range(16, 512 * 10 + 16, 16):
    msg = 2 ** i - 1
    start_time = timer()
    s1 = RSA.Enc(pubkey, i)
    time_elapsed = timer() - start_time
    msgtime.append(time_elapsed)
    msgbits.append(i)
showfig(msgbits, msgtime, 512)
# showing that longer messages will take longer to encrypt

# showing that different content will take longer to encrypt
pubkey, prikey = RSA.Gen1(512)
print(pubkey)
print(prikey)

msgtime = []
msgbits = []
msg1 = 2 * 1024 - 1
print(bin(msg1))
for i in range(16, 512, 1):
    msg = msg1 ^ (2 ** i - 1)
    start_time = timer()
    s1 = RSA.Enc(pubkey, i)
    time_elapsed = timer() - start_time
    msgtime.append(time_elapsed)
    msgbits.append(bin(msg).count("1"))
showfigdiffcont(msgbits, msgtime, 512)
# showing that different content will take longer to encrypt

# showing that longer key will take longer to encrypt
keybits = [16, 24, 32]
keys = []
for key in keybits:
    keys.append([RSA.Gen(key), key])

print(keys)

for key in keys:
    bits = []
    time = []
    for i in range(16, 8192, 16):
        msg = 2 ** i - 1
        start_time = timer()
        s1 = RSA.Enc(key[0][0], i)
        time_elapsed = timer() - start_time
        time.append(time_elapsed)
        bits.append(i)
    showfig(bits, time, key[1])
    # showing that longer key will take longer to encrypt