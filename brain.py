from sensor.ear import ear
from actor.mouth import mouth
from voiceCommand import voiceCommand
from sensor.pyobd.obd_io import OBDPort
#add from rpi
talk=mouth()
voiceMsg=ear("testig pheonix")
#vc=voiceCommand()
obd=OBDPort()
print obd.get_dtc()

while True:
    talk.speaking("What can I do for you , Sir?")

    getvoiceMsg=voiceMsg.listening()

    print getvoiceMsg

    if vc.commandList.has_key(getvoiceMsg):
        vc.runCommand(getvoiceMsg)
    else:
        talk.speaking("i can't understand command: "+getvoiceMsg)
