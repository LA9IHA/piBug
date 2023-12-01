# Artikkelserie i Amatørradio
Det er på veg inn en artikkelserie i Amatørradio om piBug av LA9IHA, Ottar. Altså meg selv.

Denne serien tar oss igjennom programmering fra det helt enkle til å kunne lage sammensatte systemer i Pyhton og Raspberry Pi Pico. Vi lagger en Elbug som blir mer og mer komplesert for hver artikkel. Når vi er ferdige har vi noe som dere kan videreutvikle til noe som blir mer funksjonsrikt enn for eksempel Logikey 5.

<img height = "200"  alt="Liten men full av pepp!" src="https://raw.githubusercontent.com/LA9IHA/piBug/main/bullen/assets/pi.jpg">

## Introduksjon
De siste årene har det vært en fantastisk utvikling innenfor mikrokontrollere og det er billig! For oss radioamatører kan vi lage styringsenhet for antennetuner, kontroll av SDR radio, repeaterlogikk og mye annet. I denne artikkelserien eksperimenterer vi med en elbug  på steroider. Ingen programmeringserfaring er nødvendig og vi lærer underveis. 

Å programmere mikrokontrollere er ikke vanskelig men annerledes enn PC programmering. Uten operativsystem må alt kodes. Det er tregere CPU, mindre RAM ulik testing mot hardwaren. Den bruker langt mindre strøm og fungerer i uker og måneder på batteri.

I dette prosjektet skal vi bruke en Raspberry Pi Pico. Det er lillesøsteren til Raspberry Pi og er 5 * 2 cm. Du programmerer prosessoren RP2040 i Python og den er din for en femtilapp. Her er det ikke noe Linux, kun blankt stål, og hvilket stål det er. La oss se kjapt på arkitekturen.

Med to kjerner, Proc0 og Proc1 kan to programmer kjøre samtidig! De deler en serie IO bus og interrupt systemet og du kan flytte av data mellom RAM banker uten å belaste CPU’en. Man kan også sette opp en rekke timere for å vekke opp funksjoner. For I/O er det puls bredde modulert output for å drive f.eks høyttalere eller steppermotorer,  seriekommunikasjon med to UART’s eller I2C til ekstern LCD display eller analog output. Du kan måle nivåer eller lese av et potmeter med en av to ADC. Som kronen på verket er det 29 generelle I/O porter som settes opp til den funksjonen man ønsker. Og ikke bare det frue, De kan også få Pico i WH versjon med innebygd internett og Bluetooth for kun noen et par tiere ekstra. Løp og kjøp!

Det er enkelt å komme i gang med massevis av dokumentasjon og aktivt miljø på internett. Strømforbruket er litt i øvre ende. Super Keyer III går i årevis på et par AA batterier mens Pico kun holder noen måneder på det samme. Hva du lærer her er også anvendelig for andre prosessorer.

## Bygging

For å ha glede av denne bør man nok være medlem av NRRL for å få tilgang til medlemsbladet der materialet er. I tillegg må man anskaffe noen saker til hardwaren:

- Raspberry Pi Pico med en USB ledning
- En liten høytaler og en 10 uF elektrolytt for å kunne høre hva som kjøres
- En paddle eller paddle alternativ, f.eks to små brytere som er koplet opp som hhv Paddle 1 og Paddle 2.
- To, helst seks brytere for å kunne kontrollere saken når vi er kommet litt ut i prosjektet
- En motstand, 330 Ohm
- En liten LED
- Noen korte ledningsbiter for å kople dette i sammen
- Et prototypekort å montere det på

Mitt lille eksperiment ser ut omtrent som dette:

<img width = "500" alt="Mitt piBug ekperiment" src="https://raw.githubusercontent.com/LA9IHA/piBug/main/bullen/assets/piBug.jpg">

For å forstå denne lille saken er det også lurt å ta en titt på pinout diagrammet for modulen. Den finner dere på <a href= "https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf">PINOUT DIAGRAM</a> linken.

Det står en del linker i artikkelen også. Få gjerne med dere dm og hvis du ikke har programmert noe særlig så går det nok litt heftig fort i artiklene. Kjøp eller lån boken jeg nevnte i artikkelen og slå opp i den og les når du lurer på noe. Det gjør læringen mye kjappere.

Det er selvsagt mye kjekt på nettet også som kan være greit å lese men bruk tiden nøye. Det er fort gjort å kaste bort virkelig tid på ting som er dårlige eller direkte feil.

Så til artiklene. Her er linkene ned til dem:

* Artikkel 1: <a href="https://github.com/LA9IHA/piBug/tree/main/bullen/art1">ARTIKKEL 1</a> Januar 2024

Jeg hekter på nye artikler etter hvert som de blir publisert. God lesning og jeg håper dere kommer til å sette pris på dette.



73 es gd luck de LA9IHA Ottar