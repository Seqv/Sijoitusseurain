import json
import subprocess
import sys
import boto3
import os

# Asentaa yahoo financen
subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')
subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'requests'])
sys.path.append('/tmp')
subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'discord'])
sys.path.append('/tmp')
import requests
from discord import SyncWebhook

import yfinance

# Asettaa pörssiosakkeen YAHOO FINANCE-tickerin (jos haluat lisätä omia osakkeita, hae kyseistä osaketta sivulta finance.yahoo.com ja kopioi koodi.)
sijoitus1=yfinance.Ticker('KEMPOWR.HE')
sijoitus2=yfinance.Ticker('0P000134K9.F')
sijoitus3=yfinance.Ticker('VIK1V.HE')
sijoitus4=yfinance.Ticker('NDA-FI.HE')
sijoitus5=yfinance.Ticker('FIA1S.HE')
sijoitus6=yfinance.Ticker('VALMT.HE')
sijoitus7=yfinance.Ticker('ELISA.HE')
sijoitus8=yfinance.Ticker('XDW0.DE')



sijoitus1nyt = 0
sijoitus2nyt = 0
sijoitus3nyt = 0
sijoitus4nyt = 0
sijoitus5nyt = 0
sijoitus6nyt = 0
sijoitus7nyt = 0
sijoitus8nyt = 0

def hintanyt(symbol): # EI TOIMI RAHASTOILLA KOSKA NIILLÄ EI OLE "ARVOA"
    ticker = yfinance.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]
sijoitus1nyt = hintanyt('KEMPOWR.HE')
#sijoitus2nyt = hintanyt('0P000134K9.F') # ESIMERKKIOHJELMAN SIJOITUSKOHDE 2 ON RAHASTO - TÄMÄ TOIMINTO EI TOIMI RAHASTOILLA
sijoitus3nyt = hintanyt('VIK1V.HE')
sijoitus4nyt = hintanyt('NDA-FI.HE')
sijoitus5nyt = hintanyt('FIA1S.HE')
sijoitus6nyt = hintanyt('VALMT.HE')
sijoitus7nyt = hintanyt('ELISA.HE')
sijoitus8nyt = hintanyt('XDW0.DE')




#def lambda_handler(event, context):  ### TÄMÄ RIVI KOODIA MAHDOLLISTAA OHJELMAN TOIMIMISEN AWS LAMBDASSA - LAMBDAN ULKOPUOLELLA KÄYTTÄESSÄ MUUTA AINA TÄMÄ RIVI KOMMENTIKSI LISÄÄMÄLLÄ # RIVIN ALKUUN

if 1 == 1:   ### JOS KÄYTÄT TÄTÄ LAMBDAN ULKOPUOLELLA, POISTA TÄMÄN RIVIN ENSIMMÄINEN #. NIMITTÄIN PYTHONISSA SISENNYKSILLÄ ON VÄLIÄ!

    alkuviesti = "--- Sijoitusten arvon muutos viime päivän ajalta: ---\n"

    # --- SIJOITUSKOHDE 1 - ESIMERKISSÄ KEMPOWER ---  # Hankitaan tiedot halutuista osakkeista Yahoo Financen kautta (ja tehdään sama homma muille osakkeille)
    sijoitus1_percent = 1 - (sijoitus1.fast_info['previousClose'] / sijoitus1.fast_info['lastPrice'])
    sijoitus1_arrow = ":arrow_up:"
    if sijoitus1_percent < 0:
        sijoitus1_arrow = ":arrow_down:"

    # --- SIJOITUSKOHDE 2 - ESIMERKISSÄ NORDNET INDEKSIRAHASTO SUOMI ESG ---
    sijoitus2_percent = 1 - (sijoitus2.fast_info['previousClose'] / sijoitus2.fast_info['lastPrice'])
    sijoitus2_arrow = ":arrow_up:"
    if sijoitus2_percent < 0:
        sijoitus2_arrow = ":arrow_down:"

    # --- SIJOITUSKOHDE 3 - ESIMERKISSÄ VIKING LINE ---
    sijoitus3_percent = 1 - (sijoitus3.fast_info['previousClose'] / sijoitus3.fast_info['lastPrice'])
    sijoitus3_arrow = ":arrow_up:"
    if sijoitus3_percent < 0:
        sijoitus3_arrow = ":arrow_down:"


    # --- SIJOITUSKOHDE 4 - ESIMERKISSÄ NORDEA ---
    sijoitus4_percent = 1 - (sijoitus4.fast_info['previousClose'] / sijoitus4.fast_info['lastPrice'])
    sijoitus4_arrow = ":arrow_up:"
    if sijoitus4_percent < 0:
        sijoitus4_arrow = ":arrow_down:"

    # --- SIJOITUSKOHDE 5 - ESIMERKISSÄ FINNAIR ---
    sijoitus5_percent = 1 - (sijoitus5.fast_info['previousClose'] / sijoitus5.fast_info['lastPrice'])
    sijoitus5_arrow = ":arrow_up:"
    if sijoitus5_percent < 0:
        sijoitus5_arrow = ":arrow_down:"

    # --- SIJOITUSKOHDE 6 - ESIMERKISSÄ sijoitus6 ---
    sijoitus6_percent = 1 - (sijoitus6.fast_info['previousClose'] / sijoitus6.fast_info['lastPrice'])
    sijoitus6_arrow = ":arrow_up:"
    if sijoitus6_percent < 0:
        sijoitus6_arrow = ":arrow_down:"

    # --- SIJOITUSKOHDE 7 - ESIMERKISSÄ sijoitus7 ---
    sijoitus7_percent = 1 - (sijoitus7.fast_info['previousClose'] / sijoitus7.fast_info['lastPrice'])
    sijoitus7_arrow = ":arrow_up:"
    if sijoitus7_percent < 0:
        sijoitus7_arrow = ":arrow_down:"

    # --- SIJOITUSKOHDE - ESIMERKISSÄ sijoitus8 Xtrackers MSCI World Energy UCITS ---
    sijoitus8_percent = 1 - (sijoitus8.fast_info['previousClose'] / sijoitus8.fast_info['lastPrice'])
    sijoitus8_arrow = ":arrow_up:"
    if sijoitus8_percent < 0:
        sijoitus8_arrow = ":arrow_down:"

    # "kasaa" webhook-viestit osakkeiden tiedoista.
    sijoitus1discord = "Kempower:    "+"Hinta:"+str(sijoitus1nyt)[:6]+"€ "+sijoitus1_arrow+"   {:.2%}\n".format(sijoitus1_percent)
    sijoitus2discord = "Nordnet Indeksi Helsinki:   "+sijoitus2_arrow+"   {:.2%}\n".format(sijoitus2_percent)           #tämä rivi on lyhyempi, koska tämä esimerkkisijoituskohde on rahasto, jolla ei ole osakkeiden kaltaista "hintaa"
    sijoitus3discord = "Viking Line:    "+"Hinta:"+str(sijoitus3nyt)[:6]+"€ "+sijoitus3_arrow+"   {:.2%}\n".format(sijoitus3_percent)
    sijoitus4discord = "Nordea:    "+"Hinta:"+str(sijoitus4nyt)[:6]+"€ "+sijoitus4_arrow+"   {:.2%}\n".format(sijoitus4_percent)
    sijoitus5discord = "Finnair:    "+"Hinta:"+str(sijoitus5nyt)[:6]+"€ "+sijoitus5_arrow+"   {:.2%}\n".format(sijoitus5_percent)
    sijoitus6discord = "Valmet:    "+"Hinta:"+str(sijoitus6nyt)[:6]+"€ "+sijoitus6_arrow+"   {:.2%}\n".format(sijoitus6_percent)
    sijoitus7discord = "Elisa:    "+"Hinta:"+str(sijoitus7nyt)[:6]+"€ "+sijoitus7_arrow+"   {:.2%}\n".format(sijoitus7_percent)
    sijoitus8discord = "Energia-ETF:    "+"Hinta:"+str(sijoitus8nyt)[:6]+"€"+sijoitus8_arrow+"   {:.2%}\n".format(sijoitus8_percent)

    yksiviesti = alkuviesti+sijoitus1discord+sijoitus2discord+sijoitus3discord+sijoitus4discord+sijoitus5discord+sijoitus6discord+sijoitus7discord+sijoitus8discord




    #lähettää webhookit discord-palvelimelle

    webhook = SyncWebhook.from_url('https://discordapp.com/api/webhooks/1100039135676342332/I6ivWE3OvqohE3DCsCKAptcHU2VxCWxLkhYrcXMjGLQVbwf3OeZV73G6MWJNMWMh8i0Y')
    #webhook.send(content=alkuviesti)
    #webhook.send(content=sijoitus1discord)
    #webhook.send(content=sijoitus2discord)
    #webhook.send(content=sijoitus3discord)
    #webhook.send(content=sijoitus4discord)
    #webhook.send(content=sijoitus5discord)
    #webhook.send(content=sijoitus6discord)
    #webhook.send(content=sijoitus7discord)
    #webhook.send(content=sijoitus8discord)
    webhook.send(content=yksiviesti)
