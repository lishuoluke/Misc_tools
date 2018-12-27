import importlib
import sys
import json
import os
import datetime
import shutil
from datetime import datetime

mydir = "/opt/stratum_test_automation"+ "/" + "Logs"
if os.path.exists(mydir):
    print("hello")
    dt = datetime.now()
    strg = '{:%B %d, %Y}'.format(dt)
    os.rename(mydir,mydir+'_bak_'+strg)
else:
    print("not there")
    os.makedirs(mydir)

