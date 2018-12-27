import random

import collections

import matplotlib.pyplot as plt

numberlist = []

for i in range(0, 512):
    number = random.getrandbits(8)

    numberlist.append(number % 128)

counter = collections.Counter(numberlist)

print(counter)

plt.hist(numberlist, bins=128)

plt.ylabel("Frequency")

plt.show()