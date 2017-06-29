#!/usr/bin/env python
import rospy
from hand_code.msg import Hand_info

def callback(data):
    val=Hand_info()
    val=data
    print "-----------------------------------"
    print val
    
def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("handData_pub", Hand_info, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
