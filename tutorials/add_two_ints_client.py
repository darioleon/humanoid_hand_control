#!/usr/bin/env python

import sys
import rospy
from hand_code.srv import *
from ros_client import HandClient
from time import sleep

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints1 = rospy.ServiceProxy('add_two_ints', hand_service)
        resp1 = add_two_ints1("A",x, y,x)
        #return resp1.resp
        return "nada"
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    hand=HandClient()
    hand.enable(2)

