#!/bin/bash

LOG_DIR='/home/robot/catkin_ws/src/hand_code/log/'


if [ "$( echo $* | egrep -c '^\-h$' )" = "1" ]
then
	echo 'Usage:	$ logclarissa [TEXT]'
	echo '	$ logclarissa -h	# Show this message'
	echo '	$ logclarissa -s	# Show the log'
	echo '	$ logclarissa -w	# Open the log over text editor'
	exit 0
elif [ "$( echo $* | egrep -c '^\-s$' )" = "1" ]
then
	less "$LOG_DIR""$( date | sed s/' \{2,4\}'/' '/g | cut -f 1,2,3,6 --delimiter=' ' | tr ' ' '_' ).txt"
	exit 0
elif [ "$( echo $* | egrep -c '^\-w$' )" = "1" ]
then
	nano "$LOG_DIR""$( date | sed s/' \{2,4\}'/' '/g | cut -f 1,2,3,6 --delimiter=' ' | tr ' ' '_' ).txt"
	exit 0
fi

echo "$( date | sed s/' \{2,4\}'/' '/g | cut -f 4 --delimiter=' ' ) : $*" >> "$LOG_DIR""$( date | sed s/' \{2,4\}'/' '/g | cut -f 1,2,3,6 --delimiter=' ' | tr ' ' '_' ).txt"



exit 0
