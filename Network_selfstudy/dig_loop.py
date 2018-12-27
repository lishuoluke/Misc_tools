import os
from time import sleep


ipadd = open ("test.dictionary","r")

content = ipadd.read()
print (content)
ip_list = content.splitlines()
data = {}
count_line = 0
for line in ip_list :
   command  = "dig " + line + " any @8.8.8.8 +recurse +bufsize=65535 +dnssec >> task2-2.tempfile"
   os.system(command)
   #os.system("`dig " +data[count_line][1] + "any @%s +recurse +bufsize=65535 +dnssec >> task2-2.tempfile" )