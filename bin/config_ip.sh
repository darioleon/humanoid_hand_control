#!/bin/bash

if [ "$( ip a | grep -c 192.168.200.10 )" == "1" ]
then
	echo 'No es necesario cambiar la IP'
else
	echo 'Es necesario configurar la IP'
	sudo ifconfig eth0:0 192.168.200.10 netmask 255.255.255.0
fi

exit 0
