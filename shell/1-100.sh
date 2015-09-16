#!/bin/bash

s=0
for i in {1..100}
do
s=$((i+s))
done
echo $s
