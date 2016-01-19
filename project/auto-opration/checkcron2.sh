#!/bin/bash
# Author: Ezreal
# Date: 20151119
# Version: 1.2

# 获取文件路径信息，并识别不同文件路径开头
path=`awk -F' ' '/app/{print $8}' /etc/crontab`
mainpath=`awk -F' ' '/run/{print $8}' /etc/crontab| awk -F'/run' '{print $1}'| uniq`
declare -a patharray

# 检测及修改操作的不同打印
if [[ $1 == "modify" ]];then
	echo -e '\033[40;31;1m### 执行修改操作\033[0m'
else
	echo -e '\033[40;31;1m### 执行检测操作（若要进行修改，请加modify参数）\033[0m'
fi

# 主程序
no=0
for i in $mainpath
do
	# 根据不同的路径开头, 分别创建不同的php文件数组
	no=`expr $no + 1`
	patharray[$no]=`echo -e "$path\n" | grep $i`
	mainconfpath="$i/config/Main.config.inc"

	# 来检测php文件的正确性及修改操作
	for i in ${patharray[$no]}
	do
		# 判断文件是否存在，不存在则跳过检测及修改
		if [ ! -f "$i" ];then
			printf "%-55s %s\n" $i 'not exist!'
		else
			# 过滤出整行，适配各种不同内容的整行, 给sed作为参数使用
			include=`cat $i | grep Main.config`
			if [[ $1 == "modify" ]];then
				# 设置修改操作中的sed命令参数, 替换过滤出的整行
				sedpara="s:$include:include_once '$mainconfpath';:g"
				sed -i "$sedpara" $i
			fi  
			# 检查打印php文件内容
			printf "%-55s %s" $i `cat $i | grep Main.config`
			echo
		fi  
	done
done
