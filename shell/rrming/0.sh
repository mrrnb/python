#!/bin/bash

path=`awk -F' ' '/app/{print $8}' /etc/crontab`
mainpath=`awk -F' ' '/run/{print $8}' /etc/crontab| awk -F'/run' '{print $1}'| uniq`
#declare -a patharray
#declare -a mainpatharray

#arrayno=1
#for i in $path
#do
#    if [ ! -f "$i" ];then
#        printf "%-55s %s\n" $i 'not exist!'
#    else
#		patharray[$arrayno]=$i
#		arrayno=`expr $arrayno + 1`
#    fi
#done
#echo -e "${patharray[@]}"

#arrayno=1
#for i in $mainpath
#do
#		mainpatharray[$arrayno]=$i
#		arrayno=`expr $arrayno + 1`
#done
#echo ${mainpatharray[@]}

no=0
for i in $mainpath
do
	no=`expr $no + 1`
	echo $i
	path1[$no]=`echo -e "$path\n" | grep $i`
done

echo -e "${path1[1]}"
echo -e "${path1[2]}"
echo -e "${path1[3]}"
echo $no


#        if [[ $1 == "modify" ]];then
#            sed -i "$sedpara" $i
#        fi
#        printf "%-55s %s" $i `cat $i | grep Main.config`
#        echo
