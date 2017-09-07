#!/usr/bin/env python

from hand_yarp_client import Hand
from time import sleep
import yarp as y
import rospy 
from hand_code.msg import Handmsg 
from hand_code.msg import Hand_info
from hand_code.srv import *

##GLOBAL VARS 
hand=Hand(1) ## 1 is the parameter for client yarp port especifically for this server  

def handle_server(req):
    """Intermittent server functions, recive a request parameter and execute operation over hand"""
    pub=rospy.Publisher('serverclient', Hand_info) 
    rate=rospy.Rate(10) 
    #global hand
    
    #util vars
    time = 2

    
    command = req.var0
    print "------------------------"
    print "operation:", command
    if command == "enable": 
        finger = req.var1
        print "finger:", finger
        hand.enable(finger)
        hand_serviceResponse("done")
    elif command == "enabled":
        finger = req.var1
        print "finger:", finger
        hand_resp=Hand_info()
        hand_resp.Enabled = hand.enabled(finger)
        pub.publish(hand_resp)
        hand_serviceResponse("done")
    elif command == "enableall":
        hand.enable_all()
        hand_serviceResponse("done")
    elif command == "disable":
        finger = req.var1
        print "finger:", finger
        hand.disable(finger)
        hand_serviceResponse("done")
    elif command == "setcontroller":
        mode = req.var1
        print "mode:", mode
        hand.set_controller_mode(mode)
        hand_serviceResponse("done")
    elif command == "setpos":
        finger = req.var1
        joint = req.var2
        pos = req.var3
        print "finger:", finger 
        print "joint:", joint 
        print "position:", pos
        hand.set_pos(finger, joint, pos)
        hand_serviceResponse("done")
    elif command == "setdamp":
        finger = req.var1
        joint = req.var2
        damp = req.var3
        print "finger:", finger 
        print "joint:", joint 
        print "damping:", damp
        hand.set_damping(finger, joint, damp)
        hand_serviceResponse("done")
    elif command == "setstiff":                
        finger = req.var1
        joint = req.var2
        stiff = req.var3
        print "finger:", finger 
        print "joint:", joint 
        print "stiffness:", stiff
        hand.set_stiffness(finger, joint, stiff)
        hand_serviceResponse("done")
    elif command == "setvel":
        finger = req.var1
        joint = req.var2
        vel = req.var3
        print "finger:", finger 
        print "joint:", joint 
        print "velocity:", vel
        hand.set_velocity(finger, joint, vel)
        return hand_serviceResponse("done")
   # elif command == "gettorque":
    #    hand.hand_in = hand.update_input()
     #   hand_resp = Hand_info()
      #  finger = req.var1
       # hand_resp.finger=finger
       # hand_resp.Torque[0]=hand.hand_in["Torque"][finger*3 + 0]
       # hand_resp.Torque[1]=hand.hand_in["Torque"][finger*3 + 1]
       # hand_resp.Torque[2]=hand.hand_in["Torque"][finger*3 + 2]
    elif command == "updinp":
        hand.hand_in=hand.update_input()
        hand_serviceResponse("done")
    elif command == "sendcmd":
        hand.send_cmd()
        hand_serviceResponse("done")
    elif command == "update":
        time = req.var1
        print "time:", time
        hand.update(time)
        hand_serviceResponse("done")
    hand.send_cmd() 
    return hand_serviceResponse("done")


def server_ros():
    """Create server node called hand_server"""
    rospy.init_node('hand_server', anonymous=True) 
    s = rospy.Service('server',hand_service, handle_server) ##Init ros service calling handle_server with hand_service object 
    print "server initialized"
    rospy.spin() ##cycling the listen client request



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
