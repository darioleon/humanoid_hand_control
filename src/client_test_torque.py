#!/usr/bin/env python

from ros_client_sm import HandClient
from time import sleep 

hand = HandClient()

tor=hand.get_torque(hand.fingers["Thumb"],hand.arts["Outer"])
print tor
