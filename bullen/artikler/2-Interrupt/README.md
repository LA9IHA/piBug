# Hjemmebygg med mikrokontroller, piBug, nummer 2, April 2024.

Nå er den andre artikkelen omsider klar. Jeg håper dere fant den interessant. Her var det om interrupter og det er en veldig annerledes måte å lage programmer. Man lar rett og slett prosessoren bryte inn når interruptet oppstår og kjøre koden som er knyttet til interruptet, deretter lar prosessoren programmet kjøre videre der det ble avbrutt.

Når dere lager interrupter er det viktig å gjøre seg ferdig med interruptrutinen så kjept som mulig slik at det vanlige programmet kan kjøres på vanlig måte. En vanlig teknikk er å lage en tilstandsmaskin. Det betyr at vi har en variabel som kan tilordnes en verdi i interruptrutinen. Når progrmmet kjører i vanlig modus sjekker det tilstandsmaskinen hyppig og hvis den ikke er i hvilemodus så utfører den oppgaven som tilstandsmaskinen beordrer og setter verdien tilbake til hvilemodus. Ett problem som kan oppstå er at en interrupt ikke er ferdig løst før en annen trør til. Derfor lar vi i vår oppgave tilstandsmaskinen være en liste av verdier og vi sletter dem etter hvert som de er utført.

Vi forholder oss til to hovedtyper av interrupter:

- **Input-interrupter**: Vi definerer en input pinne som kilde til interrupt. Når denne går til definert nivå skal prosessoren utløse et interrupt.
- **Timer interrupt**: Dette er en intern timer i prosessoren. Den kan settes opp til telle ned en gang og fyre av et interrupt eller at den oscillerer med å starte en ny nedtelling etter at den forrige er ferdig.

Vær forberedt på at en del feil i interruptdrevne programmer kan være vanskelige å finne. Derfor er programstruktur og oversikt svært viktig. Gjør gjerne tester i koden som hindrer progrmmet å gå videre eller rapporterer feil hvis forutsetningen for funksjonen ikke er til stede. Det kan være en indikasjon på at du har havnet i en feiltilstnd du ikke trodde ville skjedd. Tro meg, du vil bli overrasket over hvor mye rart som kan skje i software :)

## Tilkopling til rig
Vi har fokusert mye på kode men her er litt hardware for den som vil bruke Pibug på lufta. KG5U har et forslag for hvordan nøkle PTT for Super Keyer III og man kan nok bruke tilsvarende krets til å nøkle keyer i dette eksperimentet. Jeg må nevne at jeg ikke har testet det så hvis noen har erfaringer, del gjerne.

<img height="200" src="https://raw.githubusercontent.com/LA9IHA/piBug/main/bullen/assets/sk3.jpg">

## Batteridrift
Hvis det er slik at dere er klare for å gå på lufta med PiBug så er det jo triveligere hvis dere slipper å kople USB kabelen til en PC for å få strøm. Hva med batterier. Koplingen er som vist i tegningen under. Kopler du feil veg så ryker port 39 på kretsen. Nærmeste jord til Vcc er nabopinnen, 38.

<img height="200" src="https://raw.githubusercontent.com/LA9IHA/piBug/main/bullen/assets/pico_batt.jpg">

# Potmeter
Flere vil nok ønske å kunne regulere sendehastigheten med et potmeter. Det går fint. Picoen har innebygd to ADC - Analog til Digitalomsettere. Man kopler da et potmeter med endepunktene til Vcc og jord. Glideren koples til ADC inngngen og resten er programvare. Dere kan gjerne utvide eksperimentet med å lese potmeteret f.eks etter hvert tegn for å sette prikklengden. Samme trikset kan dere bruke for å endre medhørstonen.

Denne oppgaven er ganske enkel så med mindre jeg blir spurt så tror jeg neppe jeg legger den inn i PiuBug nå men tar gjerne imot bidrag fra dere.

Her er et par linker om hvordan man kan programmere potmeter input. Bruk det til inspirasjon!

* https://peppe8o.com/potentiometer-raspberry-pi-pico-micropython/
* https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/potentiometer-and-pwm-led

## Kode
Det kommer også kode etter hvert.

* 

## Linker:
- **Dokumentasjonssidene**: <https://www.raspberrypi.com/documentation/microcontrollers/?version=E0C9125B0D9B >
- **Litt mer om interrupter og hvordan de virker**: <https://electrocredible.com/raspberry-pi-pico-external-interrupts-button-micropython/ >
- 

## Tilbake til samleside
* <a href="https://github.com/LA9IHA/piBug/blob/main/bullen/">Om artikkelen</a>
