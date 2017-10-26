#!/usr/bin/env python

from ros_client_sm import HandClient
from time import sleep 

hand = HandClient()

#enable fingers
hand.enable(0)
sleep(2)
hand.enable(1)
sleep(2)
hand.enable(2)
sleep(2)
hand.enable(3)
sleep(2)
tor=hand.get_torque(hand.fingers["Thumb"],hand.arts["Outer"])
print tor
#set zero position
hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"],0)
sleep(0.1)
hand.set_pos(hand.fingers["Index"], hand.arts["Outer"],0)
sleep(0.1)
hand.set_pos(hand.fingers["Middle"], hand.arts["Outer"],0)
sleep(0.1)
hand.set_pos(hand.fingers["Ring"], hand.arts["Outer"],0)
sleep(0.1)
hand.set_pos(hand.fingers["Thumb"], hand.arts["Inner"],0)
sleep(0.1)
hand.set_pos(hand.fingers["Index"], hand.arts["Inner"],0)
sleep(0.1)
hand.set_pos(hand.fingers["Middle"], hand.arts["Inner"],0)
sleep(0.1)
hand.set_pos(hand.fingers["Ring"], hand.arts["Inner"],0)
sleep(0.1)


hand.set_pos(hand.fingers["Index"], hand.arts["Outer"],30)
hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"],30)
sleep(0.5)
hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"],70)
sleep(2)
hand.set_velocity(hand.fingers["Thumb"], hand.arts["Outer"],10)
sleep(0.5)
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
hand.send_cmd()


