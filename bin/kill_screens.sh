#!/bin/bash

for i in $( screen -ls | egrep "Detached" | tr '\t' '#' | sed s/'#'/''/g| cut --delimiter='.' -f 1 )
do
	echo "kill $i"
	screen -X -S $i kill

done

exit 0
