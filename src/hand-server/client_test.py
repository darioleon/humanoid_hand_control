#!/usr/bin/env python

from hand_client import HandClient
from time import sleep 

hand = HandClient()
hand.enable(1)
sleep(2)
hand.enable(3)
sleep(2)
#print hand.enabled(hand.fingers["Thumb"])
#sleep(2)
#print hand.enabled(hand.fingers["Index"])
#sleep(2)
#hand.set_pos(hand.fingers["Thumb"], hand.arts["Outer"],60)
#sleep(2)
hand.set_pos(hand.fingers["Index"], hand.arts["Outer"],0)
sleep(2)
hand.set_pos(hand.fingers["Ring"], hand.arts["Inner"],0)
sleep(2)
#hand.set_pos(hand.fingers["Index"], hand.arts["Outer"],0)
#sleep(2)
hand.disable(hand.fingers["Index"])
sleep(2)
hand.disable(hand.fingers["Ring"])
sleep(2)

