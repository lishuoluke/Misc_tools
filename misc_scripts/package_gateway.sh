#!/bin/bash
#打包各币种
set -xue
function packageSource() 
{
	#以下是python 编写的网关程序，币种有：btc，bcc,注：BTC，BCC 共用一套程序
	mkdir ${WORKSPACE}/antpool-mining-gateway-python
	array=(btc)
	cd  ${WORKSPACE}
	#打包挖矿程序
	for coin in ${array[@]}
	do     		
    	tar -czf antpool-mining-gateway-python/antpool-mining-gateway-$coin.tar.gz antpool-mining-gateway-$coin
	done
	#打包部署脚本
	tar -zcf TestEnvDeployer.tar.gz TestEnvDeployer	
}


function distributeSource()
{
	host=$1
	coin_type=`echo $2 | tr 'A-Z' 'a-z'`
	if [ "$coin_type" == "bcc" ];then
		coin_type=btc
	fi
	cd  ${WORKSPACE}	
	#拷贝文件到节点机器
	ssh ${host} "mkdir -p /deploy/antpool-mining-gateway-python"
	ssh ${host} "rm -fr /deploy/antpool-mining-gateway-python/antpool-mining-gateway-${coin_type}*"
	ssh ${host} "rm -fr /deploy/TestEnvDeployer*"
	scp antpool-mining-gateway-python/antpool-mining-gateway-${coin_type}.tar.gz ${host}:/deploy/antpool-mining-gateway-python/antpool-mining-gateway-${coin_type}.tar.gz
	scp TestEnvDeployer.tar.gz ${host}:/deploy/TestEnvDeployer.tar.gz
	ssh ${host} "tar -C /deploy/antpool-mining-gateway-python/ -zxf /deploy/antpool-mining-gateway-python/antpool-mining-gateway-${coin_type}.tar.gz"
	ssh ${host} "tar -C /deploy/ -zxf /deploy/TestEnvDeployer.tar.gz"
}





	packageSource
	Coins_Info=$1
		#Coins_Info="apt-1001-node-ali-hk-000,BTC:mainnet:127.0.0.1+127.0.0.2-BCC:mainnet:127.0.0.1+127.0.0.2
		#			;apt-1001-node-ali-hk-000,BTC:mainnet:127.0.0.1+127.0.0.2-BCC:mainnet:127.0.0.1+127.0.0.2"
					
	Coins_Info_Array=(${Coins_Info//;/ })
    for Coin_Info in ${Coins_Info_Array[@]}
    do
        Coin_Info_Array=(${Coin_Info//,/ })
        host=${Coin_Info_Array[0]}
        coin_info=${Coin_Info_Array[1]} 
        	# BTC:mainnet:127.0.0.1+127.0.0.2-BCC:mainnet:127.0.0.1+127.0.0.2
        btc_distributed=0
        coin_info_array=(${coin_info//-/ })
    	for info in ${coin_info_array[@]}
    	do
    		info_array=(${info//:/ })
    		coin=${info_array[0]}
    		server_net=${info_array[1]}
    		address=${info_array[2]}
    		echo "coin=$coin"
    		echo "server_net=$server_net"
    		echo "address=$address"
    		if [ "$coin" == "BTC" -o "$coin" == "BCC" ];then
    			if [ $btc_distributed == 0 ];then
    				echo "Coin=$coin"
    				echo "distributed BTC on ${host}"
    				distributeSource ${host} BTC
    				btc_distributed=1
    			else
    				echo "BTC have been distributed,so skip it"
    			fi    			     			
    		else
    			distributeSource ${host} ${coin}
    		fi
    		ssh ${host} "bash /deploy/TestEnvDeployer/miningserver/gatewayDeployer.sh $coin $server_net $address"
    	done 
    	                                    
    done
    










