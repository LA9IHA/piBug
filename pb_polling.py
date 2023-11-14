## PiBug - polling
#
# (C) Copyright 2013 Ottar Kvindesland - LA9IHA
#
# Licence: GPL v.2.0. See https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
#

from machine import Pin
import utime

# Global user parameters
t_pace = 100    # Base speed, 1 normal dot length - prikk
out_tone = 440  # Frequency, audio monitor

# IO-ports
paddle1 = 3 # GPIO pin id for paddle 1
paddle2 = 2 # GPIO pin id for paddle 2
out1 = 16  # GPIO pin id for rig output
speaker = 5  # GPIO pin id for speaker

# Internal house keeping
lastPaddle = 0  # Last paddle pressed
spkr = machine.PWM(Pin(speaker)) # Make speaker output a Pulse Width Modulation - PWM

sw1  = Pin(paddle1, Pin.IN, Pin.PULL_DOWN) # Set up paddle1 and assign to sw1
sw2  = Pin(paddle2, Pin.IN, Pin.PULL_DOWN) # Set up paddle2 and assign to sw2
k1 = Pin(out1, Pin.OUT)  # Assign to rig output to k1.
         # For future experiments, why not have multiple outputs, one for each rig?
         # Also, you can define an output to go active low at TX

# What happens when a addle is pressed
def keyDown(s):
    global lastPaddle # Tagged global in order to make value changes effective
    
    l = 1     # Signal length - prikk
    if s==1:
        l = 3 # Signal length 3: strek
    lastPaddle = s
    
    spkr.freq(out_tone)  # Start beep
    spkr.duty_u16(32768) # Set duty cycle to 50%
    
    k1.value(1)                  # Key TC (or turn on LED)
    utime.sleep(l * t_pace/1000) # Wait a bit
    k1.value(0)                  # and turn off everything
    spkr.duty_u16(0)
    utime.sleep(t_pace/1000)     # and wait one prikk

def scanPaddles():
    if (sw1.value() + sw2.value()) > 0: # Are any paddle squeezed in?
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
    
while True: # Forever
    scanPaddles()

