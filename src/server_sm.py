#!/usr/bin/env python

from hand_yarp_client import Hand
from time import sleep
import yarp as y
import rospy 
from hand_code.msg import Handmsg 
from hand_code.msg import Hand_info
from hand_code.srv import *

##GLOBAL VARS\n
##hand=Hand(1) 1 is the parameter for client yarp port especifically for this server  
hand=Hand(1)

def handle_server(req):
    """This function runs for other kind of commands: enable, disable, updates and executions""" 
    command = req.var0
    print "------------------------"
    if command == "enable": 
        finger = req.var1
        rospy.loginfo(
            "command: enable,"
            " finger: {}".format(finger)
        )
        hand.enable(finger)
    elif command == "enabled":
        finger = req.var1
        enabled = hand.enabled(finger)
        rospy.loginfo(
            "command: enabled,"
            " finger: {},"
            " enabled: {}"
            .format(finger,enabled)
        )
        hand_serviceResponse(str(enabled))
    elif command == "enableall":
        hand.enable_all()
        hand_serviceResponse("done")
    elif command == "disable":
        finger = req.var1
        rospy.loginfo(
            "command: disable,"
            " finger: {}"
            .format(finger)
        )
        hand.disable(finger)
    elif command == "updinp":
        hand.hand_in=hand.update_input()
    elif command == "sendcmd":
        hand.send_cmd()
    elif command == "update":
        time = req.var1
        rospy.loginfo(
            "command: update,"
            " time: {}"
            .format(time)
        )
        hand.update(time)
    hand.send_cmd() 
    return hand_serviceResponse("done")

def handle_server_get(req):
    """This function runs when the client asks for getting hand data: torque, position, velocity and all data"""
    command =req.command
    print "-------------------------"
    if command == "gettorque":
        hand.hand_in = hand.update_input()
        finger = req.finger
        joint = req.joint
        torque = hand.hand_in["Torque"][finger*3 + joint]
        rospy.loginfo(
            "command: gettorque,"
            " finger: {},"
            " joint: {},"
            " torque: {}".format(finger,joint,torque)
        )
        return hand_get_serviceResponse(str(torque))
    elif command == "getvel":
        hand.hand_in = hand.update_input()
        finger = req.finger
        joint = req.joint
        vel= hand.hand_in["Velocity"][finger*3 + joint]
        rospy.loginfo(
            "command: getvel,"
            " finger: {},"
            " joint: {},"
            " velocity: {}".format(finger,joint,vel)
        )
        return hand_get_serviceResponse(str(vel))
    elif command == "getpos":
        hand.hand_in = hand.update_input()
        finger = req.finger
        joint = req.joint
        pos = hand.hand_in["Pos"][finger*3 + joint]
        rospy.loginfo(
            "command: getpos,"
            " finger: {},"
            " joint: {},"
            " position: {}".format(finger,joint,pos)
        )
        return hand_get_serviceResponse(str(pos))
    elif command == "getdata":
        hand.hand_in = hand.update_input()
        return hand_get_serviceResponse(str(hand.hand_in))
    
def handle_server_set(req):
    """This function runs when the client sends data to the hand: position, controller, damping, velocity, stiffness"""
    command = req.command
    print "-------------------------"
    if command == "setpos":
        finger = req.finger
        joint = req.joint
        pos = req.value
        rospy.loginfo(
            "command: setpos,"
            " finger: {},"
            " joint: {},"
            " position: {}".format(finger,joint,pos)
        )
        hand.set_pos(finger, joint, pos)
    elif command == "setcontroller":
        mode = req.finger
        rospy.loginfo(
            "command: setcontroller,"
            " mode: {}"
            .format(mode)
        )
        hand.set_controller_mode(mode)
    elif command == "setdamp":
        finger = req.finger
        joint = req.joint
        damp = req.value
        rospy.loginfo(
            "command: setdamp,"
            " finger: {},"
            " joint: {},"
            " damping: {}".format(finger,joint,damp)
        )
        hand.set_damping(finger, joint, damp)
    elif command == "setstiff":                
        finger = req.finger
        joint = req.joint
        stiff = req.value
        rospy.loginfo(
            "command: setstiff,"
            " finger: {},"
            " joint: {},"
            " stiffness: {}".format(finger,joint,torque)
        )
        hand.set_stiffness(finger, joint, stiff)
    elif command == "setvel":
        finger = req.finger
        joint = req.joint
        vel = req.value
        rospy.loginfo(
            "command: setvel,"
            " finger: {},"
            " joint: {},"
            " velocity: {}".format(finger,joint,vel)
        )
        hand.set_velocity(finger, joint, vel)
    hand.send_cmd()
    return hand_set_serviceResponse("done")
    
def server_ros():
    """Create server node called hand_server
    Init ros service called server. This server is for the hand control
    This server keeps running in a loop"""
    rospy.init_node('hand_server', anonymous=True)
    rospy.Service('get_server',hand_get_service, handle_server_get)
    rospy.Service('set_server',hand_set_service, handle_server_set)
    rospy.Service('server',hand_service, handle_server) ##Init ros service calling handle_server with hand_service object
    print "server initialized"
    rospy.spin() ##cycling the listen client request



def main():
    """Main function caller of the function server_ros"""

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
