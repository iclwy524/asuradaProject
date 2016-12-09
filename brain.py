from sensor.ear import ear
from actor.mouth import mouth
from voiceCommand import voiceCommand

talk=mouth()
voiceMsg=ear("testig pheonix")
vc=voiceCommand()



while True:
    talk.speaking("What can I do for you , Sir?")

    getvoiceMsg=voiceMsg.listening()

    print getvoiceMsg

    if vc.commandList.has_key(getvoiceMsg):
        vc.runCommand(getvoiceMsg)
    else:
        talk.speaking("i can't understand command: "+getvoiceMsg)
