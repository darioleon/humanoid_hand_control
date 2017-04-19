#!/usr/bin/env python

from hand_yarp_client import Hand
from time import sleep
import yarp as y
import rospy #puede que la persona no tenga rospy, entonces es error
from hand_code.msg import Handmsg #lo mismo de arriba
from hand_code.msg import Hand_info
from hand_code.srv import *

### GLOBAL VARS ###

hand=Hand()

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
        
#
#
#
#
def handle_server(req):

    pub=rospy.Publisher('serverclient', Hand_info)
    rate=rospy.Rate(10)
    global hand
    
    #util vars
    time = 2

    
    command = req.var0
    print "------------------------"
    print "operation:", command
    if command == "enable":
        finger = req.var1
        print "finger:", finger
        hand.enable(finger)
        hand_serviceResponse("algo")
    elif command == "enabled":
        finger = req.var1
        print "finger:", finger
        hand_resp=Hand_info()
        hand_resp.Enabled = hand.enabled(finger)
        pub.publish(hand_resp)
        hand_serviceResponse("algo")
    elif command == "enableall":
        hand.enable_all()
        return hand_serviceResponse("algo")
    elif command == "disable":
        finger = req.var1
        print "finger:", finger
        hand.disable(finger)
        hand_serviceResponse("algo")
    elif command == "setcontroller":
        mode = req.var1
        print "mode:", mode
        hand.set_controller_mode(mode)
        return hand_serviceResponse("algo")
    elif command == "setpos":
        finger = req.var1
        joint = req.var2
        pos = req.var3
        print "finger:", finger 
        print "joint:", joint 
        print "position:", pos
        hand.set_pos(finger, joint, pos)
        hand_serviceResponse("algo")
    elif command == "setdamp":
        finger = req.var1
        joint = req.var2
        damp = req.var3
        print "finger:", finger 
        print "joint:", joint 
        print "damping:", damp
        hand.set_damping(finger, joint, damp)
        return hand_serviceResponse("algo")
    elif command == "setstiff":                
        finger = req.var1
        joint = req.var2
        stiff = req.var3
        print "finger:", finger 
        print "joint:", joint 
        print "stiffness:", stiff
        hand.set_stiffness(finger, joint, stiff)
        return hand_serviceResponse("algo")
    elif command == "setvel":
        finger = req.var1
        joint = req.var2
        vel = req.var3
        print "finger:", finger 
        print "joint:", joint 
        print "velocity:", vel
        hand.set_velocity(finger, joint, vel)
        return hand_serviceResponse("algo")
    elif command == "updinp":
        hand.hand_in=hand.update_input()
        return hand_serviceResponse("algo")
    elif command == "sendcmd":
        hand.send_cmd()
        return hand_serviceResponse("algo")
    elif command == "update":
        time = req.var1
        print "time:", time
        hand.update(time)
        hand_serviceResponse("algo")
    elif command == "gettorque":
        hand.hand_in=hand.update_input()
        hand_resp=Hand_info()
        finger=req.var1
        hand_resp.finger=finger
        hand_resp.Enabled=hand.hand_in["Enabled"][finger]
        hand_resp.Torque[0]=hand.hand_in["Torque"][finger*3 + 0]
        hand_resp.Torque[1]=hand.hand_in["Torque"][finger*3 + 1]
        hand_resp.Torque[2]=hand.hand_in["Torque"][finger*3 + 2]
        pub.publish(hand_resp)
        hand_serviceResponse("algo")
    elif command == "getpos":
        hand.hand_in=hand.update_input()
        hand_resp=Hand_info()
        finger=req.var1
        hand_resp.finger=finger
        hand_resp.Enabled=hand.hand_in["Enabled"][finger]
        hand_resp.Pos[0]=hand.hand_in["Pos"][finger*3 + 0]
        hand_resp.Pos[1]=hand.hand_in["Pos"][finger*3 + 1]
        hand_resp.Pos[2]=hand.hand_in["Pos"][finger*3 + 2]
        pub.publish(hand_resp)
        return hand_serviceResponse("algo")
    elif command == "getvelocity":
        hand.hand_in=hand.update_input()
        hand_resp=Hand_info()
        finger=req.var1
        hand_resp.finger=finger
        hand_resp.Enabled=hand.hand_in["Enabled"][finger]
        hand_resp.Velocity[0]=hand.hand_in["Velocity"][finger*3 + 0]
        hand_resp.Velocity[1]=hand.hand_in["Velocity"][finger*3 + 1]
        hand_resp.Velocity[2]=hand.hand_in["Velocity"][finger*3 + 2]
        pub.publish(hand_resp)
    hand.update(time) 
    return hand_serviceResponse("algo")


def server_ros():
    rospy.init_node('hand_server', anonymous=True)
    s = rospy.Service('server',hand_service, handle_server)
    print "server initialized"
    rospy.spin()



def main():

    #init hand.

    hand.set_controller_mode(1)
    
    #server_yarp()
    try:
        server_ros()
    except rospy.ROSInterruptException:
        return 1
    return 0

if __name__ == "__main__":
    main()
