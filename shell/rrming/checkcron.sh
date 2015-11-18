#!/bin/bash
# Author: Ezreal
# Date: 2015.11.17
mainconfpath='/app/www/app/config/Main.config.inc'
sedpara="s/include_once '..\/config\/Main.config.inc';/include_once '\/app\/www\/app\/config\/Main.config.inc';/g"
path=`cat /etc/crontab | grep /app/run | awk -F' ' '{print $8}'`

for i in $path
do
	if [ -e $i ];then
		if [[ $1 == "sed" ]];then
			sed -i "$sedpara" $i
		fi
		printf "%-55s" $i
		echo `cat $i | grep "include_once '$mainconfpath';"`
	fi
done
