#!/usr/bin/env python

from hand_client import HandClient as Hand
from time import sleep

# init Hand and enable fingers
print "init hand"
hand = Hand()

hand.enable(hand.fingers["Thumb"])
hand.enable(hand.fingers["Index"])
hand.enable(hand.fingers["Middle"])
hand.enable(hand.fingers["Ring"])
#hand.send_cmd()
sleep(10)

# move fingers to zero position
print "zero pos"
hand.set_pos(hand.fingers["Thumb"],hand.arts["Outer"],0)
hand.set_pos(hand.fingers["Thumb"],hand.arts["Inner"],0)
hand.set_pos(hand.fingers["Thumb"],hand.arts["Abductor"],0)
hand.set_pos(hand.fingers["Index"],hand.arts["Outer"],0)
hand.set_pos(hand.fingers["Index"],hand.arts["Inner"],0)
hand.set_pos(hand.fingers["Index"],hand.arts["Abductor"],0)
hand.set_pos(hand.fingers["Middle"],hand.arts["Outer"],0)
hand.set_pos(hand.fingers["Middle"],hand.arts["Inner"],0)
hand.set_pos(hand.fingers["Middle"],hand.arts["Abductor"],0)
hand.set_pos(hand.fingers["Ring"],hand.arts["Outer"],0)
hand.set_pos(hand.fingers["Ring"],hand.arts["Inner"],0)
hand.set_pos(hand.fingers["Ring"],hand.arts["Abductor"],0)
#hand.send_cmd()
sleep(10)

# get torque vals for threshold
torque1 = hand.get_torque(hand.fingers["Index"],hand.arts["Outer"])
torque2 = hand.get_torque(hand.fingers["Index"],hand.arts["Inner"])
torque3 = hand.get_torque(hand.fingers["Index"],hand.arts["Abductor"])

print torque1
print torque2
print torque3

#sleep(3)

print "move index"
hand.set_pos(hand.fingers["Index"],hand.arts["Outer"],20)
#hand.update(3)
hand.set_pos(hand.fingers["Index"],hand.arts["Inner"],19)
#hand.update(3)
#hand.send_cmd()
sleep(10)

print "index to zero pos"
hand.set_pos(hand.fingers["Index"],hand.arts["Outer"],0)
hand.set_pos(hand.fingers["Index"],hand.arts["Inner"],0)
#hand.send_cmd()
sleep(10)

