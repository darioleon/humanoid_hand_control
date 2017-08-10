#!/usr/bin/env python

from hand_yarp_client import Hand
from time import sleep
import yarp as y

def server_yarp():
    
    #init yarp ports for comm
    y.Network.init()
    portsrv_in = y.BufferedPortBottle()
    portsrv_in.open("/server/in")
    portsrv_out = y.BufferedPortBottle()
    portsrv_out.open("/server/out")
    
    #util vars
    time = 2
    
    #daemon code
    while(True):            
        bottle_in = portsrv_in.read()
        bottle_out = portsrv_out.prepare()
        command = bottle_in.get(0).asString()
        print command
        if command == "enable":
            finger = bottle_in.get(1).asInt()
            print finger
            hand.enable(finger)
        elif command == "enabled":
            finger = bottle_in.get(1).asInt()
            val = hand.enabled(finger)
            bottle_out.clear()
            bottle_out.addDouble(val)
            portsrv_out.write()
        elif command == "getdata":
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
        elif command == "enableall":
            hand.enable_all()
        elif command == "disable":
            finger = bottle_in.get(1).asInt()
            print finger
            hand.disable(finger)
        elif command == "setcontroller":
            mode = botlle_in.get().asInt()
            print mode
            hand.set_controller_mode(mode)
        elif command == "setpos":
            finger = bottle_in.get(1).asInt()
            joint = bottle_in.get(2).asInt()
            pos = bottle_in.get(3).asDouble()
            print finger 
            print joint 
            print pos
            hand.set_pos(finger, joint, pos)
        elif command == "setdamp":
            finger = bottle_in.get(1).asInt()
            joint = bottle_in.get(2).asInt()
            damp = bottle_in.get(3).asDouble()
            print finger 
            print joint 
            print damp
            hand.set_damping(finger, joint, damp)
        elif command == "setstiff":                
            finger = bottle_in.get(1).asInt()
            joint = bottle_in.get(2).asInt()
            stiff = bottle_in.get(3).asDouble()
            print finger 
            print joint 
            print stiff
            hand.set_stiffness(finger, joint, stiff)
        elif command == "setvel":
            finger = bottle_in.get(1).asInt()
            joint = bottle_in.get(2).asInt()
            vel = bottle_in.get(3).asDouble()
            print finger 
            print joint 
            print vel
            hand.set_velocity(finger, joint, vel)
        elif command == "updinp":
            hand.update_input()
        elif command == "sendcmd":
            hand.send_cmd()
        elif command == "update":
            time = bottle_in.get(1).asInt()
            hand.update(time)
        hand.update(time)

            

if __name__ == "__main__":

    #init hand.
    hand = Hand(4)
    hand.set_controller_mode(1)
    
    server_yarp()
