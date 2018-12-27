# This one is to parse the CPU usage from the log

import os

seperator1 = ''
seperator2 = ''

with open('output.txt', 'r') as f:
    data = f.read()
strlist = data.split('9304 S')
for item in strlist[1:]:
    try:
        list_link = item.split(' 79')[0]
        print (list_link)
    except:
        pass