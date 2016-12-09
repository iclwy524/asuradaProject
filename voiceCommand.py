from sensor.ear import ear
from actor.mouth import mouth

class voiceCommand:
    def __init__(self):
        commandList={'computer':computer,'hello': hello}
        self.commandList=commandList

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
