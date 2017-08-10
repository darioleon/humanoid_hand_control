#!/usr/bin/env python

from ros_client_sm import HandClient
from time import sleep 

hand = HandClient()
#hand.enable(0)
#sleep(2)
hand.enable(0)
sleep(2)
hand.enable(1)
sleep(2)
#hand.enabled(hand.fingers["Thumb"])
#sleep(2)
#hand.enabled(hand.fingers["Index"])
#sleep(2)
hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"],0)
sleep(2)
hand.set_pos(hand.fingers["Index"], hand.arts["Outer"],0)
sleep(2)
hand.set_pos(hand.fingers["Index"], hand.arts["Outer"],30)
hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"],30)
sleep(0.5)
hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"],60)
sleep(2)
hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"],20)
sleep(0.5)
hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"],0)
sleep(2)
hand.set_pos(hand.fingers["Index"], hand.arts["Outer"],60)
sleep(2)
hand.set_pos(hand.fingers["Index"], hand.arts["Outer"],45)
sleep(0.5)
hand.set_pos(hand.fingers["Index"], hand.arts["Outer"],0)
sleep(2)
print "disabling fingers"
hand.disable(hand.fingers["Thumb"])
sleep(2)
hand.disable(hand.fingers["Index"])
sleep(2)


