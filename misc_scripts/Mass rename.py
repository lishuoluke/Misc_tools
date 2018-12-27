import shutil
from os import listdir
from os.path import isfile, join
import glob, os



mypath ='/opt/stratum_test_automation/SC'
for i in range (1,11):
    a = '/opt/stratum_test_automation/DAS/BTC'+ str(i) + '.py'
    b = '/opt/stratum_test_automation/DAS/DAS'+ str(i) + '.py'
    os.rename(a,b)