#!/usr/bin/env python

import yarp as y
from time import sleep
import pygame as pg
from hand_client import HandClient as Hand

#----------Joystick initialization------------
pg.init()
pg.joystick.init()
js=pg.joystick.Joystick(0)
js.init()
y_out=0.
#----------End Joystick initialization------------

#----------Hand initialization------------
hand=Hand()

for i in xrange(100):
    hand.update_input()
    sleep(0.01)

#hand.enable_all()
for i in xrange(5):
    hand.enable(i)
    sleep(1.5)

range_distal=(5.,30.)
range_base_front=(5.,30.)
range_base_side=(-20.,20.)
#----------End Hand initialization------------

#----------Util functions------------
def example_values():
    hand.enable(1) #enable thumb
    hand.set_controller_mode(1)
    hand.set_pos(1, 0, 40)

def joint_pos_command(joint_range, joy):
    total_range=joint_range[1]-joint_range[0]
    a=total_range/2.
    mid_point=total_range/2.+joint_range[0]
    print a, mid_point
    return(joy*a+mid_point)

demo_types=["2pinch", "3pinch", "4pinch", "5pinch", "rutine1"]
demo=0
button_last=0.0

# Saludar, Rutinas de grasping, abrir y cerrar dedos lateralmente, live long and proster, peace and love
# Protocol: action, value
# For pos_cmd, value = [[finger_number, angle1, angle2, angle3], [finger_number, ....]]
# For sleep, value = time
# For speed, value = speed
speed=120.0
hand_sleep=1.0
rutines={
    "rutine1":[ # Grasping two fingers
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 20., 20., 0.],[1, 20., 20., 0.]]],
        ["sleep", 2.0],
        # Grasping three fingers
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 20., 20., 0.], [1, 20., 20., 0.], [2, 40., 40., 0.]]],
        ["sleep", 2.0],
        # Grasping four fingers
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 20., 20., 0.], [1, 20., 20., 0.], [2, 40., 40., 0.], [3, 30., 30., 0.]]],
        ["sleep", 2.0],
        # Grasping five fingers
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 20., 20., 0.], [1, 20., 20., 0.], [2, 40., 40., 0.], [3, 30., 30., 0.], [4, 30., 30., 0.]]],
        ["sleep", 2.0],
        # Spock!!!
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 15.], [2, 0., 0., 15.], [3, 0., 0., -15.], [4, 0., 0., -15.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., -5.], [2, 0., 0., -30.], [3, 0., 0., 30.], [4, 0., 0., 30.]]], #Normal
        ["sleep", 3.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 15.], [2, 0., 0., 15.], [3, 0., 0., -15.], [4, 0., 0., -15.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., -5.], [2, 0., 0., -30.], [3, 0., 0., 30.], [4, 0., 0., 30.]]], #Normal
        ["sleep", 3.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 15.], [2, 0., 0., 15.], [3, 0., 0., -15.], [4, 0., 0., -15.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., -5.], [2, 0., 0., -30.], [3, 0., 0., 30.], [4, 0., 0., 30.]]], #Normal
        ["sleep", 3.0],
        # Rock and Roll!
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 60., 90., 0.], [3, 60., 70., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 0.3],
        ["pos_cmd", [[0, 50., 30., 0.], [1, 0., 0., 0.], [2, 60., 90., 0.], [3, 60., 70., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 3.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 60., 90., 0.], [3, 60., 70., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 0.3],
        ["pos_cmd", [[0, 50., 30., 0.], [1, 0., 0., 0.], [2, 60., 90., 0.], [3, 60., 70., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 3.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 60., 90., 0.], [3, 60., 70., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 0.3],
        ["pos_cmd", [[0, 50., 30., 0.], [1, 0., 0., 0.], [2, 60., 90., 0.], [3, 60., 70., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 3.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 60., 90., 0.], [3, 60., 70., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 0.3],
        ["pos_cmd", [[0, 50., 30., 0.], [1, 0., 0., 0.], [2, 60., 90., 0.], [3, 60., 70., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 3.0],
        #peace and love
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 90., 30., 0.], [1, 0., 0., -30.], [2, 0., 0., 30.], [3, 60., 50., 0.], [4, 60., 50., 0.]]], #Normal
        ["sleep", 3.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 90., 30., 0.], [1, 0., 0., -30.], [2, 0., 0., 30.], [3, 60., 50., 0.], [4, 60., 50., 0.]]], #Normal
        ["sleep", 3.0],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 2.0],
        ["pos_cmd", [[0, 90., 30., 0.], [1, 0., 0., -30.], [2, 0., 0., 30.], [3, 60., 50., 0.], [4, 60., 50., 0.]]], #Normal
        ["sleep", 3.0],
        #Waving
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 0.5],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 30., 30., 0.], [2, 30., 30., 0.], [3, 30., 30., 0.], [4, 30., 30., 0.]]], #Normal
        ["sleep", 0.5],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 0.5],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 30., 30., 0.], [2, 30., 30., 0.], [3, 30., 30., 0.], [4, 30., 30., 0.]]], #Normal
        ["sleep", 0.5],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 0.5],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 30., 30., 0.], [2, 30., 30., 0.], [3, 30., 30., 0.], [4, 30., 30., 0.]]], #Normal
        ["sleep", 0.5],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 0.5],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 30., 30., 0.], [2, 30., 30., 0.], [3, 30., 30., 0.], [4, 30., 30., 0.]]], #Normal
        ["sleep", 0.5],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 0.5],
        ["pos_cmd", [[0, 0., 0., 0.], [1, 30., 30., 0.], [2, 30., 30., 0.], [3, 30., 30., 0.], [4, 30., 30., 0.]]], #Normal
        ["sleep", 0.5],
        #return to normal
        ["pos_cmd", [[0, 0., 0., 0.], [1, 0., 0., 0.], [2, 0., 0., 0.], [3, 0., 0., 0.], [4, 0., 0., 0.]]], #Normal
        ["sleep", 2.0],
        ]
               }

def rutine_executer(rutine, rutine_step):
    #this function executes all the rutine steps.
    selected_rutine=rutines[rutine]
    step=selected_rutine[rutine_step]
    cmd=step[0]
    value=step[1]
    print "Step: ", rutine_step, "Cmd: ", cmd, "Value: ", value
    if cmd=="pos_cmd":
        for finger in value:
            for i in xrange(3):
                print "command sent: finger: ", finger[0], " Joint: ", i, " Angle: ", finger[i+1]
                hand.set_pos(finger[0],i,finger[i+1])
    elif cmd=="sleep":
        sleep(value)
    else:
        print "Command unknown!"

rutine_step=0
#----------End Util functions------------

#----------Main code------------
while True:
    #----------dual shock code------------------
    #getting position from joystick
    pg.event.get()

    #getting position from left joystick
    x1=js.get_axis(0)       #Left joystick left to right values -1.0 to 0.99
    y1=js.get_axis(1)       #Left joystick up to down values -1.0 to 0.99

    y_out=-y1              #Controller gives negative values for the upbutton
    x_out=x1

    print "                                                   y_out:", y_out,"x_out:", x_out

    num_buttons = js.get_numbuttons()
    buttons = 0
    for i in xrange(num_buttons):
        buttons &= js.get_button(i)
    #getting position from right joystick
    #x2=js.get_axis(2)   #Left joystick left to right values -1.0 to 0.99
    #y2=js.get_axis(3)   #Left joystick up to down values -1.0 to 0.99
    #y2_out=-y2          #Controller gives negative values for the upbutton
    #x2_out=x2
    #-------------------------------------------
    
    if button_last==0.0 and buttons==1.0:
        demo+=1
        if demo>(len(demo_types)-1):
            demo=0
    button_last=buttons
    if demo_types[demo]=="5pinch":
        print "Commanding hand pos"
        distal_cmd=joint_pos_command(range_distal, y_out)
        base_front_cmd=joint_pos_command(range_base_front, y_out)
        base_side_cmd=joint_pos_command(range_base_side, y_out)
        print "Hand cmds: ", distal_cmd, base_front_cmd, base_side_cmd
        for i in xrange(5):
            hand.set_pos(i,0,distal_cmd)
        for i in xrange(5):
            hand.set_pos(i,1,base_front_cmd)
    elif demo_types[demo]=="4pinch":
        print "Commanding hand pos"
        distal_cmd=joint_pos_command(range_distal, y_out)
        base_front_cmd=joint_pos_command(range_base_front, y_out)
        base_side_cmd=joint_pos_command(range_base_side, y_out)
        print "Hand cmds: ", distal_cmd, base_front_cmd, base_side_cmd
        for i in xrange(4):
            hand.set_pos(i,0,distal_cmd)
        for i in xrange(4):
            hand.set_pos(i,1,base_front_cmd)
    elif demo_types[demo]=="3pinch":
        print "Commanding hand pos"
        distal_cmd=joint_pos_command(range_distal, y_out)
        base_front_cmd=joint_pos_command(range_base_front, y_out)
        base_side_cmd=joint_pos_command(range_base_side, y_out)
        print "Hand cmds: ", distal_cmd, base_front_cmd, base_side_cmd
        for i in xrange(3):
            hand.set_pos(i,0,distal_cmd)
        for i in xrange(3):
            hand.set_pos(i,1,base_front_cmd)
    elif demo_types[demo]=="2pinch":
        print "Commanding hand pos"
        distal_cmd=joint_pos_command(range_distal, y_out)
        base_front_cmd=joint_pos_command(range_base_front, y_out)
        base_side_cmd=joint_pos_command(range_base_side, y_out)
        print "Hand cmds: ", distal_cmd, base_front_cmd, base_side_cmd
        for i in xrange(2):
            hand.set_pos(i,0,distal_cmd)
        for i in xrange(2):
            hand.set_pos(i,1,base_front_cmd)
    elif demo_types[demo]=="rutine1":
        rutine_executer("rutine1", rutine_step)
        rutine_step+=1
        if rutine_step>(len(rutines["rutine1"])-1):
            rutine_step=0

    if demo_types[demo]!="rutine1":
        rutine_step=0
        for i in xrange(5):
            base_side_cmd=joint_pos_command(range_base_side, x_out)
            hand.set_pos(i,2, base_side_cmd)

    hand.update_input()
    hand.send_cmd()
    example_values()
    print
    sleep(0.1)
#----------End Main code------------
