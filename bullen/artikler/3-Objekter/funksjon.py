## PiBug - funksjon
#
# (C) Copyright 2024 Ottar Kvindesland - LA9IHA
#
# Licence: GPL v.2.0. See https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# 
# Dette er en del av Artikkel 3 i Amatørradio Juni 2024 utgitt av Norsk Radio Relæ Liga.
# Her styres tastaturet.
# 
from keyer import Keyer

class Funksjoner(Keyer):  # Definer klassen og arv klassen Keyer
    from machine import Pin, Timer, PWM
    
    def __init__(self):
        super().__init__()
        
        # Global user parameters
        # IO-ports
        self.knapp1 = 7
        self.knapp2 = 8
        self.knapp3 = 9
        self.knapp4 = 10
        self.knapp5 = 11
        self.knapp6 = 12
        
        self.prell = []
        self.prellhold = 20
        self.prellTid = 0
        self.prellOpptatt = 1
        self.prellSistOutput = 2
        for n in range (1, 7):
            self.prell.append([self.prellhold, 0, 0])
        
        # Internal house keeping
        self.nyttOrd = 0
        self.sisteOrd = 0
        self.knappMatrix = 0
        self.knappAktiv = False
        
        # Sett opp interrupter
        self.kn1 = self.Pin(self.knapp1, self.Pin.IN, self.Pin.PULL_DOWN)
        self.kn1.irq(self.iknapp1, self.Pin.IRQ_RISING)

        self.kn2 = self.Pin(self.knapp2, self.Pin.IN, self.Pin.PULL_DOWN)
        self.kn2.irq(self.iknapp2, self.Pin.IRQ_RISING)

        self.kn3 = self.Pin(self.knapp3, self.Pin.IN, self.Pin.PULL_DOWN)
        self.kn3.irq(self.iknapp3, self.Pin.IRQ_RISING)

        self.kn4 = self.Pin(self.knapp4, self.Pin.IN, self.Pin.PULL_DOWN)
        self.kn4.irq(self.iknapp4, self.Pin.IRQ_RISING)

        self.kn5 = self.Pin(self.knapp5, self.Pin.IN, self.Pin.PULL_DOWN)
        self.kn5.irq(self.iknapp5, self.Pin.IRQ_RISING)

        self.kn6 = self.Pin(self.knapp6, self.Pin.IN, self.Pin.PULL_DOWN)
        self.kn6.irq(self.iknapp6, self.Pin.IRQ_RISING)

    #IO translators
    def iknapp6(self, pin):
        knr = 0
        if self.prell[knr][self.prellOpptatt] == 0:
            self.prell[knr][self.prellOpptatt] = 1
            self.timer_k6 = self.Timer(period=self.prell[knr][self.prellTid], mode=self.Timer.ONE_SHOT, callback=lambda t, s=self: s.endprell(knr))
    
    def iknapp5(self, pin):
        knr = 1
        if self.prell[knr][self.prellOpptatt] == 0:
            self.prell[knr][self.prellOpptatt] = 1
            self.timer_k5 = self.Timer(period=self.prell[knr][self.prellTid], mode=self.Timer.ONE_SHOT, callback=lambda t, s=self: s.endprell(knr))
            
    def iknapp4(self, pin):
        knr = 2
        if self.prell[knr][self.prellOpptatt] == 0:
            self.prell[knr][self.prellOpptatt] = 1
            self.timer_k4 = self.Timer(period=self.prell[knr][self.prellTid], mode=self.Timer.ONE_SHOT, callback=lambda t, s=self: s.endprell(knr))

    def iknapp3(self, pin):
        knr = 3
        if self.prell[knr][self.prellOpptatt] == 0:
            self.prell[knr][self.prellOpptatt] = 1
            self.timer_k3 = self.Timer(period=self.prell[knr][self.prellTid], mode=self.Timer.ONE_SHOT, callback=lambda t, s=self: s.endprell(knr))

    def iknapp2(self, pin):
        knr = 4
        if self.prell[knr][self.prellOpptatt] == 0:
            self.prell[knr][self.prellOpptatt] = 1
            self.timer_k2 = self.Timer(period=self.prell[knr][self.prellTid], mode=self.Timer.ONE_SHOT, callback=lambda t, s=self: s.endprell(knr))

    def iknapp1(self, pin):
        knr = 5
        if self.prell[knr][self.prellOpptatt] == 0:
            self.prell[knr][self.prellOpptatt] = 1
            self.timer_k1 = self.Timer(period=self.prell[knr][self.prellTid], mode=self.Timer.ONE_SHOT, callback=lambda t, s=self: s.endprell(knr))
                     
    def endprell(self, knr):
        k = knr + 1
        self.prell[knr][self.prellOpptatt] = 0
        self.knappMatrix = [0, self.kn1.value(), self.kn2.value(), self.kn3.value(), self.kn4.value(), self.kn5.value(), self.kn6.value()]
        self.knappAktiv = True

    def bin2dec(self, b):  # Konverter et desimalt tall til en binær sekvens.
        b = "".join(str(x) for x in b)
        d = int(b, 2)
        return d
            
    def lesKnapp(self):                                # Les knapper fra tastaturet
        self.sjekkTilstand()                           # Kjør tilstandsmaskin i keyer (Den er arvet, se toppen)
        if self.knappAktiv == True:
            self.knappAktiv = False
            ord = self.bin2dec(self.knappMatrix)       # Les knappematrisen, konverter til desimal og legg til variabel ord
            if ord > 0:                                # Hvis det er et ord
                self.nyttOrd = max(self.nyttOrd, ord)  # Lagre den største verdien så langt
            else:
                self.sisteOrd = self.nyttOrd           # Når knappene er sluttet (ord = 0)
                self.nyttOrd = 0                       # Resett variabel for bruk neste gang noen trykker knappene
                
    def hentOrd(self):                                 # Hent ordet
        self.lesKnapp()                                # Les knappene
        r = self.sisteOrd                              # Les siste ord
        if self.sisteOrd > 0:                          # Hvis det er satt
            self.sisteOrd = 0                          # Resett variabel for bruk neste gang noen trykker knappene
        return r
