#!/bin/bash
set -e


	Coins_Info=$1
		# apt-1001-node-ali-hk-001,BTC#DAS#LTC#SC#ZEC



	Array_1=(${Coins_Info//,/ })
	echo ${Array_1[@]}

    test=${Array_1[1]}

    test1=(${test//#/ })
    echo $test1
    for coin in ${test1[@]}
    do
    echo $coin
    done