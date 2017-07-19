#!/bin/bash

echo 'Ejecutando ros_core_start.sh'

source ~/catkin_ws/devel/setup.bash && xstow -D $HOME/local/DIR/kdl && xstow -D $HOME/local/DIR/kdl-python && source /opt/ros/kinetic/setup.bash
roscore

exit 0
