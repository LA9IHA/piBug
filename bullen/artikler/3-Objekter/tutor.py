## PiBug - tutor
#
# (C) Copyright 2023 Ottar Kvindesland - LA9IHA
#
# Licence: GPL v.2.0. See https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
#
from funksjon import Funksjoner
import random

class Tutor(Funksjoner):
    
    def __init__(self):
        super().__init__()
        
        self.treningsgrupper = 25
        
        self.pGrupper = [[], # Tom gruppe for index 0 fordi vi har ingen knapp som gir 0
                         ['A', 'E', 'G', 'J', 'V'],
                         ['C', 'F', 'O', 'S', 'Å'],
                         ['H', 'L', 'Q', 'T', 'W'],
                         ['B', 'K', 'P', 'Y', 'Æ'],
                         ['D', 'N', 'R', 'X', 'Ø'],
                         ['I', 'M', 'U', '-', '.'],
                         ['1', '5', '7', ',', '?'],
                         ['0', '2', '4', '/', '='],
                         ['6', '9', ':', '(', '+'],
                         ['3', '8']]
        
        self.t_pace = 80
        self.gapBokstav = 10
        self.gapOrd = 15
        
    def sendProgramGruppe(self, p):
        found = False
        n = 5
        r = ''
        funn = False
        pl = len(self.pGrupper[p])-1
        while n > 0:
            i = random.randint(0, pl)
            r += str(self.pGrupper[p][i])
            n = n - 1
        r += ' '       
        return r
    
    def sendProgram(self, p):
        kodestring = '> '
        for n in range (0, self.treningsgrupper):
            kodestring += self.sendProgramGruppe(p)
        kodestring += '*'
        print ("KODE ", kodestring)
        self.putStreng(kodestring)
    
    def kommandoloop(self):
        o = self.hentOrd()
        g = 0
        rev = ''
        if o > 0:
            b = bin(o)[2:]
            if b.count('1') == 1:
                bstr = str(b)
                for c in bstr:
                    rev = c + rev
                g = rev.find('1') + 1
                if not self.bokstSending:
                    self.sendProgram(g)
            else:
                self.putStreng("FEIL")

t = Tutor()
while True:
    t.kommandoloop()

        
