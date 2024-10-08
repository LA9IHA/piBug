# Hjemmebygg med mikrokontroller, piBug, nummer 4, August 2024.

Den fjerde og siste artikkelen er ivertfall påtenkt.

Nå er tiden for å samle trådene. Vi vil bygge et system med flere moduler som gjør at vi kan replisere en av de eksisterende programmerbare el-bugs tilgjengelige. Vi kan også utvide funksjonen. Dessuten kan vi lage andre moduler som f.eks morse tutor, ADF (revejakt), radio beacon og kanskje andre. Vi skal ivertfall får sett på noen av disse.

Vi må også se litt på testmetoder som er gode å ha med videre og vurdere for og mot Python. Er det andre alternativer og når er de bedre, kanskje aldri?

## I2C
I2C er en hardware nær kommunikasjonsstandard. LCD display mot en mikrokontroller er en typisk anvendelse av I2C. Andre perefirienheter kan også bruke I2C som oscillatorer, sensorer og meget mer. Det er en god artikkel om dette på https://www.halvorsen.blog/documents/technology/iot/pico/pico_i2c.php

## LCD display
- **Toms Hardware, hvordan bruke I2C LCD Display med Raspberry Pi Pico**: https://www.tomshardware.com/how-to/lcd-display-raspberry-pi-pico
- **Passende LCD display**: https://www.banggood.com/HW-060B-1602-LCD-5V-Yellow-green-Screen-IIC-I2C-Interface-Module-1602-LCD-Display-Adapter-Board-p-1885095.html?cur_warehouse=CN&rmmds=search
- **Datablad, LCD display**: https://www.vishay.com/docs/37484/lcd016n002bcfhet.pdf
- alternativt: https://files.waveshare.com/upload/2/2e/LCD1602_RGB_Module.pdf

## Raspberry Pico 2
- **Om Pico 2**: https://www.raspberrypi.com/news/raspberry-pi-pico-2-our-new-5-microcontroller-board-on-sale-now/
- **Presentasjon av Pico 2 av Jeff Geerling**: https://www.youtube.com/watch?v=oXF_lVwA8A4

## Debugging
- **Debug i Thonny**: https://jongarvin.com/up/ICS3U/handouts/ICS3U_debugger_thonny.pdf
- **Raspberry Pi Debug probe eller bruke en Pico for debugging**: https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html
- **Raspberry Pi debug probe**: https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html

## Søvn
Søvn er viktig for oss alle, også den lille Pico'en. Når den sover så bruker den mye mindre energi og batteriet varer lengre. Her er litt ekstramateriale om sleep.

- https://github.com/raspberrypi/pico-playground/blob/7b53edc86106ae8e0bbba5026372294608747cff/sleep/hello_dormant/hello_dormant.c#L27
- https://ghubcoder.github.io/posts/waking-the-pico-external-trigger/

## Kode
Joda, det kommer også kode etter hvert.

## Andre linker:
- **Dokumentasjonssidene**: <https://www.raspberrypi.com/documentation/microcontrollers/?version=E0C9125B0D9B> Raspberry Pi sine egne dokumentasjonssider
- **Cad**: <https://github.com/ncarandini/KiCad-RP-Pico> setup for Raspberry Pi Pico for KiCad
- **Kurs om Raspberry Pico**: https://core-electronics.com.au/courses/raspberry-pi-pico-workshop/#1.1
- **Software definert radio (SDR) med Raspberry Pico**: https://www.youtube.com/watch?v=lS1ZRMIYLjA

## Tilbake til samleside
* <a href="https://github.com/LA9IHA/piBug/blob/main/bullen/">Om artikkelen</a>
