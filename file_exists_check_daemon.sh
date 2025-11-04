#!/bin/bash

filename=$1
seconds_to_timeout=$2

for second in $(seq 1 $seconds_to_timeout); do
	if [ -e $filename ]; then
		echo "File" $filename "arrived in server after" $second "seconds"
		exit
	fi
	sleep 1
done

echo "Timeout"
