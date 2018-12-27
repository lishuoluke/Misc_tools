# This script is searching for keywords in a flder and tell which file contain the word

import os
import re
s = os.sep
def walkFiles(root,string):
    for dirpath,dirname,filename in os.walk(root):
        for fn in filename:
          try:
            name =dirpath + s + fn
            print ("Searcing file '" + name  + "'...")
            flag =0
            fp = open(name,'r')
            count  = 0
            for line in fp.readlines():
                count +=1
                if string in line:
                   flag =1
                   print ("Yourstring is in file '" + name + "' line " + str(count))
                if flag == 0:
                    print ("NotFound")
          except:
              print ("not find")


def main():

    root ='/Users/lishuo/PycharmProjects/Scripts/'

    string ='9304 S'

    walkFiles(root,string)

    print("Done")

if __name__ == "__main__":
    main()