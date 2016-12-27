import sys
import os
import pdb
from threading import Thread
import time
from sensor.pyobd.obd_controller import OBDController

obd=OBDController()
obd.connect()
t=Thread(target=obd.record_data)
t.start()
while 1:
	print obd.rpm
	if obd.rpm > 1000:
		print "rpm >1000"
