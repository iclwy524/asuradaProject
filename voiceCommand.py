from sensor.ear import ear
from actor.mouth import mouth
#from sensor.pyobd.obd_io import OBDPort
from sensor.pyobd.obd_capture import OBD_Capture


class voiceCommand:
    def __init__(self):
        pass

    def computer(self):
        print "receive command computer"

    def hello(self):
        print "hello"

    def runCommand(self,actionToDo):
        try:
            func=self.commandList.get(actionToDo)
            return func()
        except:
            print "no command found"
            talk.speaking("no command found")

    def checkCommand(self,commandToCheck):

	commandList={'computer':computer,'hello':hello}
        return(commandList.has_key(commandToCheck))


if __name__=="__main__":
    hello()
