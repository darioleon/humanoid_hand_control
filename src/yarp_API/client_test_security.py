#!/usr/bin/env python

from hand_client import HandClient
from time import sleep

#enable fingers
hand = HandClient()

while(True):
    hand_data = hand.get_data()
    print "working"
    for i in range(0, 14):
        if (abs(hand_data["Torque"][i]) >= 0.2 or
        abs(hand_data["Pos"][i]) >= 60 or
            abs(hand_data["Velocity"][i]) > 1200): #por ahora la velocidad no tiene un valor maximo
            for finger in hand.fingers:
                for art in hand.arts:
                    hand.set_pos(hand.fingers[finger], hand.arts[art],0)
                    #sleep(1)
          
