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
        rospy.wait_for_service('handData_service')

    def get_data(self,finger):
        server = rospy.ServiceProxy('handData_service',hand_service)
        resp=server("getdata", finger, 0, 0)
        pass
    def get_all(self):
        server = rospy.ServiceProxy('handData_service',hand_service)
        resp=server("getall",0, 0, 0)
        pass


        
   
