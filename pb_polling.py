## PiBug - polling
#
# (C) Copyright 2013 Ottar Kvindesland - LA9IHA
#
# Licence: GPL v.2.0. See https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
#

from machine import Pin
import utime

# Global user parameters
t_pace = 100    # Grunnhastighet, 1 normal prikklengde
out_tone = 440  # Frekvens, audio monitor

# IO-ports
paddle1 = 3
paddle2 = 2
out1 = 16
speaker = 5

# Internal house keeping
lastPaddle = 0
spkr = machine.PWM(Pin(speaker))

sw1  = Pin(paddle1, Pin.IN, Pin.PULL_DOWN)
sw2  = Pin(paddle2, Pin.IN, Pin.PULL_DOWN)
k1 = Pin(out1, Pin.OUT)

def keyDown(s):
    global lastPaddle
    
    l = 1
    if s==1:
        l = 3
    lastPaddle = s
    
    spkr.freq(out_tone)
    spkr.duty_u16(32768)
    
    k1.value(1)
    utime.sleep(l * t_pace/1000)
    k1.value(0)
    spkr.duty_u16(0)
    utime.sleep(t_pace/1000)

def scanPaddles():
    if (sw1.value() + sw2.value()) > 0:
        if lastPaddle == 0:
            if sw2.value() != 0:
                keyDown(1)
            elif sw1.value() != 0:
                keyDown(0)
        elif lastPaddle == 1:
            if sw1.value() != 0:
                keyDown(0)
            elif sw2.value() != 0:
                keyDown(1)
    
while True:
    scanPaddles()

