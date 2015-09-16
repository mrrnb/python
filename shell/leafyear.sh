#!/bin/bash
#  求闰年
echo "请输入要求的年份"
read year 

if [ $(expr $year % 4) == "0" ]
    then
      if [ $(expr $year % 100) != "0" ] 
         then
           echo "是闰年"
      elif [ $(expr $year % 400) == "0" ]
         then
         echo "是闰年"
      else 
         echo "不是闰年" 
     fi 
else
	echo "不是闰年"
fi


