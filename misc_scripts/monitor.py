import os
from time import sleep

for i in range (0,5):
    os.system("top -pid 9315 >>output.txt")
    sleep(5)
    print (i)