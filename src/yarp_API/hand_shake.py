#!/usr/bin/env python

from hand_client import HandClient
from time import sleep 

hand = HandClient()

#enable
print "enable hand"
sleep(1)
hand.enable(0)
sleep(2)
hand.enable(1)
sleep(2)
hand.enable(2)
sleep(2)
hand.enable(3)
sleep(2)
print hand.enabled(hand.fingers["Thumb"])
sleep(2)
print hand.enabled(hand.fingers["Index"])
sleep(2)

#set position
print "set pos zero"
hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"],24)
sleep(2)
hand.set_pos(hand.fingers["Index"], hand.arts["Outer"],0)
sleep(2)
hand.set_pos(hand.fingers["Middle"], hand.arts["Outer"],0)
sleep(2)
hand.set_pos(hand.fingers["Ring"], hand.arts["Outer"],0)
sleep(2)
hand.set_pos(hand.fingers["Thumb"], hand.arts["Inner"],20)
sleep(2)
hand.set_pos(hand.fingers["Index"], hand.arts["Inner"],0)
sleep(2)
hand.set_pos(hand.fingers["Middle"], hand.arts["Inner"],0)
sleep(2)
hand.set_pos(hand.fingers["Ring"], hand.arts["Inner"],0)
sleep(2)

while(True):
    print "read torque"
    trq_idx_1 =hand.get_torque(hand.fingers["Index"], hand.arts["Outer"])
    sleep(0.01)
    trq_idx_2 =hand.get_torque(hand.fingers["Index"], hand.arts["Inner"])
    sleep(0.01)
    trq_idx_3 =hand.get_torque(hand.fingers["Index"], hand.arts["Abductor"])
    sleep(0.01)

    trq_tmb_1 =hand.get_torque(hand.fingers["Thumb"], hand.arts["Outer"])
    sleep(0.01)
    trq_tmb_2 =hand.get_torque(hand.fingers["Thumb"], hand.arts["Inner"])
    sleep(0.01)
    trq_tmb_3 =hand.get_torque(hand.fingers["Thumb"], hand.arts["Abductor"])
    sleep(0.01)

    if trq_idx_1>=0.1 or trq_idx_2>=0.1 or trq_idx_3>=0.1 or trq_tmb_1>=0.1 or trq_tmb_2>=0.1 or trq_tmb_3>=0.1:
        print "move hand"
        #hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"],24)
        #sleep(0.01)
        #hand.set_pos(hand.fingers["Thumb"], hand.arts["Inner"],20)
        #sleep(0.01)
        hand.set_pos(hand.fingers["Index"], hand.arts["Outer"],20)
        sleep(0.01)
        hand.set_pos(hand.fingers["Index"], hand.arts["Inner"],19)
        sleep(0.01)
        hand.set_pos(hand.fingers["Middle"], hand.arts["Inner"],24)
        sleep(0.01)
        hand.set_pos(hand.fingers["Middle"], hand.arts["Outer"],30)
        sleep(0.01)
        hand.set_pos(hand.fingers["Ring"], hand.arts["Inner"],22)
        sleep(0.01)
        hand.set_pos(hand.fingers["Ring"], hand.arts["Outer"],18)
        sleep(5)
        print "move pos zero"
        hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"],0)
        sleep(0.01)
        hand.set_pos(hand.fingers["Index"], hand.arts["Outer"],0)
        sleep(0.01)
        hand.set_pos(hand.fingers["Middle"], hand.arts["Outer"],0)
        sleep(0.01)
        hand.set_pos(hand.fingers["Ring"], hand.arts["Outer"],0)
        sleep(0.01)
        hand.set_pos(hand.fingers["Thumb"], hand.arts["Inner"],0)
        sleep(0.01)
        hand.set_pos(hand.fingers["Index"], hand.arts["Inner"],0)
        sleep(0.01)
        hand.set_pos(hand.fingers["Middle"], hand.arts["Inner"],0)
        sleep(0.01)
        hand.set_pos(hand.fingers["Ring"], hand.arts["Inner"],0)
        sleep(0.01)

print "disable"
hand.disable(hand.fingers["Thumb"])
sleep(2)
hand.disable(hand.fingers["Index"])
sleep(2)
hand.disable(hand.fingers["Middle"])
sleep(2)
hand.disable(hand.fingers["Ring"])
sleep(2)
