#!/bin/bash

#PYTHON 环境准备
source /etc/profile
source /root/.bashrc

#定义变量
log_path='logs/mtasvr.log'
error_0=`cat config/error_no.txt`
error_1=`grep -ir error $log_path | wc -l`

#判断是否有新的错误日志信息，有新日志则发送邮件。
if [[ $error_1 > $error_0 ]]
then
#echo "OK"
grep -irnH error $log_path > content/html_all.txt
awk -v ERR="$error_0" '{L[NR]=$0}END{for(i=ERR+1;i<=NR;i++){print L[i]}}' content/html_all.txt > content/html.txt
/usr/bin/python eMail.py
else
echo "NO MORE ERROR !"
fi

#将最新的错误日志条目记录，供下一次判断参考
echo $error_1 > config/error_no.txt
