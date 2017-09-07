#!/usr/bin/env python

from hand_yarp_client import Hand
from time import sleep
import yarp as y

def listener():
    
    #init yarp ports for comm
    y.Network.init()
    portlistener_in = y.BufferedPortBottle()
    portlistener_in.open("/listener/in")

    while(True):
        bottle_in = portlistener_in.read()
        command = bottle_in.get(0).asString()
        if command == "getdata":
            finger = bottle_in.get(1).asInt()
            enabled = bottle_in.get(2).asDouble()
            pos = []
            pos.append(bottle_in.get(3).asDouble())
            pos.append(bottle_in.get(4).asDouble())
            pos.append(bottle_in.get(5).asDouble())
            vel = []
            vel.append(bottle_in.get(6).asDouble())
            vel.append(bottle_in.get(7).asDouble())
            vel.append(bottle_in.get(8).asDouble())
            tor = []
            tor.append(bottle_in.get(9).asDouble())
            tor.append(bottle_in.get(10).asDouble())
            tor.append(bottle_in.get(11).asDouble())
            print "Finger:", finger
            print "Enabled:", enabled
            print "Position:", pos
            print "Velocity:", vel
            print "Torque:", tor
        if command == "getall":
            allData = bottle_in.get(1).asString()
            print allData
            print ""
            
        
            
if __name__ == "__main__":
    
    listener()
