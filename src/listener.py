#!/usr/bin/env python
import rospy
from hand_code.msg import Hand_info

def callback(data):
    """Gets and print the hand data coming from the publisher
       data Hand sensors output"""
    val=Hand_info()
    val=data
    print "-----------------------------------"
    print val

    
def listener():    
    """creates nodes and subscribe to the server_handData publisher"""
    rospy.init_node('listener', anonymous=True)
    """Creation of listener node called listener """
    rospy.Subscriber("handData_pub", Hand_info, callback) ##Subscribing to handData_pub topic calling callback with the message type Hand_info 
    rospy.spin() ##cycling the listener

if __name__ == '__main__':
    listener()
