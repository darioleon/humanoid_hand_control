#!/usr/bin/env python
import rospy
from hand_code.msg import Hand_info

def callback(data):
    """This function Gets and prints the hand data coming from the publisher
       that contains Hand sensors outputs"""
    val=Hand_info()
    val=data
    print "-----------------------------------"
    rospy.loginfo(val)

    
def listener():    
    """create node called listener and subscribe to the topic handData_pub and its publisher comes from the script server_handData"""
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("handData_pub", Hand_info, callback) ##Subscribing to handData_pub topic calling callback with the message type Hand_info 
    rospy.spin() 

if __name__ == '__main__':
    listener()
