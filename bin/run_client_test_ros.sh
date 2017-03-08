#!/bin/bash

source ../include/HEAD

./config_ip.sh # Configura la IP 192.168.200.10

# Se ejectuta el script SSH_HAND-SH con el fin de hacer al servidor levantar el proceso escucha

echo "El directorio de HAND_SERVER es: $HAND_SERVER_DIR"
bash "$HAND_SERVER_DIR""/ssh_hand.sh"
sleep 1
xfce4-terminal --command="yarpserver start"
sleep 4
xfce4-terminal --command="$HAND_SERVER_DIR""/hand_yarp"
#xfce4-terminal --command='ros-init' --working-directory="$HOME""/catkin_ws" /catkin_ws
#xfce4-terminal --command="yarpserver start"
