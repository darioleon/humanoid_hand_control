#!/usr/bin/env python

import yarp as y
from time import sleep
import cwiid as w

y.Network.init()
port_out=y.BufferedPortBottle()
portname_out="/handclient/out"
port_out.open(portname_out)
style=y.ContactStyle()
style.persisten=1
handportname_in="/hand/in"
y.Network.connect(portname_out, handportname_in, style)
port_in=y.BufferedPortBottle()
portname_in="/handclient/in"
port_in.open(portname_in)
handportname_out="/hand/out"
y.Network.connect(handportname_out, portname_in, style)

#----------Joystick initialization------------
import pygame as pg
pg.init()
pg.joystick.init()
js=pg.joystick.Joystick(0)
js.init()
y_out=0.







#----------dual shock code------------------
#getting position from joystick


while True:
    pg.event.get()


    #getting position from left joystick
    x1=js.get_axis(0)       #Left joystick left to right values -1.0 to 0.99
    y1=js.get_axis(1)       #Left joystick up to down values -1.0 to 0.99

    y_out=-y1              #Controller gives negative values for the upbutton
    x_out=x1

    print "                                                   y_out:", y_out,"x_out:", x_out

#getting position from right joystick
#x2=js.get_axis(2)   #Left joystick left to right values -1.0 to 0.99
#y2=js.get_axis(3)   #Left joystick up to down values -1.0 to 0.99
#y2_out=-y2          #Controller gives negative values for the upbutton
#x2_out=x2
#-------------------------------------------







#---------------------------------------------

hand_out={"Con_Mod": 0.0,
      "Enable": [0.0]*5,
      "Pos_Com": [0.0]*15,
      "Stiffness": [0.023]*15,
      "Damping": [0.0]*15,
      "Velocity": [120.0]*15,
      "Kp": [5.0]*15,
      "Con_Mod1": 0.0,
      "Enable1": [0.0]*5,
      "Pos_Com1": [0.0]*15,
      "Stiffness1": [0.023]*15,
      "Damping1": [0.0]*15,
      "Velocity1": [120.0]*15,
      "Kp1": [5.0]*15,
      "emergency": 0.0

    }

hand_out_keys=["Con_Mod", "Enable", "Pos_Com", "Stiffness", "Damping", "Velocity", "Kp", "Con_Mod1", "Enable1", "Pos_Com1", "Stiffness1", "Damping1", "Velocity1", "Kp1", "emergency"]

hand_in={"Pos": [0.0]*15,
         "Torque": [0.0]*15,
         "Velocity": [0.0]*15,
         "Enabled": [0.0]*5,
         "breakstatus": 0.0,
         "handconfig": [0.0]*2,
         "commstatus": 0.0,
         "Pos1": [0.0]*15,
         "Torque1": [0.0]*15,
         "Velocity1": [0.0]*15,
         "Enabled1": [0.0]*5,
    }

hand_in_keys=["Pos",
              "Torque",
              "Velocity",
              "Enabled",
              "breakstatus",
              "handconfig",
              "commstatus",
              "Pos1",
              "Torque1",
              "Velocity1",
              "Enabled1"]

class Hand:
    def __init__(self):
        pass

    def enable(self, finger):
        hand_out["Enable"][finger]=1.0
        pass

    def enabled(self, finger):
        return(hand_in["Enabled"][finger])

    def enable_all(self):
        self.disable(0)
        self.update_input()
        self.send_cmd()
        sleep(2)
        self.enable(0)
        self.update_input()
        self.send_cmd()
        
        for i in xrange(5):
            self.disable(i)
            self.send_cmd()
            sleep(2)
            print "Disabling"
            print hand_out["Enable"]
            print hand_in["Enabled"]
            while self.enabled(i)>0.0:
                self.update_input()
                sleep(0.1)
                print "Disabling"
                print hand_out["Enable"]
                print hand_in["Enabled"]
        for i in xrange(4):
            self.enable(i)
            self.send_cmd()
            print "Enabling"
            print hand_out["Enable"]
            print hand_in["Enabled"]
            while self.enabled(i)<1.0:
                self.update_input()
                sleep(0.1)
                print "Enabling"
                print hand_out["Enable"]
                print hand_in["Enabled"]

    def disable(self, finger):
        hand_out["Enable"][finger]=0.0
        pass

    def set_pos(self, finger, joint, pos):
        hand_out["Pos_Com"][finger*3+joint]=pos
        pass

    def set_controller_mode(self, mode):
        hand_out["Con_Mod"]=mode

    def set_stiffness(self, finger, joint, stiffness):
        pass

    def update_input(self):
        print "INPUT"
        bottle_in=port_in.read()
        j=0
        for item in hand_in_keys:
            if type(hand_in[item])==list:
                for i in xrange(len(hand_in[item])):
                    hand_in[item][i]=bottle_in.get(j).asDouble()
                #print "j, hand in", j, hand_in
                    j+=1
            else:
                hand_in[item]=bottle_in.get(j).asDouble()
            #print "j, hand in ", j, hand_in
                j+=1
        for item in hand_in_keys:
            #print "Item", item, "value: ", hand_in[item]
            pass

    def send_cmd(self):
        print "OUTPUT"
        bottle=port_out.prepare()
        bottle.clear()
        for item in hand_out_keys:
            #print "item: ", item, "Value: ", hand_out[item]
            if type(hand_out[item])==list:
                for x in hand_out[item]:
                    bottle.addDouble(x)
            else:
                bottle.addDouble(hand_out[item])
        port_out.write()
        pass

def example_values():
    hand.enable(1) #enable thumb
    hand.set_controller_mode(1)
    hand.set_pos(1, 0, 40)

hand=Hand()





#----------------------------------------------Wii code--------------------------------------------
'''
print "Press 1 and 2 buttons at once now"
wm=w.Wiimote()
print "Wiimote connected"
wm.rpt_mode=w.RPT_NUNCHUK
while not 'nunchuk' in wm.state.keys():
    print "Waiting for nunchuk"
print "nunchuk present"


print "Don't touch joystick. Calibrating zero"
y_center=0.
y=0
while y==0:
    x,y=wm.state['nunchuk']['stick']

for i in xrange(100):
    x,y=wm.state['nunchuk']['stick']
    y_center+=y
x_center=0.
x=0
while x==0:
    x,y=wm.state['nunchuk']['stick']

for i in xrange(100):
    x,y=wm.state['nunchuk']['stick']
    x_center+=x


y_center/=100.0
x_center/=100.0
print "Center calibrated: ", x_center, y_center

print "When ready press any button and Move up and down. Then press any button when finished"
while wm.state['nunchuk']['buttons']==0:
    pass
sleep(0.1)
while wm.state['nunchuk']['buttons']!=0:
    pass
sleep(0.1)
y_max=0.
y_min=200.
x_max=0.
x_min=200.
while wm.state['nunchuk']['buttons']==0:
    x,y=wm.state['nunchuk']['stick']
    if y>y_max:
        y_max=y
        print "Y Max: ", y
    if y<y_min:
        y_min=y
        print "Y Min: ", y
    if x>x_max:
        x_max=x
        print "X Max: ", x
    if x<x_min:
        x_min=x
        print "X Min: ", x
    sleep(0.01)

print "Max and min values", x_max, x_min, y_max, y_min

print "When ready press any button to continue"
while wm.state['nunchuk']['buttons']==0:
    pass

y_min-=y_center
y_max-=y_center
x_min-=x_center
x_max-=x_center

y_out=0.
'''
#---------------------------------------------------------------------------------
for i in xrange(100):
    hand.update_input()
    sleep(0.01)
hand.enable_all()

range_distal=(5.,30.)
range_base_front=(5.,30.)
range_base_side=(-20.,20.)

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

while True:
    #--------------Wii code------------------------------------------------------
    '''
    x,y=wm.state['nunchuk']['stick']
    accx,accy,accz=wm.state['nunchuk']['acc']
    buttons=wm.state['nunchuk']['buttons']
    print wm.state
    y_out=y-y_center
    x_out=x-x_center
    if y_out>0.:
        y_out/=y_max
    else:
        y_out/=-y_min
    if x_out>0.:
        x_out/=x_max
    else:
        x_out/=-x_min
    print y_out, x_out
    '''

    #------------------------------------------------------------------------------
    
    #----------dual shock code------------------
    #getting position from joystick
    pg.event.get()


    #getting position from left joystick
    x1=js.get_axis(0)       #Left joystick left to right values -1.0 to 0.99
    y1=js.get_axis(1)       #Left joystick up to down values -1.0 to 0.99

    y_out=-y1              #Controller gives negative values for the upbutton
    x_out=x1

    print "                                                   y_out:", y_out,"x_out:", x_out

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
