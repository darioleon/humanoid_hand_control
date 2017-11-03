#!/usr/bin/env python

from hand_yarp_client import Hand
from time import sleep
import yarp as y

def get_functions(command, bottle_in, bottle_out, portsrv_out):
    """This function runs when the client asks for getting hand data: torque, position, velocity or all data"""
    if command == "gettorque":
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
    elif command == "getvel":
        finger = bottle_in.get(1).asInt()
        joint = bottle_in.get(2).asInt()
        vel = bottle_in.get(3).asDouble()
        print finger 
        print joint 
        print torque
        hand.hand_in = hand.update_input()
        handData=[]
        val=hand.hand_in["Velocity"][finger*3+joint]
        bottle_out.clear()
        bottle_out.addDouble(val)
        portsrv_out.write()
    elif command  == "getpos":
        finger = bottle_in.get(1).asInt()
        joint = bottle_in.get(2).asInt()
        pos = bottle_in.get(3).asDouble()
        print finger 
        print joint 
        print torque
        hand.hand_in = hand.update_input()
        handData=[]
        val=hand.hand_in["Pos"][finger*3+joint]
        bottle_out.clear()
        bottle_out.addDouble(val)
        portsrv_out.write()
    elif command == "getdata":
        hand.hand_in = hand.update_input()
        bottle_out.clear()
        bottle_out.addString(str(hand.hand_in))
        portsrv_out.write()

def set_functions(command, bottle_in, bottle_out):
    """This function runs when the client sends data to the hand: position, controller, damping, velocity, stiffness"""
    if command == "setpos":
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
    elif command == "setcontroller":
        mode = botlle_in.get().asInt()
        print mode
        hand.set_controller_mode(mode)

        
def server_yarp():
    """Init yarp ports for communication /server/in and /server/out"""
    """Depending on the command excecutes a function of the object Hand"""
    """The command is obtained through the port /server/in"""
    """The result of get type command is sent through the port /server/out"""
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
        command_type = command.split("t")[0]
        if command_type == "se":
            set_functions(command, bottle_in, bottle_out)
        elif command_type == "ge":
            get_functions(command, bottle_in, bottle_out, portsrv_out)
        elif command == "enable":
            finger = bottle_in.get(1).asInt()
            print finger
            hand.enable(finger)
        elif command == "enabled":
            finger = bottle_in.get(1).asInt()
            val = hand.enabled(finger)
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

    ##init hand
    ##hand=Hand(3) 3 is the parameter for client yarp port especifically for this server
    hand = Hand(6)
    hand.set_controller_mode(1)
    
    server_yarp()


