#!/usr/bin/env python

from handData_client import HandClient
from time import sleep 

hand = HandClient()
while(True):
    hand.get_data(hand.fingers["Thumb"])
    sleep(2)
