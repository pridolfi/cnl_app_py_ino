#!/usr/bin/python

import wiringpi
import time
import sdnotify

n = sdnotify.SystemdNotifier()
n.notify("READY=1")

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(20, 1)

while True:
    wiringpi.digitalWrite(20, 1)
    time.sleep(1)
    wiringpi.digitalWrite(20, 0)
    time.sleep(1)
    n.notify("WATCHDOG=1")
