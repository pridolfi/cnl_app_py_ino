#!/usr/bin/python

import wiringpi
import time

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(21, 1)

while True:
    wiringpi.digitalWrite(21, 1)
    time.sleep(0.2)
    wiringpi.digitalWrite(21, 0)
    time.sleep(0.2)

