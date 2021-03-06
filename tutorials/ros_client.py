#!/usr/bin/env python
import random
import rospy
from hand_code.srv import hand_service 


class HandClient:
    
    def __init__(self):

        self.fingers={
            "Thumb": 0,
            "Index": 1,
            "Middle": 2,
            "Ring": 3,
            "Pinky": 4
        }

        self.arts={
            "Outer": 0,
            "Inner": 1,
            "Abductor": 2
        }
        rospy.wait_for_service('server')
        
    def enable(self, finger):
        server = rospy.ServiceProxy('server',hand_service)
        print "---------------------"
        server("enable", finger, 0, 0)
        pass
    def enabled(self, finger):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("enabled", finger, 0, 0)
        #sleep(5)
        #bottle_in = self.port_in.read()
        #val = bottle_in.get(0).asDouble()
        #return(val)

    def enable_all(self):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("enableall", finger, 0, 0)
        pass

    def disable(self, finger):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("disable", finger, 0, 0)
        pass

    def set_pos(self, finger, joint, pos):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("setpos", finger,joint,pos)
        pass

    def set_controller_mode(self, mode):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("setcontroller", mode, 0, 0)
        pass

    def set_damping(self, finger, joint, damping):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("setdamp", finger,joint,damping)
        pass

    def set_stiffness(self, finger, joint, stiffness):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("setstiff", finger,joint,stiffness)
        pass

    def set_velocity(self, finger, joint, velocity):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("setvel", finger,joint,velocity)
        pass

    def update_input(self):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("updinp", 0, 0, 0)
        pass

    def send_cmd(self, finger, joint, velocity):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("sendcmd", finger,joint,velocity)
        pass

    def update(self, time=0):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("setpos", time, 0, 0)
        pass

    def get_torque(self,finger):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("gettorque", finger, 0, 0)
        pass

    def get_pos(self,finger):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("gettorque", finger, 0, 0)
        pass
    
    def get_velocity(self,finger):
        server = rospy.ServiceProxy('server',hand_service)
        resp=server("getvel", finger, 0, 0)
        pass
    
    def routine(self, routine=[["enable",[1,1,0,0,0]],  
		       ["sleep", 3],
		       ["move",["Thumb","Outer",40],["Index","Outer",60]], 
		       ["sleep", 3], 
		       ["move",["Thumb","Outer",0],["Index","Outer",0]], 
		       ["sleep", 3]]):
        pass

        
        
    
