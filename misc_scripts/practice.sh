#!/bin/bash
set -u


	Coins_Info=$1
		#Coins_Info="
		#	apt-1001-node-ali-hk-000,BTC:127.0.0.1+127.0.0.1-127.0.0.1+127.0.0.1#DAS:mainnet:127.0.01#LTC#SC#ZEC
		#  ;apt-1001-node-ali-hk-001,BTC:127.0.0.1+127.0.0.1-127.0.0.1+127.0.0.1#DAS#LTC#SC#ZEC"
		#BTC：- 前面为BTC gateway地址，后面2个为BCC gateway 地址


	Server_Info_Array=(${Coins_Info//;/ })
    echo ${Server_Info_Array[@]}

    for Server_Info in ${Server_Info_Array[@]}
    do
        coin_info_array=(${Server_Info//,/ })
        server=${coin_info_array[0]}
        echo $server
        coins=${coin_info_array[1]}
        coins_array=(${coins//#/ })

        for info in ${coins_array[@]}
    	do
    		echo $info

    	done

    done