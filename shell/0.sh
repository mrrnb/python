#!/bin/bash

date +%Y.%m.%d | awk -F"." '{OFMT="%2"; print $1$2$3-1}'



date +%Y.%m.%d | awk -F"." '{if($3<10){printf("%s%s0%s\n",$1,$2,$3-1)}else{printf("%s%s%s\n",$1,$2,$3-1)}}'

month=`date +%m`
year=`date +%Y`
day=`date +%d`
yuedi=0
#case $month in
#	01) echo 31 ;;
#	02) echo 28 ;;
#	03) echo 31 ;;
#	04) echo 30 ;;
#	05) echo 31 ;;
#	06) echo 30 ;;
#	07) echo 31 ;;
#	08) echo 31 ;;
#	09) echo 30 ;;
#	10) echo 31 ;;
#	11) echo 30 ;;
#	12) echo 31 ;;
#esac
#if [ $month == "01" ];
if [[ $month =~ [01,03,05,07,08,10,12] ]]
then
	echo "31"
	yuedi=31
	echo $yuedi
elif [[ $month =~ [04,06,09,11] ]]
then
	echo "30"
	yuedi=30
	echo $yuedi
else
	if [ $(expr $year % 4) == "0" ]
	then
		if [ $(expr $year % 100) != "0" ] 
		then
        	echo "闰年29"
      	elif [ $(expr $year % 400) == "0" ]
         	then
         	echo "闰年29"
      	else 
         	echo "平年28" 
     	fi 
	else
		echo "平年28"
	fi
fi


if [[ $day == yuedi ]]
then
	if [[ $month == 12 ]]
	then
		echo $((year+1))"0101"
	else
		echo $year$((month+1))"01"
	fi
else
	printf $year$month"%1s"$((day+1))"\n" | sed "s/ /0/g"
fi
