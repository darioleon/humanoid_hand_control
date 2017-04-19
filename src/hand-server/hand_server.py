#!/usr/bin/env python

import yarp as y
from time import sleep

class HandServer:

    #init vars & YARP ports for comm
    def __init__(self):
        #global vars for a Hand object
        self.hand_out={"Con_Mod": 0.0,
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

        self.hand_out_keys=["Con_Mod", "Enable", "Pos_Com", "Stiffness", "Damping", "Velocity", "Kp", "Con_Mod1", "Enable1", "Pos_Com1", "Stiffness1", "Damping1", "Velocity1", "Kp1", "emergency"]

        self.hand_in={"Pos": [0.0]*15,
                 "Torque": [0.0]*15,
                 "Velocity": [0.0]*15,
                 "Enabled": [0.0]*5,
                 "brakestatus": 0.0,
                 "handconfig": [0.0]*2,
                 "commstatus": 0.0,
                 "Pos1": [0.0]*15,
                 "Torque1": [0.0]*15,
                 "Velocity1": [0.0]*15,
                 "Enabled1": [0.0]*5,
            }

        self.hand_in_keys=["Pos",
                      "Velocity",
                      "Enabled",
                      "brakestatus",
                      "handconfig",
                      "Torque",
                      "commstatus",
                      "Pos1",
                      "Torque1",
                      "Velocity1",
                      "Enabled1"]

        self.hand_cal=[[0.,0.,0.],
                  [0.,0.,0.],
                  [0.,0.,0.],
                  [0.,0.,0.]]

        self.fingers={
            "Thumb": 0,
            "Index": 1,
            "Middle": 2,
            "Ring": 3,
            "Pinky": 4
        }

        self.arts={
            "Outer": 0,
            "Inner": 1,
            "Abductor": 2
        }

        #init YARP ports
        y.Network.init()
        self.port_out = y.BufferedPortBottle()
        self.portname_out="/handclient/out"
        self.port_out.open(self.portname_out)
        self.style = y.ContactStyle()
        self.style.persisten = 1
        self.handportname_in = "/hand/in"
        y.Network.connect(self.portname_out, self.handportname_in, self.style)
        self.port_in = y.BufferedPortBottle()
        self.portname_in = "/handclient/in"
        self.port_in.open(self.portname_in)
        self.handportname_out = "/hand/out"
        y.Network.connect(self.handportname_out, self.portname_in, self.style)
        self.portsrv_in = y.BufferedPortBottle()
        self.portsrv_in.open("/server/in")
        self.portsrv_out = y.BufferedPortBottle()
        self.portsrv_out.open("/server/out")

    #close YARP ports for comm
    def __del__(self):
        y.Network.disconnect(self.handportname_out, self.portname_in, self.style)
        y.Network.disconnect(self.portname_out, self.handportname_in, self.style)
        y.Network.fini()

    def enable(self, finger):
        self.hand_out["Enable"][finger] = 1.0
        pass

    def enabled(self, finger):
        return(self.hand_in["Enabled"][finger])

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
            print self.hand_out["Enable"]
            print self.hand_in["Enabled"]
            while self.enabled(i) > 0.0:
                self.update_input()
                sleep(0.1)
                print "Disabling"
                print self.hand_out["Enable"]
                print self.hand_in["Enabled"]
        for i in xrange(5):
            self.enable(i)
            self.send_cmd()
            print "Enabling"
            print self.hand_out["Enable"]
            print self.hand_in["Enabled"]
            while self.enabled(i) < 1.0:
                self.update_input()
                sleep(0.1)
                print "Enabling"
                print self.hand_out["Enable"]
                print self.hand_in["Enabled"]

    def disable(self, finger):
        self.hand_out["Enable"][finger] = 0.0
        pass

    def set_pos(self, finger, joint, pos):
        print "set_pos"
        self.hand_out["Pos_Com"][finger*3+joint] = pos
        pass

    def set_controller_mode(self, mode):
        self.hand_out["Con_Mod"] = mode

	def set_damping(self, finger, joint, damping):
		self.hand_out["Damping"][finger*3+joint] = damping
		pass

    def set_stiffness(self, finger, joint, stiffness):
        self.hand_out["Stiffness"][finger*3+joint] = stiffness
        pass

    def set_stiffness(self, finger, stiffness):
        for i in xrange(3):
            self.hand_out["Stiffness"][finger*3+i] = stiffness
        pass

	def set_velocity(self, finger, joint, velocity):
		self.hand_out["Velocity"][finger*3+joint] = velocity
		pass
		
    #pseudo-protocol for routines
    #routine: [[command, val], ...]
    #ex: [["enable",val], ["stiffness",val], ["move",val], ["sleep,val"], ["move",val], ["sleep,val"], ["move",val], ...]
    #enable, [val, val, val, val, val]
    #move, [finger, joint, angle],[finger, joint, angle],[finger, joint, angle],[finger, joint, angle],[finger, joint, angle]
    #move, [finger, angle, angle, angle], [finger, angle, angle, angle], [finger, angle, angle, angle], [finger, angle, angle, angle]
    #stiffness, [finger, angle, angle, angle], [finger, angle, angle, angle], [finger, angle, angle, angle], [finger, angle, angle, angle]
    #velocity, [finger, angle, angle, angle], [finger, angle, angle, angle], [finger, angle, angle, angle], [finger, angle, angle, angle]
    #sleep, val
    def routine(self, routine=[["enable",[1,1,0,0,0]],  
		       ["sleep", 3],
		       ["move",["Thumb","Outer",40],["Index","Outer",60]], 
		       ["sleep", 3], 
		       ["move",["Thumb","Outer",0],["Index","Outer",0]], 
		       ["sleep", 3]]):
		#init code here for routine
		for step in routine:
			cmd = step[0]
			#"switch" for command
			#TODO: do checks for every command
			if cmd == "enable":
				val = step[1]
				for i in xrange(len(val)):
					self.disable(i)
					self.update(1)
					if val[i]:
						self.enable(i)
						self.update(1)
			elif cmd == "move":
				scd_arg = step[1][1]
				#check second argument 
				if type(scd_arg) is str:
					for i in xrange(1, len(step)):
						sub_cmd = step[i]
						self.set_pos(self.fingers[sub_cmd[0]], self.arts[sub_cmd[1]], sub_cmd[2])
					self.update(1)
				else:
					for i in xrange(1, len(step)):
						sub_cmd = step[i]
						self.set_pos(self.fingers[sub_cmd[0]], 0, sub_cmd[1])
						self.set_pos(self.fingers[sub_cmd[0]], 1, sub_cmd[2])
						self.set_pos(self.fingers[sub_cmd[0]], 2, sub_cmd[3])
					self.update(1)
			elif cmd == "stiffness":
				for i in xrange(1, len(step)):
					sub_cmd = step[i]
					self.set_stifness(self.fingers[sub_cmd[0]], 0, sub_cmd[1])
					self.set_stifness(self.fingers[sub_cmd[0]], 1, sub_cmd[2])
					self.set_stifness(self.fingers[sub_cmd[0]], 2, sub_cmd[3])
				self.update(1)
			elif cmd == "velocity":
				for i in xrange(1, len(step)):
					sub_cmd = step[i]
					self.set_velocity(self.fingers[sub_cmd[0]], 0, sub_cmd[1])
					self.set_velocity(self.fingers[sub_cmd[0]], 1, sub_cmd[2])
					self.set_velocity(self.fingers[sub_cmd[0]], 2, sub_cmd[3])
				self.update(1)
			elif cmd == "sleep":
		    		sleep(step[1])

    def update_input(self):
        print "INPUT"
        bottle_in = self.port_in.read()
        j = 0
        for item in self.hand_in_keys:
            if type(self.hand_in[item]) == list:
                for i in xrange(len(self.hand_in[item])):
                    self.hand_in[item][i] = bottle_in.get(j).asDouble()
                #print "j, hand in", j, hand_in
                    j += 1
            else:
                self.hand_in[item] = bottle_in.get(j).asDouble()
            #print "j, hand in ", j, hand_in
                j += 1
        for item in self.hand_in_keys:
            #print "Item", item, "value: ", hand_in[item]
            pass

    def send_cmd(self):
        print "OUTPUT"
        bottle = self.port_out.prepare()
        bottle.clear()
        for item in self.hand_out_keys:
            #print "item: ", item, "Value: ", hand_out[item]
            if type(self.hand_out[item]) == list:
                for x in self.hand_out[item]:
                    bottle.addDouble(x)
            else:
                bottle.addDouble(self.hand_out[item])
        self.port_out.write()
        pass

    def update(self, time=0):
        self.send_cmd()
        if time != 0:
	        sleep(time)
        self.update_input()

    def init_daemon(self):
        time = 2
        while(True):            
            bottle_in = self.portsrv_in.read()
            bottle_out = self.portsrv_out.prepare()
            command = bottle_in.get(0).asString()
            print command
            if command == "enable":
                finger = bottle_in.get(1).asInt()
                print finger
                self.enable(finger)
            elif command == "enabled":
                finger = bottle_in.get(1).asInt()
                val = self.enabled(finger)
                bottle_out.clear()
                bottle_out.addDouble(val)
                self.portsrv_out.write()
            elif command == "enableall":
                self.enable_all()
            elif command == "disable":
                finger = bottle_in.get(1).asInt()
                print finger
                self.disable(finger)
            elif command == "setcontroller":
                mode = botlle_in.get().asInt()
                print mode
                self.set_controller_mode(mode)
            elif command == "setpos":
                finger = bottle_in.get(1).asInt()
                joint = bottle_in.get(2).asInt()
                pos = bottle_in.get(3).asDouble()
                print finger 
                print joint 
                print pos
                self.set_pos(finger, joint, pos)
            elif command == "setdamp":
                finger = bottle_in.get(1).asInt()
                joint = bottle_in.get(2).asInt()
                damp = bottle_in.get(3).asDouble()
                print finger 
                print joint 
                print damp
                self.set_damping(finger, joint, damp)
            elif command == "setstiff":                
                finger = bottle_in.get(1).asInt()
                joint = bottle_in.get(2).asInt()
                stiff = bottle_in.get(3).asDouble()
                print finger 
                print joint 
                print stiff
                self.set_stiffness(finger, joint, stiff)
            elif command == "setvel":
                finger = bottle_in.get(1).asInt()
                joint = bottle_in.get(2).asInt()
                vel = bottle_in.get(3).asDouble()
                print finger 
                print joint 
                print vel
                self.set_velocity(finger, joint, vel)
            elif command == "update":
                self.update_input()
            elif command == "setvel":
                self.send_cmd()
            self.update(time)

if __name__ == "__main__":
    hand = HandServer()
    hand.set_controller_mode(1)
    while(True):
        hand.init_daemon()

