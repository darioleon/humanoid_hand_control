#!/usr/bin/env python

from time import sleep
from hand_yarp_client import Hand

print "Init test"
hand = Hand()
print "Enabling thumb & index fingers"
hand.enable(hand.fingers["Thumb"]) #enable thumb
hand.enable(hand.fingers["Index"])
hand.set_controller_mode(1)
hand.update()
sleep(1)
hand.update_input()
sleep(1)
#print "Is thumb finger enabled? %d"%hand.enabled(hand.fingers["Thumb"])
print "Moving thumb finger"
hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"], 40)
hand.update()
sleep(1)
hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"], 0)
hand.update()
sleep(1)
print "Moving index finger"
hand.set_pos(hand.fingers["Index"], hand.arts["Outer"], 40)
hand.update()
sleep(1)
hand.set_pos(hand.fingers["Index"], hand.arts["Outer"], 0)
hand.update()
sleep(1)
print "Moving both fingers"
hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"], 40)
hand.set_pos(hand.fingers["Index"], hand.arts["Outer"], 60)
hand.update()
sleep(1)
hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"], 0)
hand.set_pos(hand.fingers["Index"], hand.arts["Outer"], 0)
print "Disabling thumb & index fingers"
hand.disable(hand.fingers["Thumb"])
hand.disable(hand.fingers["Index"])
hand.update()
sleep(1)
print "Finish test"
