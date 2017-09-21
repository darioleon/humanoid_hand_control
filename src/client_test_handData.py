#!/usr/bin/env python

from ros_handData_client import HandClient
from time import sleep 

hand = HandClient()

while True:
    print "getting all Data"
    #hand.get_data(hand.fingers["Thumb"])
    hand.get_all()
    sleep(0.5)

