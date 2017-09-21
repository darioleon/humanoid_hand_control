#!/usr/bin/env python

from hand_yarp_client import Hand
from time import sleep
import yarp as y
import rospy 
from hand_code.msg import Handmsg 
from hand_code.msg import Hand_info
from hand_code.srv import *

## GLOBAL VARS\n
##hand=Hand(2) 2 is the parameter for client arp port especifically for this server
hand=Hand(2)

def handle_server(req):
    """Intermittent server functions, recive a request parameter and excecute operation over hand"""
    """creates a topic called handData_pub and publish over it a finger data or all fingers data"""
    pub=rospy.Publisher('handData_pub', Hand_info) 
    rate=rospy.Rate(10)
    global hand
    
    #util vars
    time = 2
    
    command = req.var0
    print "------------------------"
    print "operation:", command
    
    if command == "getdata":
        hand.hand_in=hand.update_input()
        hand_resp=Hand_info()
        finger=req.var1
        hand_resp.finger=finger
        hand_resp.Enabled=hand.hand_in["Enabled"][finger]
        hand_resp.Pos[0]=hand.hand_in["Pos"][finger*3 + 0]
        hand_resp.Pos[1]=hand.hand_in["Pos"][finger*3 + 1]
        hand_resp.Pos[2]=hand.hand_in["Pos"][finger*3 + 2]
        hand_resp.Velocity[0]=hand.hand_in["Velocity"][finger*3 + 0]
        hand_resp.Velocity[1]=hand.hand_in["Velocity"][finger*3 + 1]
        hand_resp.Velocity[2]=hand.hand_in["Velocity"][finger*3 + 2]
        hand_resp.Torque[0]=hand.hand_in["Torque"][finger*3 + 0]
        hand_resp.Torque[1]=hand.hand_in["Torque"][finger*3 + 1]
        hand_resp.Torque[2]=hand.hand_in["Torque"][finger*3 + 2]
        pub.publish(hand_resp)
    elif command == "getall":
        hand.hand_in=hand.update_input()
        hand_resp=Hand_info()
        hand_resp.AllData=str(hand.hand_in)
        pub.publish(hand_resp)
    #hand.send_cmd() 
    return hand_serviceResponse("algo")


def server_ros():
    """Create server node called hand_server, creates the server handData_service and keep running the server in a loop"""
    rospy.init_node('handData_server', anonymous=True)
    s = rospy.Service('handData_service',hand_service, handle_server) ##Init ros service calling handle_server with hand_service object
    print "handData_server initialized"
    rospy.spin() ##cycling the listen client request



def main():
    """Main function caller of the function server_ros()""" 
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
