# Sijoitusseurain
Webhookeilla toimiva python-ohjelma, joka lähettää haluttujen sijoitusten päivittäiset muutokset halutulle Discord-palvelimelle. Toimii AWS Lambdassa ilman layereiden kanssa säätämistä - ohjelma asentaa lambdan puuttuvat dependencyt automaattisesti.

Tällä hetkellä ohjelma näyttää halutun sijoituskohteen

# Käyttö

Ohjelma on koodattu siten, että se on konfiguroitava koodia muuttamalla. Tässä tekstissä ja koodissa on kommentteja, jotka opastavat koodin käyttöä, ja miten omia sijoituskohteita voi lisätä.

Ohjelma EI TOIMI MUUTTUMATTOMANA. Sinun on VÄHINTÄÄN asetettava discord-webhookin osoite, joka on merkitty seuraavalle riville koodin alaosassa:
```
webhook = SyncWebhook.from_url('WEBHOOK TÄHÄN') ### VAIHDA TÄHÄN SINUN DISCORD-WEBHOOKISI URL-OSOITE!
```

Silloin kun olet asettanut webhookin onnistuneesti, koodin suorittuessa sinun pitäisi saada kahdeksan esimerkkisijoitusta.

Jotta saat omat sijoituksesi näkymään, voit katsoa mallia esimerkkipohjasta, eli sijoitus9:stä. Muuttamattomana esimerkit näkyvät kommentoituina, eli niillä ei ole mitään vaikutusta koodiin. Jos haluat käyttää niitä, poista #-merkki rivin alusta.


Esimerkkirivit ovat seuraavanlaisia:
```
sijoitus6discord = "Valmet:    "+"Hinta:"+str(sijoitus6nyt)[:6]+"€ "+sijoitus6_arrow+"   {:.2%}\n".format(sijoitus6_percent)
sijoitus7discord = "Elisa:    "+"Hinta:"+str(sijoitus7nyt)[:6]+"€ "+sijoitus7_arrow+"   {:.2%}\n".format(sijoitus7_percent)
sijoitus8discord = "Energia-ETF:    "+"Hinta:"+str(sijoitus8nyt)[:6]+"€"+sijoitus8_arrow+"   {:.2%}\n".format(sijoitus8_percent)
#sijoitus9discord = "<OSAKKEESI NIMI>:    "+"Hinta:"+str(sijoitus9nyt)[:6]+"<VALUUTTAMERKKI>"+sijoitus9_arrow+"   {:.2%}\n".format(sijoitus9_percent)
``` 

Eli, sinun on muutettava jokainen isoilla kirjaimilla <>-symbolien sisälle kirjoitettu teksti. Muista poistaa <>-merkit!
Esimerkiksi:
```
#sijoitus9nyt = hintanyt('<YAHOOFINANCETICKERTÄHÄN>')
```
olisi muutettava muotoon
```
sijoitus9nyt = hintanyt('OUT1V.HE')
``` 
Jossa siis OUT1V.HE on Yahoo Financen koodi Outokumpu Oyj-osakkeelle. Koodin voi löytää helposti yksinkertaisesti hakemalla osakkeen Yahoo Financesta. 

Kaikki määritettävät arvot ovat (ylhäältä alaspäin):

Sijoituskohteen Yahoo Finance Ticker <YAHOOFINANCETICKERTÄHÄN> (huom! määritettävä kahdessa eri kohdassa) 

Sijoituskohteen nimi <SIJOITUSKOHTEEN NIMI> - Nimi, jolla osake näkyy discord-viestissä.

Sijoituskohteen rahayksikön merkki <VALUUTTAMERKKI> - rahayksikön symboli, kuten € tai $. Vaihtelee, riippuen mistä pörssistä olet hankkinut sijoituskohteesi. 

SILLOIN KUN OLET VALMIS, POISTA KAIKKIEN ESIMERKKIPOHJARIVIEN KOMMENTOINTI POISTAMALLA #-SYMBOLI KOODIN ALUSTA.


Silloin kun olet saanut ohjelmaan asetettua vaikka esimerkkipohjalla ensimmäisen oman sijoituksesi, voit kopioida juuri tekemäsi sijoitus9-muuttujan koodin, mutta vaihda sijoitus9:n sijaan muuttujaksi esimerkiksi sijoitus10 ja asettaa kaikki määritettävät arvot. 

Oletuksena sisälletyt kahdeksan esimerkkisijoitusta eivät ole välttämättömiä ohjelmalle, vaan ne on mahdollista muuttaa tai poistaa kokonaan ilman ongelmia. 



# AWS Lambda

Yksi ratkaisu tämän ohjelman ilmaiseen hostaamiseen on AWS Lambda. Sen avulla voit myös ajastaa skriptin pyörimään tiettynä aikana.

TÄRKEÄÄ: Jos olet käyttämässä AWS Lambdaa, sinun on hieman muutettava seuraavaa koodia:
```
#def lambda_handler(event, context):  ### TÄMÄ RIVI KOODIA MAHDOLLISTAA OHJELMAN TOIMIMISEN AWS LAMBDASSA - LAMBDAN ULKOPUOLELLA KÄYTTÄESSÄ MUUTA AINA TÄMÄ RIVI KOMMENTIKSI LISÄÄMÄLLÄ # RIVIN ALKUUN

if 1 == 1:   ### JOS KÄYTÄT TÄTÄ LAMBDAN ULKOPUOLELLA, POISTA TÄMÄN RIVIN ENSIMMÄINEN #. NIMITTÄIN PYTHONISSA SISENNYKSILLÄ ON VÄLIÄ!
```

Eli: Silloin kun asetat ohjelman AWS-lambdaan, poista def lambda_handler-riviltä #, jotta koodi ei ole kommentoitu. Lisää samalla if 1 == 1 rivin alkuun #, joka taas muuttaa sen kommentiksi.

! JOS TEET KYSEISEN TOIMENPITEEN, OHJELMA EI TOIMI OIKEIN AWS LAMBDAN ULKOPUOLELLA !

kuitenkin muuttamalla koodin takaisin tilaan, jossa def lambda_handler-rivi on kommentoitu ja if 1==1-rivi ei koodi toimii taas normaalisti AWS Lambdan ulkopuolella.


Ohjelma käyttää toimiakseen pääosin (https://pypi.org/project/yfinance/ "YFinance")- ja (
https://pypi.org/project/discord.py/ "Discord.py")-kirjastoja.
