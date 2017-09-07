import yarp as y
from time import sleep

class HandClient:

    #init vars & YARP ports for comm
    def __init__(self):

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
        self.portname_out="/data_client/out"
        self.port_out.open(self.portname_out)
        self.style = y.ContactStyle()
        self.style.persisten = 1
        self.serverportname_in = "/data_server/in"
        y.Network.connect(self.portname_out, self.serverportname_in, self.style)
        self.port_in = y.BufferedPortBottle()
        self.portname_in = "/data_client/in"
        self.port_in.open(self.portname_in)
        self.serverportname_out = "/data_server/out"
        #y.Network.connect(self.serverportname_out, self.portname_in, self.style) #conecta la salida del servidor con la entrada del cliente
        self.listenerportname_in = "/listener/in"
        y.Network.connect(self.serverportname_out, self.listenerportname_in, self.style)

    #close YARP ports for comm
    def __del__(self):
        y.Network.disconnect(self.serverportname_out, self.portname_in, self.style)
        y.Network.disconnect(self.portname_out, self.serverportname_in, self.style)
        y.Network.fini()

    def get_data(self, finger):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("getdata")
        bottle.addInt(finger)
        self.port_out.write()

    def get_all(self):
        bottle = self.port_out.prepare()
        bottle.clear()
        bottle.addString("getall")
        self.port_out.write()


