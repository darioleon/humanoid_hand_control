#!/usr/bin/env python

from hand_client import HandClient as Hand
from time import sleep

# init Hand and enable fingers
print "init hand"
hand = Hand()

hand.enable(hand.fingers["Thumb"])
hand.send_cmd()
sleep(2)
hand.enable(hand.fingers["Index"])
hand.send_cmd()
sleep(2)

# move fingers to zero position
print "zero pos"
hand.set_pos(hand.fingers["Thumb"],hand.arts["Outer"],0)
hand.send_cmd()
sleep(1)
hand.set_pos(hand.fingers["Index"],hand.arts["Outer"],0)
hand.send_cmd()
sleep(1)
hand.set_pos(hand.fingers["Thumb"],hand.arts["Inner"],0)
sleep(1)
hand.set_pos(hand.fingers["Thumb"],hand.arts["Abductor"],0)
sleep(1)
hand.send_cmd()
#hand.set_velocity(hand.fingers["Thumb"],hand.arts["Outer"],60)
sleep(0.1)
hand.set_pos(hand.fingers["Thumb"],hand.arts["Outer"],50)
sleep(0.1)
hand.set_velocity(hand.fingers["Thumb"],hand.arts["Outer"],20)
sleep(0.1)
#hand.send_cmd()
sleep(0.1)
hand.set_pos(hand.fingers["Index"],hand.arts["Outer"],40)
hand.send_cmd()
sleep(0.1)
sleep(2)
hand.set_pos(hand.fingers["Thumb"],hand.arts["Outer"],0)
hand.send_cmd()
sleep(0.1)
hand.set_pos(hand.fingers["Index"],hand.arts["Outer"],0)
hand.send_cmd()
sleep(0.1)

print "disable"
hand.disable(hand.fingers["Thumb"])
hand.send_cmd()
sleep(0.1)
hand.disable(hand.fingers["Index"])
hand.send_cmd()

