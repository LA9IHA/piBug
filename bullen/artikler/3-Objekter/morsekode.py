## PiBug - morsekode
#
# (C) Copyright 2024 Ottar Kvindesland - LA9IHA
#
# Licence: GPL v.2.0. See https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# 
# Dette er en del av Artikkel 3 i Amatørradio Juni 2024 utgitt av Norsk Radio Relæ Liga.
# Denne klassen håndterer morsealfabetet
# 

class MorseKode:
    
    def __init__(self):
        self.morsekode = []
        
        self.morsekode.append(['A',6])
        self.morsekode.append(['B',17])
        self.morsekode.append(['C',21])
        self.morsekode.append(['D',9])
        self.morsekode.append(['E',2])
        self.morsekode.append(['F',20])
        self.morsekode.append(['G',11])
        self.morsekode.append(['H',16])
        self.morsekode.append(['I',4])
        self.morsekode.append(['J',30])
        self.morsekode.append(['K',13])
        self.morsekode.append(['L',18])
        self.morsekode.append(['M',7])
        self.morsekode.append(['N',5])
        self.morsekode.append(['O',15])
        self.morsekode.append(['P',22])
        self.morsekode.append(['Q',27])
        self.morsekode.append(['R',10])
        self.morsekode.append(['S',8])
        self.morsekode.append(['T',3])
        self.morsekode.append(['U',12])
        self.morsekode.append(['V',24])
        self.morsekode.append(['W',14])
        self.morsekode.append(['X',25])
        self.morsekode.append(['Y',29])
        self.morsekode.append(['Z',19])
        self.morsekode.append(['Æ',26])
        self.morsekode.append(['Ø',23])
        self.morsekode.append(['Å',54])
        self.morsekode.append(['1',62])
        self.morsekode.append(['2',60])
        self.morsekode.append(['3',56])
        self.morsekode.append(['4',48])
        self.morsekode.append(['5',32])
        self.morsekode.append(['6',33])
        self.morsekode.append(['7',35])
        self.morsekode.append(['8',39])
        self.morsekode.append(['9',47])
        self.morsekode.append(['0',63])
        self.morsekode.append(['.',106])
        self.morsekode.append([',',115])
        self.morsekode.append(['?',76])
        self.morsekode.append(['-',97])
        self.morsekode.append(['=',49])
        self.morsekode.append(['/',41])
        self.morsekode.append([':',71])
        self.morsekode.append(['+',42])
        self.morsekode.append(['(',109])
        self.morsekode.append(['@',86])
        self.morsekode.append(['\'',46]) # Aprostrophe
        self.morsekode.append(['*',104]) # End of work
        self.morsekode.append(['§',128]) # Error, correction follows - SPECIAL CODE
        self.morsekode.append(['&',50])  # Separator groups of numbers and letters
        self.morsekode.append(['>',53])  # Starting signal
        self.morsekode.append(['^',40])  # Understood
        self.morsekode.append(['%',34])  # Wait
        self.morsekode.append([' ', 0])  # Word space - SPECIAL CODE

    def hentTallFraBokstav(self, l):
        funnet = False
        for bokstav in self.morsekode:
            if bokstav[0] == l.upper():
                funnet = True
                return bokstav[1]
        if funnet == False:
            return(1)
            
    def hentBokstavFraTall(self, n):
        funnet = False
        for tall in self.morsekode:
            if tall[1] == n:
                funnet = True
                return tall[0]
        if funnet == False:
            return(' ')
