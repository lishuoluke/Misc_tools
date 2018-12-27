# This script can simulate the press button function of keyboard

import threading
import signal
import subprocess

while True:
    n = input("give your word")
    if n == "2":
        continue
    if n == "1":
        process = subprocess.Popen(1)
        process.send_signal(signal.SIGINT)