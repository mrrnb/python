#!/bin/bash


host_list="10.10.28.228 10.10.106.54"
#echo $host_list | while read line
for line in $host_list
do
	echo $line
	host=$line
	password="5rdx&YGVCF"
	port=22
	user=root
	source_dir=/root/github/python/project/auto-opration/
	target_dir=/script/rrming/

	./load.sh $host $password $port $user $source_dir $target_dir
done

