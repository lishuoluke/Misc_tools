import os
import sys
import traceback
import pymysql
import re

#Serverlist

#'id', 'bigint(20)', 'NO', 'PRI', None, 'auto_increment')
#'share_oid', 'bigint(20)', 'NO', '', '-1', '')
#'node_oid', 'bigint(20)', 'NO', 'MUL', '-1', '')
#'user_worker_id', 'varchar(72)', 'YES', '', None, '')
#'user_oid', 'bigint(20)', 'NO', 'MUL', '-1', '')
#'remote_host', 'varchar(16)', 'YES', '', None, '')
#'block_height', 'int(11)', 'NO', 'MUL', '-1', '')
#'network_diff', 'bigint(20)', 'NO', 'MUL', '0', '')
#'payment_method', 'char(1)', 'NO', 'MUL', '0', '')
#'min_diff', 'int(11)', 'NO', '', '1', '')
#'speed', 'bigint(20)', 'NO', '', '0', '')
#'share1_count', 'int(11)', 'NO', '', '0', '')
#'stale1_count', 'int(11)', 'NO', '', '0', '')
#'dupe1_count', 'int(11)', 'NO', '', '0', '')
#'other1_count', 'int(11)', 'NO', '', '0', '')
#'diff_max', 'bigint(20)', 'NO', '', '0', '')
#'time_space', 'int(11)', 'NO', '', '0', '')
#'type', 'char(1)', 'NO', '', '0', '')
#'status', 'char(1)', 'NO', 'MUL', '0', '')
#'pay_flag', 'char(1)', 'NO', 'MUL', '0', '')
#'create_time', 'timestamp', 'NO', 'MUL', 'CURRENT_TIMESTAMP', '')


db = pymysql.connect("serverip", "username", "password", "bpsdb2_ltc", charset='utf8')
cursor = db.cursor()
cursor.execute("select user_worker_id,speed,create_time from t_user_share where user_worker_id like 'gxl%' ")
#cursor.execute("select user_worker_id,speed from t_user_share")
#cursor.execute("describe t_user_worker")
#cursor.execute("select user_worker_id,speed,create_time from t_user_share ")
for row in cursor:
    print (row)
cursor.close()
db.commit()
db.close()