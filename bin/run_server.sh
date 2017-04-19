#!/bin/bash

echo 'Ejecutando run_server.sh'

source ~/catkin_ws/devel/setup.bash && xstow -D $HOME/local/DIR/kdl && xstow -D $HOME/local/DIR/kdl-python && source /opt/ros/kinetic/setup.bash

python ../src/server_sm.py

exit 0
