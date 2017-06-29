#!/usr/bin/env python

from handData_client import HandClient
from time import sleep 

hand = HandClient()

while True:
    print "getting thumb Data"
    #hand.get_data(hand.fingers["Thumb"])
    hand.get_all()
    sleep(2)

