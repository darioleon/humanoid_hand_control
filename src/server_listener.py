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
