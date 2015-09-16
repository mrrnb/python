#!/bin/bash
j=0
k=99
echo -e "5,81,2,38,91,66\n"
for i in {5,81,2,38,91,66}

do
	if [[ $i > $j ]]
	then
		j=$i
	fi
	if [[ $i < $k ]]
	then
		k=$i
	fi
done
echo -e "The small one is $k, and the big one is $j\n"
