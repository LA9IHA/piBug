## PiBug - Øvelse 2, Interruptstyring
# 
# (C) Copyright 2024 Ottar Kvindesland - LA9IHA
#
# Licence:     GPL v.2.0. See https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
# Source code: https://github.com/LA9IHA/piBug
#
# Purpose:     Dette er program for artikkel 2 i en serie om hjemmebygging med Raspberry
#              Pico. Denne artikkelen ble beskrevet i Amatørradio, April 2024.
#              Amatørradio utgis av Norsk Radio Relæ Liga, www.nrrl.no
#
# This file:   main.py
#
#

from machine import Pin, Timer, PWM

# IO-ports
paddle1 = 3      # GPIO port paddle 1
paddle2 = 2      # GPIO port paddle 2
speaker = 5      # GPIO port høyttaler
out1 = 16        # GPIO port keyer
prellHold = 20   # Prell ledetid
prellTid = 0     #      Liste indeks for prell tid
prellOpptatt = 1 #      Liste indeks for prell opptatt
prellSistOutput = 2 #   Liste indeks for siste signal
# Prell Liste med underlister for hver paddle
prell = [[0, 0, 0], [prellHold, 0, 0], [prellHold, 0, 0]]
        
# Global user parameters
tFart = 100    # Grunnhastighet, 1 normal prikklengde
toneUt = 440   # Frekvens, audio monitor
    
# Intern husholdning
TILSTANDSMASKIN = []    # Tidsmaskinen er en liste, i tilfelle to kjappe interrupter
lastSig = 0             # Siste signal, prikk eller strek
lockedSig = False       # Begynn med at utsending ikke er på gang
keivhendt = 0           # 1: keivhendt, 2: resten av hurven
dult = 9                # Etter pågående signal: 0: prikk, 1:strek, 9 intet
        
# States for keyer state machine
s_VENT = 0              # Vente, intet skjer
s_PADDLE1 = 1           # Paddle 1 trykket inn
s_PADDLE2 = 2           # Paddle 2 trykket inn
s_STOPP_TX = 3          # Denne skal brukes i neste artikkel
s_KLAR_TX = 4           # Denne også
        
# Sett opp interrupter
spkr = PWM(Pin(speaker))# Sett høyttaler GPIO utgang til puls breddemodulasjon

sw1 = Pin(paddle1, Pin.IN, Pin.PULL_DOWN) # Sett paddle 1 GPIO og trekk ned spenningen ved kontakt
sw2 = Pin(paddle2, Pin.IN, Pin.PULL_DOWN) # Sett paddle 2 GPIO og trekk ned spenningen ved kontakt
        
k1 = Pin(out1, Pin.OUT)  # Sett keyer GPIO til en utgang
k1.value(0)              # Sett keyer output av

def toState(newState):
    # Funksjon for å laste opp tilstanden
    TILSTANDSMASKIN.append(newState)  # Legg ny tilstand til køen
            
#IO translators
def key1(pin):
    # Funksjon for nøkling av paddle 1. Prellhåndtering
    if prell[1][prellOpptatt] == 0:
        prell[1][prellOpptatt] = 1
        toState(s_PADDLE1)
            
def key2(pin):
    # Funksjon for nøkling av paddle 2. Prellhåndtering
    if prell[2][prellOpptatt] == 0:
        prell[2][prellOpptatt] = 1
        toState(s_PADDLE2)

def paddleSignal(p):
    return (keivhendt ^ p) # Signalet ut blir motsatt av innkommende signal

def klikkPaddle(p):
    # Funksjon startet av tilstandsmaskin etter paddle trykket. Start pause for prell
    global dult                          # Global verdi for dulten
    if prell[p][prellSistOutput] == 0:   # Hvis gyldig signal
        if lockedSig == True: dult = p-1 # og sending pågår så lagre dultverdien
    # Sett timer for å avslutte prell perioden
    timer_p = Timer(period=prell[p][prellTid], mode=Timer.ONE_SHOT, callback=lambda t:endprell(p))
    startSig(p-1)                        # Send signalet

def endprell(p):
    # Funksjon for å avslutte prell perioden, både i begynnelsen og slutten av paddle trykking
    prell[p][prellOpptatt] = 0                  # Frigi input
    if p == 1:                                  # Hvis paddle 1
        prell[p][prellSistOutput] = sw1.value() # Lagre paddle 1 verdi i liste, 1 for på og 0 for av
    else:                                       # ellers..
        prell[p][prellSistOutput] = sw2.value() # Lagre paddle 2 verdi i liste, 1 for på og 0 for av

def squeezeKey():
    # Funksjon for å sjekke om paddles er inne etter at signalet er ferdig
    global dult                              # Hent inn verdien av dult
    paddles = sw1.value() + sw2.value()      # paddles > 0 når mins en paddle er inne
    
    if dult < 9:                             # Hvis dult er aktivert
        startSig(dult)                       # Send signal for verdien av dult
        dult = 9                             # og deretter deaktiver dult
    elif paddles > 1: startSig(lastSig ^ 1)  # Ellers, hvis begge paddles inne sendes signal motsatt av forrige gang
    elif paddles > 0:                        
        if sw1.value() == 1:                 # ellers, hvis paddle 1
            prell[2][prellSistOutput] = 0    #   Sett siste output for paddle 2 til 0
            startSig(0)                      #   og send signal for paddle 1
        elif sw2.value() == 1:               # ellers, hvis paddle 2
            prell[1][prellSistOutput] = 0    #   Sett siste output for paddle 1 til 0
            startSig(1)                      #   og send signal for paddle 2
    else:                                    # ellers
        prell[1][prellSistOutput] = 0        #   Sett siste output til 0 for begge paddles
        prell[2][prellSistOutput] = 0
        
def monitor(v):
    # Funksjon for å sende signal på høyttaler
    if v == 1:                # Hvis nivå er 1
        spkr.freq(toneUt)     #   Sett frekvens til variabel toneUt, her 440 Hz
        spkr.duty_u16(32768)  #   Sett duty cycle til 50%
    elif v==0:                # Ellers, hvis nivå er 0
        spkr.duty_u16(0)      #   Sett duty cycle til 0%, altså av

def stoppTx (timer):
    # Funksjon kalt opp når signalet er ferdig
    monitor(0)                # Slå av høyttaler
    k1.value(0)               # Slå av key output
    # Sett en timer for pause etter signalet, lengden av en prikk
    t_pause_bokst = Timer(period=1*tFart, mode=Timer.ONE_SHOT, callback=klarTx)

def klarTx (timer):
    # Funksjon som blir kallt etter pausen etter et signal
    global lockedSig          # Hent inn flagg for lås
    lockedSig = False         # Slå av låsen
    squeezeKey()              # Kjør squeeze key for å sjekke om paddles er ennå inne

def startSig (sig):
    # Funksjon for å sende et signal
    global lockedSig, lastSig    # Hent inn globale variabler
    if not lockedSig:            # Hvis ikke låst så:
        lockedSig = True         # Lås for utsending, kan kun sende ett signal om gangen
        s = paddleSignal(sig)    # Paddle mot prikk/strek, også for kjeivhendte
        lastSig = sig            # Husk siste signal for squeeze
        monitor(1)               # Slå på piping i høyttaler
        k1.value(1)              # Slå på keyer ut
        if s == 0:               # Lag prikk
            t_kort = Timer(period=1*tFart, mode=Timer.ONE_SHOT, callback=stoppTx)
        elif s == 1:             # eller lag strek
            t_lang = Timer(period=3*tFart, mode=Timer.ONE_SHOT, callback=stoppTx)

def sjekkTilstand():
    # Hjerte i programmet, den som sjekker tilstanden
    if len(TILSTANDSMASKIN) > 0:                   # Hvis en tilstand er lagret i maskinen
        tilstand = TILSTANDSMASKIN [0]             # Hent ut første tilstand i køen
        del(TILSTANDSMASKIN [0])                   # Slett den fra køen
        if tilstand == s_PADDLE1: klikkPaddle(1)   # Kall opp funksjonen til tilstanden
        elif tilstand == s_PADDLE2: klikkPaddle(2)
        elif tilstand == s_STOPP_TX: stoppTx()
        elif tilstand == s_KLAR_TX: klarTx()
        elif tilstand == s_BOKSTAVROM: klarTx()
        tilstand = s_VENT

sw1.irq(key1, Pin.IRQ_RISING) # Slå på interrupt for paddle 1 på stigende flanke
sw2.irq(key2, Pin.IRQ_RISING) # Slå på interrupt for paddle 2 på stigende flanke

while True:          # Gjenta til evig tid
    sjekkTilstand () # Kall opp funksjonen sjekk tilstand