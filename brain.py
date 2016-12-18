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


#t=Thread(target=counting)
#t.start()

obd=OBDController()
obd.connect()


if not obd.is_connected():
	print "not connected"
	print obd.is_connected()
	print "not connected"


while 1:
	cmd=raw_input("in put to send: ")
	print "getting information of command: "+cmd
	obd.send_command(cmd)
	print "got the following result:"
	print obd.get_result() 
#vcTemp()
