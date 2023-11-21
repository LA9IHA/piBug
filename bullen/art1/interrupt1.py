## PiBug - interrupt 1
#
# (C) Copyright 2013 Ottar Kvindesland - LA9IHA
#
# Licence: GPL v.2.0. See https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
#
from machine import Pin, Timer, PWM

# Global user parameters
t_pace = 100    # Grunnhastighet, 1 normal prikklengde
out_tone = 440  # Frekvens, audio monitor

# IO-ports
paddle1 = 3
paddle2 = 2
speaker = 5
out1 = 16
        
# Internal house keeping
TILSTANDSMASKIN = []
locked_sig = False

# States for keyer state machine
s_VENT = 0
s_PADDLE1 = 1
s_PADDLE2 = 2
s_STOPP_TX = 3
s_KLAR_TX = 4

# Tilstandsmaskinen
def toState(newState):
    global TILSTANDSMASKIN
    TILSTANDSMASKIN.append(newState)

# IO translators
def key1(pin):
    toState(s_PADDLE1)

def key2(pin):
    toState(s_PADDLE2)

def monitor(v):
    if v == 1:
        spkr.freq(out_tone)
        spkr.duty_u16(32768)
    elif v==0:
        spkr.duty_u16(0)

def start_sig (s):
    global locked_sig
    if not locked_sig:
        locked_sig = True
        monitor(1)
        k1.value(1)
        if s == 0:
            t_kort = Timer(period=1*t_pace, mode=Timer.ONE_SHOT, callback=stoppTx)
        elif s==1:
            t_lang = Timer(period=3*t_pace, mode=Timer.ONE_SHOT, callback=stoppTx)

def stoppTx (timer):
    monitor(0)
    k1.value(0)
    t_pause_kort = Timer(period=1*t_pace, mode=Timer.ONE_SHOT, callback=klarTx)

def klarTx (timer):
    global locked_sig
    locked_sig = False

def sjekkTilstand():
    global TILSTANDSMASKIN
    if len(TILSTANDSMASKIN) > 0:
        tilstand = TILSTANDSMASKIN [0]
        del(TILSTANDSMASKIN [0])
        if tilstand == s_PADDLE1: start_sig(0)
        elif tilstand == s_PADDLE2: start_sig(1)
        elif tilstand == s_STOPP_TX: stoppTx()
        elif tilstand == s_KLAR_TX: klarTx()
        tilstand = s_VENT

spkr = PWM(Pin(speaker))

sw1 = Pin(paddle1, Pin.IN, Pin.PULL_DOWN)
sw1.irq(key1, Pin.IRQ_RISING)

sw2 = Pin(paddle2, Pin.IN, Pin.PULL_DOWN)
sw2.irq(key2, Pin.IRQ_RISING)
        
k1 = Pin(out1, Pin.OUT)
k1.value(0)

while True:
    sjekkTilstand ()
