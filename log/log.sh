#!/bin/bash
#####################################################################
# Written by Jeancarlo E. Hidalgo Ureña <jeancahu@gmail.com>,
#            Javier Darío León García <darox72leon@hotmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
########################################################################
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
