#!/usr/bin/env python
import random
import rospy
from hand_code.srv import hand_service 

## Client class for hand data reciving
class HandClient:
    ##Define the fingers and articulations id, then wait for the service called handData_service to be initialized
    def __init__(self):
        ##Default definition fingers id
        self.fingers={
            "Thumb": 0,
            "Index": 1,
            "Middle": 2,
            "Ring": 3,
            "Pinky": 4
        }
        ##Default definition articulation id
        self.arts={
            "Outer": 0,
            "Inner": 1,
            "Abductor": 2
        }
        
        rospy.wait_for_service('handData_service')

    ## Gets a finger data
    #  @param finger int finger id.
    def get_data(self,finger):
        server = rospy.ServiceProxy('handData_service',hand_service)
        resp=server("getdata", finger, 0, 0)
        pass
    ##Gets all fingers data
    def get_all(self):
        server = rospy.ServiceProxy('handData_service',hand_service)
        resp=server("getall",0, 0, 0)
        pass


        
   
