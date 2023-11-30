## PiBug - polling
#
# (C) Copyright 2013 Ottar Kvindesland - LA9IHA
#
# Licence: GPL v.2.0. See https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# 

from machine import Pin
import utime

# Globale brukervariabler
t_pace = 100    # Grunnhastighet, 1 normal prikklengde
out_tone = 440  # Frekvens, audio monitor

# IO-porter
paddle1 = 3     # GPIO pinne for paddlene
paddle2 = 2
out1 = 16       # GPIO pinne for keyer ut, til rig
speaker = 5     # GPIO pinne for høytaler

# Internal house keeping
lastPaddle = 0                   # Start med at ingen paddles har vært trykket inn
spkr = machine.PWM(Pin(speaker)) # Sett opp høytaler for puls breddemodulasjon

sw1  = Pin(paddle1, Pin.IN, Pin.PULL_DOWN) # Definer GPIO for paddles
sw2  = Pin(paddle2, Pin.IN, Pin.PULL_DOWN)
k1 = Pin(out1, Pin.OUT)                    # Definer GPIO for keyer ut

# #######
# Funksjon for å legge keyer ned, altså sette på senderen
# Parameter: s: 0 for prikk og 1 for strek
#
def keyDown(s):
    global lastPaddle
    
    l = 1          # Lengden på et signal er 1
    if s==1:       # men for strek er den
        l = 3      # tre
    lastPaddle = s # Så husker vi siste paddle
    
    spkr.freq(out_tone)  # Start piping i monitor
    spkr.duty_u16(32768) # med 50% duty cycle
    
    k1.value(1)                  # Slå på TX
    utime.sleep(l * t_pace/1000) # Vent til signalet er ferdig
    k1.value(0)                  # Slå av TX
    spkr.duty_u16(0)             # Slå av monitor
    utime.sleep(t_pace/1000)     # Vent en prikklengde

# #######
# Funksjon for å lese paddles og legge keyDown. Hvis begge paddles er inne så gjøres
# det annen hver gang
# Parameter: Ingen
#
def scanPaddles():
    if (sw1.value() + sw2.value()) > 0: # Les Beddle nivåene og hvis minst en er på så
        if lastPaddle == 0:             # hvis siste signal var prikk
            if sw2.value() != 0:        # og paddle 2 er inne
                keyDown(1)              # så send en strek
            elif sw1.value() != 0:      # hvis ikke så er kanskje paddle 1 inne
                keyDown(0)              # da sender du en prikk
        elif lastPaddle == 1:           # Men hvis siste signal var en strek
            if sw1.value() != 0:        # så sjekk om paddle 1 er inne
                keyDown(0)              # da sender du en prikk
            elif sw2.value() != 0:      # hvis ikke sjekk paddle 2, er den inne så
                keyDown(1)              # send en strek
    
while True:        # Til evig tid
    scanPaddles()  # Kjør funksjonen scanPaddles

