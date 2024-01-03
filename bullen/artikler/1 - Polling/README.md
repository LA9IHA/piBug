# Hjemmebygg med mikrokontroller, piBug, nummer 1, Februar 2024.

Da er første artikkel klar. Det er sikkert en del som ikke har drevet med programmering før så jeg har gått forsiktig frem, og i små steg. Håper dere alle har hengt fint med. Litt lengre nede er den en link til å hente ned ferdig skrevet kode som fungerer hos meg.

Hvis du er helt ny innen programmering så da er det lurt å låne eller kjøpe boken. Den norske kjenner jeg ikke så godt men den ser veldig bra ut. Det er også en engelsk bok som er anerkjent og den har jeg brukt litt selv.

Du kommer sikkert til å trenge litt tid til å få i gang miljøet med Thonny og Pico. Det er ikke så vanskelig men slike ting kommer typisk i orden etter fjerde eller åttende forsøk. Les dokumentasjonen på Raspberry Pi sidene.

## Hva med litt sosialt samvær?

Ingenting er så hyggelig som å ha et prosjekt i gruppen eller blant noen interesserte radioamatører. Det er en veldig god ide. Dere lærer ikke like fort hele tiden. Noen lærer først og hjelper de som er litt bakpå. Dermed blir alle med og får det til. Dessuten, den beste måten å lære på er å prøve, feile, prøve igjen, forstå og deretter LÆRE DET BORT! Da sitter det sveist i skallen.

Bruk gjerne dette prosjektet som en sak å gjøre i noen byggekvelder. Hører gjerne fra dere hvordan det går :)

## Pin-up

En sak som jeg ikke var så tydelig på var Pin nummer og pinne nummer på modulen. Det er jo litt forvirrende at Paddle på 3 og 4 går til pinne 5 og 6? Det skyldes simpelthen at Pin er knyttet opp mot IO portene på enheten som IKKE er de samme som pinnene på modulen. Hvis dere ser på pinnene for GP0 til GP28 ser dere at de ikke er ført ut til samme pin nummer som GP nummer. Dere ser det i tegningen under. Her ser dere at samme pin kan ha flere typer data på IO. Alt dette kan programmeres. Oh, la la la så mye moro vi kan ha med en sånn liten ting.

<img src="https://raw.githubusercontent.com/LA9IHA/piBug/main/bullen/assets/pinout.jpeg">


## Kode
Her er koden for programmet vi lagte i artikkelen. Det er bare å laste ned og kikke. Kjør den gjerne også. Eksperimenter med den. Ødelegger du det så last ned på nytt og prøv igjen. God fornøyelse!

* <a href="https://github.com/LA9IHA/piBug/blob/main/bullen/artikler/1%20-%20Polling/main.py">main.py</a>

## Om sendehastighet
I Norge har vi brukt sendehastighet i bokstaver per minutt mens man i UK og USA bruker ord per minutt. De ulike morsesignalene har ulik lengde så man trenger et standard ord å måle mot. Det ordet er PARIS. Når man analyserer det ordet finner man at lengden tilsvarer 50 prikker.

For vår Pico er delayet oppgitt i millisekund. En prikk skal da vare i 100 ms og oppholdet deretter er nye 100 ms. Streken skal være tre ganger så lang og opphold mellom ord, like lenge. Ordet Paris blir da 50 * 100 ms = 50000 ms = 5 sekund.

Vi erindrer også at et minutt er 60 sekund og når hvert ord behøver 5 sekund er sendehastigheten 60 / 5 = 12 ord per minutt.

Man har altså med 100 ms prikklengde, 12 ord i minuttet og multipliserer man det med antall bokstaver i ordet får man 12 * 5 = 60. Det er altså lik det gamle kravet fra telegrafieksamen for radioamatører.

## Linker:
- **Leverandører**: Det er mulig Christech leverer. Hvis ikke har jeg hatt hell med <https://thepihut.com/products/raspberry-pi-pico>
- **Dokumentasjonssidene**: <https://www.raspberrypi.com/documentation/microcontrollers/?version=E0C9125B0D9B >
- **Bok om Python**: <a href="https://www.akademika.no/skoleboker/barne-og-ungdomsboker-motvillige-lesere/programmering-i-python/9788269333008" target="_blank">Programmering i Python algoritmer og kode</a>. Skrindo, Knut Weider og Øystein Johannes. Flott norsk bok som du kan kjøpe hos Haugenbok.no eller låne på biblioteket. 
- **Engelsk bok om Python**: <a href="https://www.amazon.co.uk/Python-Crash-Course-3Rd-Matthes/dp/1718502702/" target="_blank">Python Crash Course, 3Rd Edition: A Hands-On, Project-Based Introduction to Programming</a>. Eric Matthes. Anerkjent engelsk bok som du ikke kjøper på Akademika men på Amazon til en mer edruelig pris.
- **Thonny**, programmeringsmiljøet: <https://thonny.org>



## Tilbake til samleside
* <a href="https://github.com/LA9IHA/piBug/blob/main/bullen/">Om artikkelen</a>
