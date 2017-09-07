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
        elif command == "gettorque":
            finger = bottle_in.get(1).asInt()
            joint = bottle_in.get(2).asInt()
            torque = bottle_in.get(3).asDouble()
            print finger 
            print joint 
            print torque
            hand.hand_in = hand.update_input()
            handData=[]
            val=hand.hand_in["Torque"][finger*3+joint]
            bottle_out.clear()
            bottle_out.addDouble(val)
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
            print "sendcmd"
            hand.send_cmd()
        elif command == "update":
            print "update"
            time = bottle_in.get(1).asInt()
            hand.update(time)
        hand.send_cmd()
        #sleep(0.1)


if __name__ == "__main__":

    #init hand.
    hand = Hand(3)
    hand.set_controller_mode(1)
    
    server_yarp()


