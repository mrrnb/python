#!/bin/bash
# Author: Ezreal
# Date: 2015.11.17

# 从crontab中获取php文件路径，并打印
path=`cat /etc/crontab | grep /app/run | awk -F' ' '{print $8}'`
echo -e "\033[40;31;1m### 从crontab中获取的php文件路径:\n\033[0m$path"

# 从crontab中获取路径信息，便于后续检测及修改操作
mainpath=`cat /etc/crontab | grep /app/run | awk -F' ' '{print $8}' | awk -F'/run' '{print $1}'| uniq`
mainconfpath="$mainpath/config/Main.config.inc"

# 设置修改操作中的sed命令参数
sedpara="s:include_once '../config/Main.config.inc';:include_once '$mainconfpath';:g"

#  检测及修改操作的不同打印
if [[ $1 == "modify" ]];then
	echo -e '\033[40;31;1m### 执行修改操作\033[0m'
else
	echo -e '\033[40;31;1m### 执行检测操作（若要进行修改，请加modify参数）\033[0m'
fi

# 主程序，用来检测php文件的正确性及修改操作
for i in $path
do
	tuichu=0
	if [ ! -f "$i" ];then
		printf "%-55s %s\n" $i 'not exist!'
	else
		if [[ $1 == "modify" ]];then
			sed -i "$sedpara" $i
		fi
		printf "%-55s %s" $i `cat $i | grep Main.config`
		echo
	fi
done
