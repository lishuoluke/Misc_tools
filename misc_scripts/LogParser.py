# Parse log search key words for the job status

import os

def parseBTC(file):

    check_notify = "{\"error\": null, \"result\": [[[\"mining.notify\","
    check_auth = "Auth success"
    check_submit = "Submit share success"
    notify_flag = 0
    auth_flag = 0
    submit_flag = 0

    with open(file, 'r') as f:

        data = f.readlines()
        for line in data:
            if check_notify in line:
                #print("BTC- Subscription is successful")
                notify_flag = 1
            if check_auth in line:
                #print("BTC- Authorization is successful")
                auth_flag = 1
            if check_submit in line and submit_flag == 0:
                #print("BTC - Share Submission is successful")
                submit_flag = 1


        if (notify_flag == 1 and auth_flag == 1 and submit_flag == 1):
            print("BTC -  Overall communication Successful")
        elif notify_flag == 0:
            print("BTC - Subscription failed")
        elif auth_flag == 0:
            print("BTC - authorization failed")
        elif submit_flag == 0:
            print("BTC - Submission failed")

##ParseLTC,ParseDASH.. will be added in the future

files = os.listdir(os.curdir)

for file in files:

    if file.startswith("BTC") and file.endswith(".txt"):
        print(file)
        parseBTC(file)
    #elif file.startswith("LTC") and file.endswith(".txt"):
    #    parsefile("LTC")
    elif file.endswith(".txt"):
        print ("This coin is not in the system - " + file)





