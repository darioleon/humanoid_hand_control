#!/usr/bin/env python
import re
import random
import rospy
from hand_code.srv import *
from hand_code.msg import Hand_info


## Client class for hand data sending
class HandClient:
    ##Define the fingers and articulations id, then wait for the service called server to be initialized
    def __init__(self):
        ##Default definition fingers id
        self.fingers={
            "Thumb": 0,
            "Index": 1,
            "Middle": 2,
            "Ring": 3,
            "Pinky": 4
        }
        ##Default definition articulations id  
        self.arts={
            "Outer": 0,
            "Inner": 1,
            "Abductor": 2
        }
        rospy.init_node('ros_client', anonymous=True)
        rospy.wait_for_service('server')
        rospy.wait_for_service('get_server')
        rospy.wait_for_service('set_server')
        
    ##Enable finger
    # @param finger int finger id
    def enable(self, finger):
        server = rospy.ServiceProxy('server',hand_service) ##Client object for server 
        resp=server("enable", finger, 0, 0) 
    
    ##Get finger enable state
    # @param finger int finger id
    def enabled(self, finger):
        ##return boolean var: enabled=1, disabled=0
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("enabled", finger, 0, 0)
        resp = str(resp).split(" " )[1]
        return(float(resp))

    ##Enable all fingers
    def enable_all(self):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("enableall", finger, 0, 0)

    ##Disable finger
    # @param finger int finger id
    def disable(self, finger):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("disable", finger, 0, 0)

    ##Set finger position
    # @param finger int finger id
    # @param joint int articulation id
    # @param pos float position value
    def set_pos(self, finger, joint, pos):
        server = rospy.ServiceProxy('set_server',hand_set_service)
        resp=server("setpos", finger,joint,pos)

    ##Set controller mode
    # @param mode int controller mode
    def set_controller_mode(self, mode):
        server = rospy.ServiceProxy('set_server',hand_set_service)
        resp=server("setcontroller", mode, 0, 0)
    
    ##Set finger damping
    # @param finger int finger id
    # @param joint int articulation id
    # @param damping float damping value
    def set_damping(self, finger, joint, damping):
        server = rospy.ServiceProxy('set_server',hand_set_service)
        resp=server("setdamp", finger,joint,damping)

    ##Set finger stiffness
    # @param finger int finger id
    # @param joint int articulation id
    # @param stiffness float stiffness value
    def set_stiffness(self, finger, joint, stiffness):
        server = rospy.ServiceProxy('set_server',hand_set_service)
        resp=server("setstiff", finger,joint,stiffness)

    ##Set finger velocity
    # @param finger int finger id
    # @param joint int articulation id
    # @param velocity float velocity value
    def set_velocity(self, finger, joint, velocity):
        server = rospy.ServiceProxy('set_server',hand_set_service)
        resp=server("setvel", finger,joint,velocity)
    
    def get_torque(self, finger, joint):
        server = rospy.ServiceProxy('get_server',hand_get_service)
        resp = server("gettorque", finger,joint) #resp = resp: 'torque'
        resp = str(resp).split(" " )[1] #resp = 'torque'
        return(float(resp))
    
    def get_velocity(self, finger, joint):
        server = rospy.ServiceProxy('get_server',hand_get_service)
        resp = server("getvel", finger,joint) 
        resp = str(resp).split(" " )[1]
        return(float(resp))

    def get_pos(self, finger, joint):
        server = rospy.ServiceProxy('get_server',hand_get_service)
        resp = server("getpos", finger,joint) 
        resp = str(resp).split(" " )[1]
        return(float(resp))

    ##update fingers inputs. This is for getting the fingers data 
    def update_input(self):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("updinp", 0, 0, 0)

    ##Send queue commands
    def send_cmd(self):
        server = rospy.ServiceProxy('server',hand_service)
        resp = server("sendcmd", 0, 0, 0)

    ##Send queue commands, wait time, update finger inputs
    # @param time sleep time for the update
    def update(self, time=0):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("update", time, 0, 0)
    

        
        
    
