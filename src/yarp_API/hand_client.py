import yarp as y
from time import sleep
import ast

##Client class for hand data sending
class HandClient:

    ##Define the fingers and articulations id, then wait for the service called server to be initialized
    def __init__(self):
        ##Default definition fingers id
        self.fingers={
            "Thumb": 0,
            "Index": 1,
            "Middle": 2,
            "Ring": 3,
            "Pinky": 4
        }
        ##Default definition articulations id
        self.arts={
            "Outer": 0,
            "Inner": 1,
            "Abductor": 2
        }

        #init YARP ports
        y.Network.init()
        self.port_out = y.BufferedPortBottle()
        self.portname_out="/client/out"
        self.port_out.open(self.portname_out)
        self.style = y.ContactStyle()
        self.style.persisten = 1
        self.serverportname_in = "/server/in"
        y.Network.connect(self.portname_out, self.serverportname_in, self.style) 
        self.port_in = y.BufferedPortBottle()
        self.portname_in = "/client/in"
        self.port_in.open(self.portname_in)
        self.serverportname_out = "/server/out"
        y.Network.connect(self.serverportname_out, self.portname_in, self.style)

    ##close YARP ports for comm
    def __del__(self):
        y.Network.disconnect(self.serverportname_out, self.portname_in, self.style)
        y.Network.disconnect(self.portname_out, self.serverportname_in, self.style)
        y.Network.fini()
        
    ##Enable finger
    # @param finger int finger id
    def enable(self, finger):
        bottle = self.port_out.prepare() 
        bottle.clear() 
        bottle.addString("enable") 
        bottle.addInt(finger)      
        self.port_out.write() 
        pass
    
    ##Get finger enable state
    # @param finger int finger id
    def enabled(self, finger):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("enabled")
        bottle.addInt(finger)        
        self.port_out.write()
        sleep(5)
        bottle_in = self.port_in.read()
        val = bottle_in.get(0).asDouble()
        return(val)
    
    ##Enable all fingers
    def enable_all(self):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("enableall")        
        self.port_out.write()
        pass
    
    ##Disable finger
    # @param finger int finger id
    def disable(self, finger):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("disable")
        bottle.addInt(finger)        
        self.port_out.write()
        pass
    
    ##Set finger position
    # @param finger int finger id
    # @param joint int articulation id
    # @param pos float position value
    def set_pos(self, finger, joint, pos): 
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("setpos")
        bottle.addInt(finger)
        bottle.addInt(joint) #establece en la posicion 2 el joint
        bottle.addDouble(pos) #establece en la posicion 3 la posicion
        self.port_out.write()
        pass

    ##Set controller mode
    # @param mode int controller mode
    def set_controller_mode(self, mode):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("setcontroller")
        bottle.addInt(mode)
        pass
    
    ##Set finger damping
    # @param finger int finger id
    # @param joint int articulation id
    # @param damping float damping value
    def set_damping(self, finger, joint, damping):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("setdamp")
        bottle.addInt(finger)
        bottle.addInt(joint)
        bottle.addDouble(damping)        
        self.port_out.write()
        pass
    
    ##Set finger stiffness
    # @param finger int finger id
    # @param joint int articulation id
    # @param stiffness float stiffness value
    def set_stiffness(self, finger, joint, stiffness):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("setstiff")
        bottle.addInt(finger)
        bottle.addInt(joint)
        bottle.addDouble(stiffness)        
        self.port_out.write()
        pass
    
    ##Set finger velocity
    # @param finger int finger id
    # @param joint int articulation id
    # @param velocity float velocity value
    def set_velocity(self, finger, joint, velocity):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("setvel")
        bottle.addInt(finger)
        bottle.addInt(joint)
        bottle.addDouble(velocity)        
        self.port_out.write()
        pass

    ##Get joint torque
    # @param finger int finger id
    # @param joint int finger joint
    def get_torque(self, finger, joint):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("gettorque")
        bottle.addInt(finger)
        bottle.addInt(joint)
        self.port_out.write()
        bottle_in = self.port_in.read()
        val = bottle_in.get(0).asDouble()
        return(val)

    ##Get joint velocity
    # @param finger int finger id
    # @param joint int finger joint
    def get_velocity(self, finger, joint):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("getvel")
        bottle.addInt(finger)
        bottle.addInt(joint)
        self.port_out.write()
        bottle_in = self.port_in.read()
        val = bottle_in.get(0).asDouble()
        return(val)

    ##Get joint position
    # @param finger int finger id
    # @param joint int finger joint
    def get_pos(self, finger, joint):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("getpos")
        bottle.addInt(finger)
        bottle.addInt(joint)
        self.port_out.write()
        bottle_in = self.port_in.read()
        val = bottle_in.get(0).asDouble()
        return(val)

    ##Get all data
    def get_data(self):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("getdata")
        self.port_out.write()
        bottle_in = self.port_in.read()
        val = bottle_in.get(0).asString()
        val = ast.literal_eval(val)
        return(val)
    
    ##update fingers inputs. This is for getting the fingers data 
    def update_input(self):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("update")        
        self.port_out.write()
        pass
    
    ##Send queue commands
    def send_cmd(self):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("sendcmd")        
        self.port_out.write()
        pass
    
    ##Send queue commands, wait time, update finger inputs
    # @param time sleep time for the update
    def update(self, time):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("update1")
        bottle.addInt(time)
        self.port_out.write()
        pass



