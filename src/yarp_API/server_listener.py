#!/usr/bin/env python

from hand_yarp_client import Hand
from time import sleep
import yarp as y

def server_yarp():
    """Init yarp ports for communication /data_server/in and /data_server/out"""
    """Depending on the command it gets a finger data or all fingers data and send it through the port /data_server/out"""
    y.Network.init()
    portsrv_in = y.BufferedPortBottle()
    portsrv_in.open("/data_server/in")
    portsrv_out = y.BufferedPortBottle()
    portsrv_out.open("/data_server/out")
    
    #util vars
    time = 2
    
    #daemon code
    while(True):            
        bottle_in = portsrv_in.read()
        bottle_out = portsrv_out.prepare()
        command = bottle_in.get(0).asString()
        print command
        if command == "getdata":
            finger = bottle_in.get(1).asInt()
            hand.hand_in = hand.update_input()
            enabledVal=hand.hand_in["Enabled"][finger]
            handData=[]
            handData.append(hand.hand_in["Pos"][finger*3 + 0])
            handData.append(hand.hand_in["Pos"][finger*3 + 1])
            handData.append(hand.hand_in["Pos"][finger*3 + 2])
            handData.append(hand.hand_in["Velocity"][finger*3 + 0])
            handData.append(hand.hand_in["Velocity"][finger*3 + 1])
            handData.append(hand.hand_in["Velocity"][finger*3 + 2])
            handData.append(hand.hand_in["Torque"][finger*3 + 0])
            handData.append(hand.hand_in["Torque"][finger*3 + 1])
            handData.append(hand.hand_in["Torque"][finger*3 + 2])
            bottle_out.clear()
            bottle_out.addString("getdata")
            bottle_out.addInt(finger)
            bottle_out.addDouble(enabledVal)
            for i in range(0,9):
                bottle_out.addDouble(handData[i])
            portsrv_out.write()
        elif command == "getall":
            hand.hand_in = hand.update_input()
            allData = str(hand.hand_in)
            bottle_out.clear()
            bottle_out.addString("getall")
            bottle_out.addString(allData)
            portsrv_out.write()
            

if __name__ == "__main__":

    ##init hand
    ##hand=Hand(3) 3 is the parameter for client yarp port especifically for this server
    hand = Hand(4)
    hand.set_controller_mode(1)
    
    server_yarp()
