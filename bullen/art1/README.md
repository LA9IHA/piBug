# Hjemmebygg med mikrokontroller, piBug, nummer 1
## Polling
### Introduksjon
De siste årene har det vært en fantastisk utvikling innenfor mikrokontrollere og det er billig! For oss radioamatører kan vi lage styringsenhet for antennetuner, kontroll av SDR radio, repeaterlogikk og mye annet. I denne artikkelserien eksperimenterer vi med en elbug  på steroider. Ingen programmeringserfaring er nødvendig og vi lærer underveis. 

Å programmere mikrokontrollere er ikke vanskelig men annerledes enn PC programmering. Uten operativsystem må alt kodes. Det er tregere CPU, mindre RAM ulik testing mot hardwaren. Den bruker langt mindre strøm og fungerer i uker og måneder på batteri.

I dette prosjektet skal vi bruke en Raspberry Pi Pico. Det er lillesøsteren til Raspberry Pi og er 5 * 2 cm. Du programmerer prosessoren RP2040 i Python og den er din for en femtilapp. Her er det ikke noe Linux, kun blankt stål, og hvilket stål det er. La oss se kjapt på arkitekturen.

Med to kjerner, Proc0 og Proc1 kan to programmer kjøre samtidig! De deler en serie IO bus og interrupt systemet og du kan flytte av data mellom RAM banker uten å belaste CPU’en. Man kan også sette opp en rekke timere for å vekke opp funksjoner. For I/O er det puls bredde modulert output for å drive f.eks høyttalere eller steppermotorer,  seriekommunikasjon med to UART’s eller I2C til ekstern LCD display eller analog output. Du kan måle nivåer eller lese av et potmeter med en av to ADC. Som kronen på verket er det 29 generelle I/O porter som settes opp til den funksjonen man ønsker. Og ikke bare det frue, De kan også få Pico i WH versjon med innebygd internett og Bluetooth for kun noen et par tiere ekstra. Løp og kjøp!

Det er enkelt å komme i gang med massevis av dokumentasjon og aktivt miljø på internett. Strømforbruket er litt i øvre ende. Super Keyer III går i årevis på et par AA batterier mens Pico kun holder noen måneder på det samme. Hva du lærer her er også anvendelig for andre prosessorer.

Eksempelprogram 1: <interrupt1.py>

### Linker:
- **Leverandører**: Det er mulig Christech leverer. Hvis ikke har jeg hatt hell med <https://thepihut.com/products/raspberry-pi-pico>
- **Dokumentasjonssidene**: <https://www.raspberrypi.com/documentation/microcontrollers/?version=E0C9125B0D9B >
- **Bok om Python**: Programmering i Python algoritmer og kode. Skrindo, Knut Weider og Øystein Johannes. Flott norsk bok som du kan kjøpe hos Haugenbok.no eller låne på biblioteket.
- **Thonny**, programmeringsmiljøet: <https://thonny.org>
- **Kode**: [https://github.com/LA9IHA/piBug/ ](https://github.com/LA9IHA/piBug/tree/main/bullen/art1)
