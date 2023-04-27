# Sijoitusseurain
Webhookeilla toimiva python-ohjelma, joka lähettää haluttujen sijoitusten päivittäiset muutokset halutulle Discord-palvelimelle. Toimii AWS Lambdassa ilman layereiden kanssa säätämistä - ohjelma asentaa lambdan puuttuvat dependencyt automaattisesti.

Tällä hetkellä ohjelma näyttää määritetyn sijoituskohteen:

- Tämänhetkisen hinnan
- Hinnan muutoksen 24 tunnin ajalta


Tulevia toimintoja:

- Hinnan muutos viimeisen viikon ajalta
- Hankintahinta (manuaalisesti asetettava)

# Käyttö

Tarvitset Pythonin tietokoneellesi ohjelman käyttöä varten, joten lataa uusin python-versio tarvittaessa. Ohjelma on luotu Python 3.10.10:llä, joten suosittelen, että käytät vähintään kyseistä python-versiota tai uudempaa.

Ohjelma on koodattu siten, että se on konfiguroitava config.json-tiedostoa muuttamalla tekstinkäsittelyohjelmalla. Tässä tekstissä ja koodissa on kommentteja, jotka opastavat myös itse koodin käyttöä, ja miten omia sijoituskohteita voi lisätä jos sitä haluat tehdä..

Ohjelma EI TOIMI MUUTTAMATTOMANA. Sinun on VÄHINTÄÄN asetettava discord-webhookin osoite, joka on merkitty config-tiedoston ensimmäiselle riville
```
"webhook" : "WEBHOOKTÄHÄN",
```

Silloin, kun olet asettanut webhookin onnistuneesti, koodin suorittuessa sinun pitäisi saada kahdeksan esimerkkisijoitusta lähetettyä Discord-palvelimelle webhookin kautta.

Jotta saat omat sijoituksesi näkymään, voit vaihtaa config-tiedoston kautta esimerkkisijoitusten yahoo finance-tickerin, nimen ja valuutan oman sijoituksen arvoiksi. Jos haluat yli kahdeksaa sijoitusta lisätä, voit vain kopioida koodista 


Esimerkiksi:
```
sijoitus8discord = sijoitus8nimi+"Hinta:"+str(sijoitus8nyt)[:6]+sijoitus8valuutta+sijoitus8_arrow+"   {:.2%}\n".format(sijoitus8_percent)
``` 
muutettaisiin yksinkertaisesti seuraavaksi:
```
sijoitus9discord = sijoitus9nimi+"Hinta:"+str(sijoitus9nyt)[:6]+sijoitus9valuutta+sijoitus9_arrow+"   {:.2%}\n".format(sijoitus9_percent)
``` 

Sinun on silloin luotava samaan tyyliin myös json-tiedostoon arvot.

```
#sijoitus9nyt = hintanyt('<YAHOOFINANCETICKERTÄHÄN>')



# AWS Lambda

Yksi ratkaisu tämän ohjelman ilmaiseen hostaamiseen on AWS Lambda. Sen avulla voit myös ajastaa skriptin pyörimään tiettynä aikana. Aseta ohjelmalle tarpeeksi ramia, 512mb riittää mainiosti, ja laita automaattinen aikakatkaisu tarpeeksi suureksi (5-10 minuuttiia riittää lähes kaikissa tapauksissa).

TÄRKEÄÄ: Jos olet käyttämässä AWS Lambdaa, sinun on hieman muutettava seuraavaa koodia kommenttien ohjeiden mukaisesti:
```
#import boto3   ### TÄMÄ RIVI KOODIA MAHDOLLISTAA OHJELMAN TOIMIMISEN AWS LAMBDASSA, MUTTA TUO LAMBDAN ULKOPUOLELLA TURHAN RIIPPUVUUDEN. AWS LAMBDASSA POISTA TÄMÄN RIVIN KOMMENTOINTI POISTAMALLA # RIVIN ALUSTA
#def lambda_handler(event, context):  ### TÄMÄ RIVI KOODIA MAHDOLLISTAA OHJELMAN TOIMIMISEN AWS LAMBDASSA MUTTA RIKKOO OHJELMAN LAMBDAN ULKOPUOLELLA - AWS LAMBDASSA POISTA TÄMÄN RIVIN KOMMENTOINTI POISTAMALLA # RIVIN ALUSTA.


if 1 == 1:   ### JOS KÄYTÄT TÄTÄ LAMBDAN ULKOPUOLELLA, POISTA TÄMÄN RIVIN ENSIMMÄINEN #. NIMITTÄIN PYTHONISSA SISENNYKSILLÄ ON VÄLIÄ!
```

Eli: Silloin kun asetat ohjelman AWS-lambdaan, poista import boto3-riviltä ja def lambda_handler-riviltä #, jotta koodi ei ole kommentoitu. Lisää samalla if 1 == 1 rivin alkuun #, joka taas muuttaa sen kommentiksi.

! JOS TEET KYSEISEN TOIMENPITEEN, OHJELMA EI TOIMI OIKEIN AWS LAMBDAN ULKOPUOLELLA !

kuitenkin muuttamalla koodin takaisin alkuperäiseen tilaan, jossa def lambda_handler-rivi on kommentoitu ja if 1==1-rivi ei, koodi toimii taas normaalisti AWS Lambdan ulkopuolella.

# Yleisimpiä virheitä

Virheen tapahtuessa Python näyttää tracebackin, eli näyttää millä rivillä ja mikä virhe on tapahtunut. Kaikkein alin rivi aina kertoo minkälainen virhe on tapahtunut.

```
ValueError: Invalid webhook URL given.
```
Et ole määrittänyt webhookia, eli "osoitetta", johon tiedot pitäisi lähettää. [Näin luot Discord-Webhookin.](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)



Ohjelma käyttää toimiakseen pääosin [YFinance](https://pypi.org/project/yfinance/) ja [Discord.py](
https://pypi.org/project/discord.py/)-kirjastoja.
