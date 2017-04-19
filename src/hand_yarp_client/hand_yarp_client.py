import yarp as y

class Hand:
    #init vars & YARP ports for comm #multicopter-hardware
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
            "Thumb":0,
            "Index":1,
            "Middle":2,
            "Ring":3,
            "Pinky":4
        }

        #outer, inner, abductor
        self.arts={
            "Outer":0,
            "Inner":1,
            "Abductor":2
        }

        #init YARP ports
        y.Network.init()
        self.port_out=y.BufferedPortBottle()
        self.portname_out="/handclient/out"
        self.port_out.open(self.portname_out)
        self.style=y.ContactStyle()
        self.style.persisten=1
        self.handportname_in="/hand/in"
        y.Network.connect(self.portname_out, self.handportname_in, self.style)
        self.port_in=y.BufferedPortBottle()
        self.portname_in="/handclient/in"
        self.port_in.open(self.portname_in)
        self.handportname_out="/hand/out"
        y.Network.connect(self.handportname_out, self.portname_in, self.style)

    #close YARP ports for comm
    def __del__(self):
        y.Network.connect(self.handportname_out, self.portname_in, self.style)
        y.Network.connect(self.portname_out, self.handportname_in, self.style)
        y.Network.fini()

    def enable(self, finger):
        self.hand_out["Enable"][finger]=1.0
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
            while self.enabled(i)>0.0:
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
            while self.enabled(i)<1.0:
                self.update_input()
                sleep(0.1)
                print "Enabling"
                print self.hand_out["Enable"]
                print self.hand_in["Enabled"]

    def disable(self, finger):
        self.hand_out["Enable"][finger]=0.0
        pass

    def set_pos(self, finger, joint, pos):
        self.hand_out["Pos_Com"][finger*3+joint]=pos
        pass

    def set_controller_mode(self, mode):
        self.hand_out["Con_Mod"]=mode

    def set_stiffness(self, finger, joint, stiffness):
        self.hand_out["Stiffness"][finger*3+joint]=stiffness
        pass

    def set_stiffness(self, finger stiffness):
        for i in range(3):
            self.hand_out["Stiffness"][finger*3+i]=stiffness
        pass

    #pseudo-protocol for routines
    #routine: [[command, val], ...]
    #ex: [["enable",val], ["stiffness",val], ["pos_cmd",val], ["pos_cmd",val], ["pos_cmd",val], ...]
    #enable, [val, val, val, val, val]
    #pos_cmd, [[finger, joint, angle],[finger, joint, angle],[finger, joint, angle],[finger, joint, angle],[finger, joint, angle]]
    #stiffness, [[finger, joint, angle],[finger, joint, angle],[finger, joint, angle],[finger, joint, angle],[finger, joint, angle]]
    #velocity, [[finger, joint, angle],[finger, joint, angle],[finger, joint, angle],[finger, joint, angle],[finger, joint, angle]]
    def routine(self, routine):
        pass

    def update_input(self):
        print "INPUT"
        bottle_in=self.port_in.read()
        j=0
        for item in self.hand_in_keys:
            if type(self.hand_in[item])==list:
                for i in xrange(len(self.hand_in[item])):
                    self.hand_in[item][i]=bottle_in.get(j).asDouble()
                #print "j, hand in", j, hand_in
                    j+=1
            else:
                self.hand_in[item]=bottle_in.get(j).asDouble()
            #print "j, hand in ", j, hand_in
                j+=1
        for item in self.hand_in_keys:
            #print "Item", item, "value: ", hand_in[item]
            pass

    def send_cmd(self):
        print "OUTPUT"
        bottle=self.port_out.prepare()
        bottle.clear()
        for item in self.hand_out_keys:
            #print "item: ", item, "Value: ", hand_out[item]
            if type(self.hand_out[item])==list:
                for x in self.hand_out[item]:
                    bottle.addDouble(x)
            else:
                bottle.addDouble(self.hand_out[item])
        self.port_out.write()
        pass

    def update(self, time=0):
        self.send_cmd()
        self.update_input()
