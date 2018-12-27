import sys
import threading
from time import sleep

import os

def PrintFucntion():
    while True:
        print ("hello")
        sleep(1)

def timer():
    for i in range (0,9):
        print("peppa")
        sleep(1)
    sys.exit(0)

t2= threading.Thread(target=PrintFucntion)
t2.setDaemon(True)
t2.start()
t2.join(3)




