# piBug, en odysse
Da er første artikkel om piBug kommet inn i Amatørradio. Jeg håper du fikk prøvd med litt kode.

Denne serien tar oss igjennom programmering fra det helt enkle til å kunne lage sammensatte systemer i Python og Raspberry Pi Pico. Vi lagger en Elbug som blir mer og mer komplisert for hver artikkel. Når vi er ferdige har vi noe som dere kan videreutvikle til noe som blir mer funksjonsrikt enn for eksempel Logikey model 5:

<img height = "250" alt="En veldig bra elbug keyer" src="https://raw.githubusercontent.com/LA9IHA/piBug/main/bullen/assets/logkey.jpg">

## Men morse da, hører ikke det hjemme på museum?
Det er akkurat dette som er så fint med amatørradio. Vi fakturerer ikke timer og derfor gjør vi det vi vil. Morsetelegrafi er en kommunikasjon som krever litt men det funker. Når du får det til får du noe som heter mestringsfølelse. Det kan vi aldri få nok av.

Det jo også mange som ikke bryr seg om å spille piano eller andre instrumenter. De hører heller på Spotify. Hvem tror du er lykkeligst, de som spiller musikken eller de som spiller den av på nettet. Den samme sammenligningen er de som fyrer av en SMS eller tar seg bryet om å kunne faktisk kommunisere med helt basale verktøy.

Jeg må få si noen ord om nøkler også, de som kommer med to paddles. Jeg greier ikke å holde meg men tar frem <a href = "https://github.com/LA9IHA/piBug/blob/main/bullen/artikler/paddlekeys.md">litt paddle fetisj her</a>. Og forresten, her har du <a href="https://morsecode.world/international/morse2.html">hele morsealfabetet</a>.

## Introduksjon
De siste årene har det vært en fantastisk utvikling innenfor mikrokontrollere og det er billig! For oss radioamatører kan vi lage styringsenhet for antennetuner, kontroll av SDR radio, repeaterlogikk og mye annet. I denne artikkelserien eksperimenterer vi med en elbug  på steroider. Ingen programmeringserfaring er nødvendig og vi lærer underveis. 

<img height = "200"  alt="Liten men full av pepp!" src="https://raw.githubusercontent.com/LA9IHA/piBug/main/bullen/assets/pi.jpg">

Å programmere mikrokontrollere er ikke vanskelig men annerledes enn PC programmering. Uten operativsystem må alt kodes. Det er tregere CPU, mindre RAM ulik testing mot hardwaren. Den bruker langt mindre strøm og fungerer i uker og måneder på batteri.

I dette prosjektet skal vi bruke en Raspberry Pi Pico. Det er lillesøsteren til Raspberry Pi og er 5 * 2 cm. Du programmerer prosessoren RP2040 i Python og den er din for en femtilapp. Her er det ikke noe Linux, kun blankt stål, og hvilket stål det er. La oss se kjapt på arkitekturen.

Med to kjerner, Proc0 og Proc1 kan to programmer kjøre samtidig! De deler en serie IO bus og interrupt systemet og du kan flytte av data mellom RAM banker uten å belaste CPU’en. Man kan også sette opp en rekke timere for å vekke opp funksjoner. For I/O er det puls bredde modulert output for å drive f.eks høyttalere eller steppermotorer,  seriekommunikasjon med to UART’s eller I2C til ekstern LCD display eller analog output. Du kan måle nivåer eller lese av et potmeter med en av to ADC. Som kronen på verket er det 29 generelle I/O porter som settes opp til den funksjonen man ønsker. Og ikke bare det frue, De kan også få Pico i WH versjon med innebygd internett og Bluetooth for kun noen et par tiere ekstra. Løp og kjøp!

Det er enkelt å komme i gang med massevis av dokumentasjon og aktivt miljø på internett. Strømforbruket er litt i øvre ende. Super Keyer III går i årevis på et par AA batterier mens Pico kun holder noen måneder på det samme. Hva du lærer her er også anvendelig for andre prosessorer.

## Bygging

For å ha glede av denne bør man nok være medlem av NRRL for å få tilgang til medlemsbladet der materialet er. I tillegg må man anskaffe noen saker til hardwaren:

- Raspberry Pi Pico med en USB ledning
- En liten høyttaler og en 10 uF elektrolytt for å kunne høre hva som kjøres
- En paddle eller paddle alternativ, f.eks to små brytere som er koplet opp som hhv Paddle 1 og Paddle 2.
- To, helst seks brytere for å kunne kontrollere saken når vi er kommet litt ut i prosjektet
- En motstand, 330 Ohm
- En liten LED
- Noen korte ledningsbiter for å kople dette i sammen
- Et prototypekort å montere det på

Mitt lille eksperiment ser ut omtrent som dette:

<img width = "500" alt="Mitt piBug ekperiment" src="https://raw.githubusercontent.com/LA9IHA/piBug/main/bullen/assets/piBug.jpg">

For å forstå denne lille saken er det også lurt å ta en titt på pinout diagrammet for modulen. Den finner dere på <a href= "https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf">PINOUT DIAGRAM</a> linken.

Det står en del linker i artikkelen også. Få gjerne med dere dem og hvis du ikke har programmert noe særlig så går det nok litt heftig fort i artiklene. Kjøp eller lån boken jeg nevnte i artikkelen og slå opp i den og les når du lurer på noe. Det gjør læringen mye kjappere.

Det er selvsagt mye kjekt på nettet også som kan være greit å lese men bruk tiden nøye. Det er fort gjort å kaste bort virkelig tid på ting som er dårlige eller direkte feil.

## Litt fakta om Raspberry Pi Pico
- Dette er en mikroprosessor med alle støtte som strømforsyning, minne, disk, I/O enten innebygd eller som tilleggskomponenter på kortet
- Den får strøm enten fra USB, batterier eller strømforsyning
- Den har ikke operativsystem men du kan legge ned et miljø for Python som gjør noe husholdningsarbeid for deg
- Eksempelet vi skal jobbe oss igjennom er en avansert el-bug for radioamatører
- Hvis du arbeider deg igjennom denne artikkelserien så lærer du å lage mer komplekse systemer enn de enkle hacks fra internett. Kunnskapen kan brukes for andre prosessorfamilier.

## Artikkelserien
Så til artiklene. Her er linkene ned til dem:

* <a href="https://github.com/LA9IHA/piBug/tree/main/bullen/artikler/1-Polling">ARTIKKEL 1, Polling</a> Februar 2024. Beskriver Raspberry Pi Pico og viser hvordan vi kan programmere en fungerende elbug på enkleste måte. Vi leser paddles og sender prikk eller strek og repeterer, det er alt.
* <a href="https://github.com/LA9IHA/piBug/tree/main/bullen/artikler/2-Interrupt">ARTIKKEL 2, Interrupt</a> April 2024. Legger ut en alternativ måte der vi lar paddles eller timere lage interrupt og håndterer dem når de inntreffer. For øvrig har vi fått ledig tid til andre ting.
* <a href="https://github.com/LA9IHA/piBug/tree/main/bullen/artikler/3-Objekter">ARTIKKEL 3, Objekter</a> Juni 2024. Viser hvordan vi kan strukturere kode i objekter. Da kan vi la et objekt ta seg av paddles, et annet kan sende bokstaver. Det gjør oss i stand til å lage mer kompleks kode med mange funksjoner uten å miste oversikten
* <a href="https://github.com/LA9IHA/piBug/tree/main/bullen/artikler/4-System">ARTIKKEL 4, System og ekstern kode</a> August 2024. Tar oss igjennom hvordan vi kan bruke andres kode i våre prosjekter. Dessuten kan vi bruke samme kodebase til flere applikasjoner.

Hvis du ikke har artiklene så stikk innom <a href="https://www.nrrl.no" target="_blank">Norsk Radio Relæ Liga</a> og be om å få være med i klubben. Da kan du hente ned materialet på nettet og til og med få medlemsbladet Amatørradio i posten. Det er ordentlig trivelig lesestoff!

## Forum
Det er etablert et diskusjonsforum der alle kan hive seg med i diskusjonen. Opprett gjerne en konto der så kan dere være med på moroa - live.

<b><a href="https://github.com/LA9IHA/piBug/discussions">https://github.com/LA9IHA/piBug/discussions</b> Diskusjonsforum.

Ta en tur innom der og vær aktiv. Skriver du noe interessant vil andre også gjøre det :)

Jeg hekter på nye artikler etter hvert som de blir publisert. God lesning og jeg håper dere kommer til å sette pris på dette.



73 es gd luck de LA9IHA Ottar
