from funksjon import Funksjoner

b = Funksjoner()
while True:
    o = b.hentOrd()
    if o > 0:
        if o == 1: b.putStreng("CQ CQ CQ de LA9IHA LA9IHA LA9IHA pse k")
        elif o == 2 : b.putStreng("TNX FER CALL - UR RST RST RST es 599 599 5nn es name name es O t t a r  o t t a r   o t t a r - hw cpy?")
        elif o == 3 : b.putStreng("vy happy xmas")
        else:
            b.putStreng("? " + str(o))
            
