# Hjemmebygg med mikrokontroller, piBug, nummer 2, April 2024.

Nå er den andre artikkelen omsider klar. Jeg håper dere fant den interessant. Her var det om interrupter og det er en veldig annerledes måte å lage programmer. Man lar rett og slett prosessoren bryte inn når interruptet oppstår og kjøre koden som er knyttet til interruptet, deretter lar prosessoren programmet kjøre videre der det ble avbrutt.

Når dere lager interrupter er det viktig å gjøre seg ferdig med interruptrutinen så kjapt som mulig slik at det vanlige programmet kan kjøres mest mulig og man unngår at et nytt intterupt krasjer i en pågående interrupthåndtering. En mye brukt teknikk er å lage en tilstandsmaskin. Det betyr at vi har en variabel som kan tilordnes en verdi i interruptrutinen. Når programmet kjøres normalt uten pågående interrupthåndtering sjekker det tilstandsmaskinen hyppig. Er det dukket opp en ny tilstand fra en interruptrutine utføres den oppgaven som tilstandsmaskinen beordrer og deretter setter verdien tilbake til hvilemodus og programmet løper normalt. For å håndtere at en interrupt ikke er ferdig løst før en annen trør til lar vi i vår oppgave tilstandsmaskinen være en liste av verdier og vi sletter dem etter hvert som de utføres. Diagrammet under er et forsøk på å illustrere dette.

<img height="200" src="https://raw.githubusercontent.com/LA9IHA/piBug/main/bullen/assets/interrupts.png">

Vi forholder oss til to hovedtyper av interrupter:

- **Input-interrupter**: Vi definerer en input pinne som kilde til interrupt. Når denne går til definert nivå skal prosessoren utløse et interrupt.
- **Timer interrupt**: Dette er en intern timer i prosessoren. Den kan settes opp til telle ned en gang og fyre av et interrupt eller at den oscillerer med å starte en ny nedtelling etter at den forrige er ferdig.

Vær forberedt på at en del feil i interruptdrevne programmer kan være vanskelige å finne. Derfor er programstruktur og oversikt svært viktig. Gjør gjerne tester i koden som hindrer programmet å gå videre eller rapporterer feil hvis forutsetningen for funksjonen ikke er til stede. Det kan være en indikasjon på at du har havnet i en feiltilstand du ikke trodde ville skjedd. Tro meg, du vil bli overrasket over hvor mye rart som kan skje i software :)

## Design av timing
Her er et tips når du skal lage et program med interrupt rutiner. Tegn et timing program. Det hjelper deg å tenke igjennom hvordan du håndterer situasjonen med flere interrupter oppå hverandre. Vi har laget et system med flagg for å si at piBug er oppttt, alle nye paddeltrykk blir ignorert. Timingdiagrammet hjelper oss til å håndtere timere som stopper signalet eller holder gap mellom ord og bokstaver.

Under her er et eksempel på et slikt. Jeg lagte dette for å illustrere sånn circa hva jeg ville oppnå før jeg begynte å programmere. Det gjør at man forstår oppgaven ordentlig.

Hvis du skal lage et kritisk program med høy kvalitet bør du lage timingdiagrammet ordentlig og helt ferdig med alle de ulike konstellasjonene av tilstandsmaskiner, flagg, timere og andre interrupter du kan komme på. En times innsats i et timingprogram kan spare dager i feilsøking. Dessuten blir koden også lettere å lese!

<img height="500" src="https://raw.githubusercontent.com/LA9IHA/piBug/main/bullen/assets/timing.jpg">


## Tilkopling til rig
Vi har fokusert mye på kode men her er litt hardware for den som vil bruke piBug på lufta. KG5U har et forslag for hvordan nøkle PTT for Super Keyer III og man kan nok bruke tilsvarende krets til å nøkle keyer i dette eksperimentet. I stedet for tilkopling til Super keyer kopler du den til port 21, nøkkel. Jeg må nevne at jeg ikke har testet det så hvis noen har erfaringer, del gjerne.

<img height="200" src="https://raw.githubusercontent.com/LA9IHA/piBug/main/bullen/assets/sk3.jpg">

## Batteridrift
Hvis det er slik at dere er klare for å gå på lufta med piBug så er det jo triveligere hvis dere slipper å kople USB kabelen til en PC for å få strøm. Hva med batterier. Koplingen er som vist i tegningen under. Nærmeste jord til Vcc er nabopinnen, 38.

<img height="300" src="https://raw.githubusercontent.com/LA9IHA/piBug/main/bullen/assets/pico_batt.jpg">

Kopler du feil veg så ryker port 39 på kretsen. Det er vel en ide å putte inn litt beskyttelse. Jeg rasket sammen en skisse som vist under. Sett en diode i sperreretning i serie med en liten motstand for å begrense strømmen. Med 3V bør det være nok med 12 Ohm for å bryte en liten sikring. Det bør være nok til at kretsen ikke stekes. Resultater fra eksperimenter mottas med takk.

<img height="200" src="https://raw.githubusercontent.com/LA9IHA/piBug/main/bullen/assets/batteri.jpg">

## Potensiometer
Flere vil nok ønske å kunne regulere sendehastigheten med et potmeter. Det går fint. Picoen har innebygd to ADC - Analog til Digitalomsettere. Man kopler da et potmeter med endepunktene til Vcc og jord. Glideren koples til ADC inngangen og resten er programvare. Dere kan gjerne utvide eksperimentet med å lese potmeteret f.eks etter hvert tegn for å sette prikklengden. Samme trikset kan dere bruke for å endre medhørstonen.

Denne oppgaven er ganske enkel så med mindre jeg blir spurt så tror jeg neppe jeg legger den inn i PiuBug nå men tar gjerne imot bidrag fra dere.

Her er et par linker om hvordan man kan programmere potmeter input. Bruk det til inspirasjon og send meg noen ord hvis du har gjordt det så kan vi dele beskrivelsen din her!

* https://peppe8o.com/potentiometer-raspberry-pi-pico-micropython/
* https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/potentiometer-and-pwm-led

## Kode
Her er koden for programmet. Det ligger mange kommentarer i koden så du kan lese deg igjennom. Håper det ikke blir forvirrende. Last den gjerne ned og test ut selv. Hvis det går i stykker laster du på nytt. Prøv og utfordre den og lag egne løsninger. Hvis du finner feil i koden vil jeg gjerne høre om det og da vanker det hederlig omtale!

God fornøyelse!

* <a href="https://github.com/LA9IHA/piBug/blob/main/bullen/artikler/2-Interrupt/main.py">main.py</a>


## Linker:
- **Dokumentasjonssidene**: <https://www.raspberrypi.com/documentation/microcontrollers/?version=E0C9125B0D9B >
- **Litt mer om interrupter og hvordan de virker**: <https://electrocredible.com/raspberry-pi-pico-external-interrupts-button-micropython/ >

## Tilbake til samleside
* <a href="https://github.com/LA9IHA/piBug/blob/main/bullen/">Om artikkelen</a>
