#!/usr/bin/env python

from hand_yarp_client import Hand
from time import sleep
import yarp as y
import rospy #puede que la persona no tenga rospy, entonces es error
from hand_code.msg import Handmsg #lo mismo de arriba
from hand_code.msg import Hand_info

def server_yarp():
    
    #init yarp ports for comm
    y.Network.init()
    portsrv_in = y.BufferedPortBottle()
    portsrv_in.open("/server/in")
    portsrv_out = y.BufferedPortBottle()
    portsrv_out.open("/server/out")
    
    #util vars
    time = 2
    
    #daemon code
    while(True):            
        bottle_in = portsrv_in.read()
        bottle_out = portsrv_out.prepare()
        command = bottle_in.get(0).asString()
        print command
        if command == "enable":
            finger = bottle_in.get(1).asInt()
            print finger
            hand.enable(finger)
        elif command == "enabled":
            finger = bottle_in.get(1).asInt()
            val = hand.enabled(finger)
            bottle_out.clear()
            bottle_out.addDouble(val)
            portsrv_out.write()
        elif command == "enableall":
            hand.enable_all()
        elif command == "disable":
            finger = bottle_in.get(1).asInt()
            print finger
            hand.disable(finger)
        elif command == "setcontroller":
            mode = botlle_in.get().asInt()
            print mode
            hand.set_controller_mode(mode)
        elif command == "setpos":
            finger = bottle_in.get(1).asInt()
            joint = bottle_in.get(2).asInt()
            pos = bottle_in.get(3).asDouble()
            print finger 
            print joint 
            print pos
            hand.set_pos(finger, joint, pos)
        elif command == "setdamp":
            finger = bottle_in.get(1).asInt()
            joint = bottle_in.get(2).asInt()
            damp = bottle_in.get(3).asDouble()
            print finger 
            print joint 
            print damp
            hand.set_damping(finger, joint, damp)
        elif command == "setstiff":                
            finger = bottle_in.get(1).asInt()
            joint = bottle_in.get(2).asInt()
            stiff = bottle_in.get(3).asDouble()
            print finger 
            print joint 
            print stiff
            hand.set_stiffness(finger, joint, stiff)
        elif command == "setvel":
            finger = bottle_in.get(1).asInt()
            joint = bottle_in.get(2).asInt()
            vel = bottle_in.get(3).asDouble()
            print finger 
            print joint 
            print vel
            hand.set_velocity(finger, joint, vel)
        elif command == "updinp":
            hand.update_input()
        elif command == "sendcmd":
            hand.send_cmd()
        elif command == "update":
            time = bottle_in.get(1).asInt()
            hand.update(time)
        hand.update(time)
        
#
#
#
#
def callback(data):    
    pub = rospy.Publisher('serverclient', Hand_info)
    rate = rospy.Rate(10)
    #hand = Hand()
    #hand.set_controller_mode(1)
    
    #util vars
    time = 2
    
    command = data.var0
    print command
    if command == "enable":
        finger = data.var1
        print finger
        hand.enable(finger)
    elif command == "enabled":
        finger = data.var1
        hand_resp=Hand_info()
        hand_resp.finger =finger
        hand_resp.Enabled = hand.enabled(finger)
        pub.publish(hand_resp)
    elif command == "enableall":
        hand.enable_all()
    elif command == "disable":
        finger = data.var1
        print finger
        hand.disable(finger)
    elif command == "setcontroller":
        mode = data.var1
        print mode
        hand.set_controller_mode(mode)
    elif command == "setpos":
        finger = data.var1
        joint = data.var2
        pos = data.var3
        print "finger:", finger 
        print joint 
        print pos
        hand.set_pos(finger, joint, pos)
    elif command == "setdamp":
        finger = data.var1
        joint = data.var2
        damp = data.var3
        print finger 
        print joint 
        print damp
        hand.set_damping(finger, joint, damp)
    elif command == "setstiff":                
        finger = data.var1
        joint = data.var2
        stiff = data.var3
        print finger 
        print joint 
        print stiff
        hand.set_stiffness(finger, joint, stiff)
    elif command == "setvel":
        finger = data.var1
        joint = data.var2
        vel = data.var3
        print finger 
        print joint 
        print vel
        hand.set_velocity(finger, joint, vel)
    elif command == "updinp":
        hand.hand_in=hand.update_input()
    elif command == "sendcmd":
        hand.send_cmd()
    elif command == "update":
        time = data.var1
        hand.update(time)
    elif command == "gettorque":
        hand.hand_in=hand.update_input()
        hand_resp=Hand_info()
        finger=data.var1
        hand_resp.finger=finger
        hand_resp.Enabled=hand.hand_in["Enabled"][finger]
        hand_resp.Torque[0]=hand.hand_in["Torque"][finger*3 + 0]
        hand_resp.Torque[1]=hand.hand_in["Torque"][finger*3 + 1]
        hand_resp.Torque[2]=hand.hand_in["Torque"][finger*3 + 2]
        pub.publish(hand_resp)
    elif command == "getpos":
        hand.hand_in=hand.update_input()
        hand_resp=Hand_info()
        finger=data.var1
        hand_resp.finger=finger
        hand_resp.Enabled=hand.hand_in["Enabled"][finger]
        hand_resp.Pos[0]=hand.hand_in["Pos"][finger*3 + 0]
        hand_resp.Pos[1]=hand.hand_in["Pos"][finger*3 + 1]
        hand_resp.Pos[2]=hand.hand_in["Pos"][finger*3 + 2]
        pub.publish(hand_resp)
    elif command == "getvel":
        hand.hand_in=hand.update_input()
        hand_resp=Hand_info()
        finger=data.var1
        hand_resp.finger=finger
        hand_resp.Enabled=hand.hand_in["Enabled"][finger]
        hand_resp.Velocity[0]=hand.hand_in["Velocity"][finger*3 + 0]
        hand_resp.Velocity[1]=hand.hand_in["Velocity"][finger*3 + 1]
        hand_resp.Velocity[2]=hand.hand_in["Velocity"][finger*3 + 2]
        pub.publish(hand_resp)
    hand.update(time) 

def server_ros():
    rospy.init_node('server', anonymous=True)
    rospy.Subscriber('clientserver',Handmsg,callback)
    #hand.hand_in=hand.update_input()
    print hand.hand_in
    print "------------------"
    rospy.spin()


if __name__ == "__main__":

    #init hand.
    hand = Hand()
    hand.set_controller_mode(1)
    
    #server_yarp()
    try:
        server_ros()
    except rospy.ROSInterruptException:
        pass


