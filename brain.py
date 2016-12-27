import sys
from sensor.ear import ear
from actor.mouth import mouth
from voiceCommand import voiceCommand
from sensor.pyobd.obd_capture import OBD_Capture
import pdb
from threading import Thread
import time
from sensor.pyobd.obd_controller import OBDController
#add from windows2
talk=mouth()
voiceMsg=ear("testig pheonix")

#-------------------------------------------------------------------------------

def obd_connect(o):
    o.connect()

class OBDConnection(object):
    """
    Class for OBD connection. Use a thread for connection.
    """

    def __init__(self):
        self.c = OBD_Capture()

    def get_capture(self):
        return self.c

    def connect(self):
        self.t = Thread(target=obd_connect, args=(self.c,))
        self.t.start()

    def is_connected(self):
        return self.c.is_connected()

    def get_output(self):
        if self.c and self.c.is_connected():
            return self.c.capture_data()
        return ""

    def get_port(self):
        return self.c.is_connected()

    def get_port_name(self):
        if self.c:
            port = self.c.is_connected()
            if port:
                try:
                    return port.port.name
                except:
                    pass
        return None

    def get_sensors(self):
        sensors = []
        if self.c:
            sensors = self.c.getSupportedSensorList()
        return sensors

#-------------------------------------------------------------------------------

def vcTemp():
    vc=voiceCommand()

    while True:
        talk.speaking("What can I do for you , Sir?")
        getvoiceMsg=voiceMsg.listening()
        talk.speaking(getvoiceMsg)
        print getvoiceMsg

        """if vc.checkCommand(getvoiceMsg):
            vc.runCommand(getvoiceMsg)
        else:
            talk.speaking("i can't understand command: "+getvoiceMsg)

        """

#vcTemp()
def counting():
    num=1
    while 1:
        print num
        time.sleep(1)
        num=num+1



"""
def typeInMode():
    cmd=raw_input("input command to send: ")
    print "getting information of command: "+cmd
    obd.send_command(cmd)
    time.sleep(0.5)
    print "got the following result:"
    print obd.get_result()
"""


obd=OBDController()
obd.connect()

print obd.speed
