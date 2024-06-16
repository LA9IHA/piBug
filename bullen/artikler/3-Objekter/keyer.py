import time
from machine import Timer
class Keyer:
    from machine import Pin, PWM, Timer
    
    def __init__(self):
        from morsekode import MorseKode
        self.morse = MorseKode()

        # IO-ports
        self.paddle1 = 3
        self.paddle2 = 2
        self.speaker = 5
        self.out1 = 16
        self.prellhold = 20
        self.prellTid = 0
        self.prellOpptatt = 1
        self.prellSistOutput = 2
        self.prell = [[0, 0, 0], [self.prellhold, 0, 0], [self.prellhold, 0, 0]]
        
        # Global user parameters
        self.t_pace = 100
        self.maxFart = self.prellhold + 2
        self.minFart = 300
        self.fartSteg = 5
        self.toneUt = 440
        self.keivhendt = 0
        self.gapBokstav = 2
        self.gapOrd = 4
        
        # Internal house keeping
        self.TILSTANDSMASKIN = []
        self.lockedSig = False
        self.dult = 9
        
        # States for keyer state machine
        self.sVENT = 0
        self.sPADDLE1 = 1
        self.sPADDLE2 = 2
        self.sSTOPP_TX = 3
        self.sKLAR_TX = 4
        self.sSQUEEZE = 5
        self.sTXTSEP = 6
        
        # Sett opp interrupter
        self.spkr = self.PWM(self.Pin(self.speaker))

        self.sw1 = self.Pin(self.paddle1, self.Pin.IN, self.Pin.PULL_DOWN)
        self.sw1.irq(self.key1, self.Pin.IRQ_RISING)
        
        self.sw2 = self.Pin(self.paddle2, self.Pin.IN, self.Pin.PULL_DOWN)
        self.sw2.irq(self.key2, self.Pin.IRQ_RISING)
        
        self.k1 = self.Pin(self.out1, self.Pin.OUT)
        self.k1.value(0)
        
        # Variable for å sende bokstaver
        self.bokstSending = False # Sann ved automatisk bokstavsending
        self.txBokst = [] # Message from paddles
        self.txBokst = ''
        self.pdlWrd = 1  # Current word on paddles
        self.wordHold = 0 # Observing gap between words: 1


    #IO translators
    def key1(self, pin):
        if self.prell[1][self.prellOpptatt] == 0:
            self.prell[1][self.prellOpptatt] = 1
            self.timer_k2 = self.Timer(period=self.prell[1][self.prellTid], mode=self.Timer.ONE_SHOT, callback=lambda t, s=self: s.endprell(1))
            if self.prell[1][self.prellSistOutput] == 0:
                self.prell[1][self.prellSistOutput] = 1
                if self.lockedSig == True: self.dult = 0
                self.TILSTANDSMASKIN.append(self.sPADDLE1)
                     
    def key2(self, pin):
        if self.prell[2][self.prellOpptatt] == 0:
            self.prell[2][self.prellOpptatt] = 1
            self.timer_k1 = self.Timer(period=self.prell[2][self.prellTid], mode=self.Timer.ONE_SHOT, callback=lambda t, s=self: s.endprell(2))
            if self.prell[2][self.prellSistOutput] == 0:
                self.prell[2][self.prellSistOutput] = 1
                if self.lockedSig == True: self.dult = 1
                self.TILSTANDSMASKIN.append(self.sPADDLE2)

    def endprell(self, pnr):
        self.prell[pnr][self.prellOpptatt] = 0
        
    def paddleSignal(self, p):
        return (self.keivhendt ^ p)
    
    # Paddle logikk
    def goPaddle(self, p):
        self.txBokst = ''
        self.txBokst = []
        self.bokstSending = False
        self.startSig(self.paddleSignal(p))
        
    def paddleSignal(self, paddle):
        return (self.keivhendt ^ paddle)
    
    def squeezeKey(self):        
        self.paddles = self.sw1.value() + self.sw2.value()
        if self.dult < 9:
            self.goPaddle(self.dult)
        elif self.paddles > 1:
            self.startSig(self.lastSig ^ 1)
        elif self.paddles > 0:
            if self.sw1.value() == 1:
                self.prell[2][self.prellSistOutput] = 0
                self.goPaddle(0)
            elif self.sw2.value() == 1:
                self.prell[1][self.prellSistOutput] = 0
                self.goPaddle(1)
        else:
            self.prell[1][self.prellSistOutput] = 0
            self.prell[2][self.prellSistOutput] = 0
        self.dult = 9
        
    def monitor(self, v):
        if v == 1:
            self.spkr.freq(self.toneUt)
            self.spkr.duty_u16(32768)
        elif v==0:
            self.spkr.duty_u16(0)
            
    def stoppTx (self, timer):
        self.monitor(0)
        self.k1.value(0)
        self.t_pause_bokst = self.Timer(period=(1*self.t_pace), mode=self.Timer.ONE_SHOT, callback=self.klarTx)
        
    def klarTx (self, timer):        
        self.lockedSig = False
        if self.bokstSending:
            self.sendBokstav()
        else:
            self.TILSTANDSMASKIN.append(self.sSQUEEZE)
            
    def startSig (self, s):
        if not self.lockedSig:
            self.lockedSig = True
            self.lastSig = s
            self.monitor(1)
            self.k1.value(1)
            if s == 0:
                self.t_kort = self.Timer(period=(1*self.t_pace), mode=self.Timer.ONE_SHOT, callback=self.stoppTx)
            elif s == 1:
                self.t_lang = self.Timer(period=(3*self.t_pace), mode=self.Timer.ONE_SHOT, callback=self.stoppTx)
   
    def sjekkTilstand(self):
        if len(self.TILSTANDSMASKIN) > 0:
            tilstand = self.TILSTANDSMASKIN [0]
            del(self.TILSTANDSMASKIN [0])
            
            if tilstand == self.sPADDLE1: self.goPaddle(0)
            elif tilstand == self.sPADDLE2: self.goPaddle(1)
            elif tilstand == self.sSTOPP_TX: self.stoppTx()
            elif tilstand == self.sKLAR_TX: self.klarTx()
            elif tilstand == self.sSQUEEZE: self.squeezeKey()
            elif tilstand == self.sTXTSEP: self.sendStreng()
            tilstand = self.sVENT

    # #################################################################
    # Sende bokstaver
    #
    def putStreng(self, s):
        self.txMsg = list(s)
        self.bokstSending = True
        self.sendStreng()

    def sendStreng(self):
        if len(self.txMsg) > 0:
            self.txBokst = self.morse.hentTallFraBokstav(self.txMsg[0])
            del(self.txMsg[0])
            self.sendBokstav()
        else:
            self.bokstSending = False

    def sendBokstav(self):
        if self.txBokst == 0: self.holdOrd()
        elif self.txBokst == 1: self.holdBokst()
        elif self.txBokst > 1:
            self.startSig(self.txBokst & 1)
            self.txBokst = self.txBokst >> 1

    def holdBokst(self):
        self.t_pause_ord = self.Timer(period=self.gapBokstav * self.t_pace, mode=self.Timer.ONE_SHOT, callback=self.tekstSkille)
        self.lockedSig = True
        
    def tekstSkille(self, timer):
        self.lockedSig = False
        self.TILSTANDSMASKIN.append(self.sTXTSEP)
        #self.sendStreng()
        
    def holdOrd(self):
        self.t_pause_ord = self.Timer(period=self.gapOrd * self.t_pace, mode=self.Timer.ONE_SHOT, callback=self.tekstSkille)
        self.lockedSig = True