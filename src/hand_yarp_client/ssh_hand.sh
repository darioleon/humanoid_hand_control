#!/bin/bash
ardnet -ardiudp 30003 -ardoshm gui_in 1 -size 1000 &
ardnet -ardoudp 192.168.200.1 30004 -ardishm gui_out 1 -size 1000 &
ssh -t root@192.168.200.1 -Y /root/package/ard/bin/qnx-intel-gcc33/ardnet -ardoshm glove_input 1 -ardiudp 30005 -size 1000 &
ssh -t root@192.168.200.1 -Y /root/package/ard/bin/qnx-intel-gcc33/ardnet -ardoshm input_com 1 -ardiudp 30006 -size 1000 &
ssh -t root@192.168.200.1 -Y /root/package/ard/bin/qnx-intel-gcc33/ardnet  -ardishm force_feedback 1 -ardoudp 192.168.201.6 30007 &
ssh -t root@192.168.200.1 -Y /root/package/ard/bin/qnx-intel-gcc33/ardnet  -ardoshm com_gui 1 -ardiudp 30004 -size 1000 &
ssh -t root@192.168.200.1 -Y /root/package/ard/bin/qnx-intel-gcc33/ardnet  -ardishm out_gui 1 -ardoudp 192.168.200.10 30003 -size 1000 &
sleep 5
ssh -t root@192.168.200.1 -Y /root/package/./start_test_model.sh &

