#!/usr/bin/env python
import random
import rospy
from hand_code.msg import Handmsg


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
        self.server=rospy.ServiceProxy('server',Handmsg)
        
    def enable(self, finger):
        hand = Handmsg()
        hand.var0 = "enable"
        hand.var1 = finger
        rospy.loginfo(hand)
        self.server(hand)
        pass
    def enabled(self, finger):
        hand = Handmsg()
        hand.var0 = "enabled"
        hand.var1 = finger
        self.pub.publish(hand)
        #sleep(5)
        #bottle_in = self.port_in.read()
        #val = bottle_in.get(0).asDouble()
        #return(val)

    def enable_all(self):
        hand = Handmsg()
        hand.var0 = "enableall"
        self.pub.publish(hand)
        pass

    def disable(self, finger):
        hand = Handmsg()
        hand.var0 = "disable"
        hand.var1 = finger
        self.pub.publish(hand)
        pass

    def set_pos(self, finger, joint, pos): 
        hand=Handmsg()
        hand.var0="setpos"
        hand.var1=finger
        hand.var2=joint
        hand.var3=pos
        print hand
        self.pub.publish(hand)
        pass

    def set_controller_mode(self, mode):
        hand=Handmsg()
        hand.var0="setcontroller"
        hand.var1=mode
        self.pub.publish(hand)
        pass

    def set_damping(self, finger, joint, damping):
        hand=Handmsg()
        hand.var0="setdamp"
        hand.var1=finger
        hand.var2=joint
        hand.var3=damping
        self.pub.publish(hand)
        pass

    def set_stiffness(self, finger, joint, stiffness):
        hand=Handmsg()
        hand.var0="setstiff"
        hand.var1=finger
        hand.var2=joint
        hand.var3=stiffness
        self.pub.publish(hand)
        pass

    def set_velocity(self, finger, joint, velocity):
        hand=Handmsg()
        hand.var0="setvel"
        hand.var1=finger
        hand.var2=joint
        hand.var3=velocity
        self.pub.publish(hand)
        pass

    def update_input(self):
        hand=Handmsg()
        hand.var0="updinp"       
        self.pub.publish(hand)
        pass

    def send_cmd(self, finger, joint, velocity):
        hand=Handmsg()
        hand.var0="sendcmd"
        self.pub.publish(hand)
        pass

    def update(self, time=0):
        hand=Handmsg()
        hand.var0="update"
        hand.var1=time
        self.pub.publish(hand)
        pass

    def get_torque(self,finger):
        hand=Handmsg()
        hand.var0="gettorque"
        hand.var1=finger
        self.pub.publish(hand)
        pass

    def get_pos(self,finger):
        hand=Handmsg()
        hand.var0="getpos"
        hand.var1=finger
        self.pub.publish(hand)
        pass

    def get_velocity(self,finger):
        hand=Hnadmsg()
        hand.var0="getvelocity"
        hand.var1=finger
        self.pub.publish(hand)
        pass
    
    def routine(self, routine=[["enable",[1,1,0,0,0]],  
		       ["sleep", 3],
		       ["move",["Thumb","Outer",40],["Index","Outer",60]], 
		       ["sleep", 3], 
		       ["move",["Thumb","Outer",0],["Index","Outer",0]], 
		       ["sleep", 3]]):
        pass
