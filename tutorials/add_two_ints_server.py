#!/usr/bin/env python

from hand_code.srv import *
import rospy

def handle_add_two_ints(req):
    num=req.var1
    print req
    print "--------"
    return hand_serviceResponse(" numw ")

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('server', hand_service, handle_add_two_ints)
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
