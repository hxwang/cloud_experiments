#!/bin/bash
for i in {1..10000}
do
	ts=`date -u`
	wget -q target-ip -O index.html
	echo "$ts, $i"	
	sleep 1

done
