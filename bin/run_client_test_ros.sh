#!/bin/bash

case "$1" in
    -d|--daemon)
        $0 < /dev/null &> /dev/null & disown
        exit 0
        ;;
    *)
        ;;
esac

source ../include/HEAD

./config_ip.sh # Configura la IP 192.168.200.10

# Se ejectuta el script SSH_HAND-SH con el fin de hacer al servidor levantar el proceso escucha

echo "El directorio de HAND_SERVER es: $HAND_SERVER_DIR"
echo 'Ejecutando $ yarpserver start'
screen -d -m yarpserver start
sleep 4
echo "Ejecutando"' $ '"$HAND_SERVER_DIR""/ssh_hand.sh"
cd "$HAND_SERVER_DIR" # Visita el directorio de HAND_SERVER
screen -d -m  bash "./ssh_hand.sh"
sleep 10
echo "Ejecutando"' $ '"$HAND_SERVER_DIR""/hand_yarp"
nohup -d "./hand_yarp" &
sleep 1
sleep 1
cd - # Regresa a ./
echo "Ejecutando ./ros_core_start.sh"
screen -d -m bash "./ros_core_start.sh"
sleep 2
echo "Ejecutando ./run_server.sh"
nohup -d "./run_server.sh" &
sleep 1
sleep 1

source ~/catkin_ws/devel/setup.bash && xstow -D $HOME/local/DIR/kdl && xstow -D $HOME/local/DIR/kdl-python && source /opt/ros/kinetic/setup.bash
. ~/catkin_ws/devel/setup.bash
echo "Ejecutando ../src/client_test_ros.py"
python ../src/client_test_ros.py

sleep 2

exit 0
