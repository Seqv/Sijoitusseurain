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
kem=yfinance.Ticker('KEMPOWR.HE')
indeksi=yfinance.Ticker('0P000134K9.F')
viking=yfinance.Ticker('VIK1V.HE')
nordea=yfinance.Ticker('NDA-FI.HE')
finnair=yfinance.Ticker('FIA1S.HE')
valmet=yfinance.Ticker('VALMT.HE')
elisa=yfinance.Ticker('ELISA.HE')
energiaetf=yfinance.Ticker('XDW0.DE')


finnairnyt = 0
indeksinyt = 0
kempowernyt = 0
vikingnyt = 0
nordeanyt = 0
valmetnyt = 0
elisanyt = 0
energiaetfnyt = 0

def hintanyt(symbol): # EI TOIMI RAHASTOILLA KOSKA NIILLÄ EI OLE "ARVOA"
    ticker = yfinance.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]
kempowernyt = hintanyt('KEMPOWR.HE')
#indeksinyt = hintanyt('0P000134K9.F')
vikingnyt = hintanyt('VIK1V.HE')
nordeanyt = hintanyt('NDA-FI.HE')
finnairnyt = hintanyt('FIA1S.HE')
valmetnyt = hintanyt('VALMT.HE')
elisanyt = hintanyt('ELISA.HE')
energiaetfnyt = hintanyt('XDW0.DE')




#def lambda_handler(event, context):  ### TÄMÄ RIVI KOODIA MAHDOLLISTAA OHJELMAN TOIMIMISEN AWS LAMBDASSA - LAMBDAN ULKOPUOLELLA KÄYTTÄESSÄ MUUTA AINA TÄMÄ RIVI KOMMENTIKSI #:N AVULLA

if 1 == 1:   ### JOS KÄYTÄT TÄTÄ LAMBDAN ULKOPUOLELLA, POISTA TÄMÄN RIVIN ENSIMMÄINEN #. NIMITTÄIN PYTHONISSA SISENNYKSILLÄ ON VÄLIÄ!

    alkuviesti = "--- Sijoitusten arvon muutos viime päivän ajalta: ---\n"

    # --- KEMPOWER ---  # Hankitaan tiedot halutuista osakkeista Yahoo Financen kautta (ja tehdään sama homma muille osakkeille)
    kempower_percent = 1 - (kem.fast_info['previousClose'] / kem.fast_info['lastPrice'])
    kempower_arrow = ":arrow_up:"
    if kempower_percent < 0:
        kempower_arrow = ":arrow_down:"

    # --- NORDNET INDEKSIRAHASTO SUOMI ESG ---
    indeksi_percent = 1 - (indeksi.fast_info['previousClose'] / indeksi.fast_info['lastPrice'])
    indeksi_arrow = ":arrow_up:"
    if indeksi_percent < 0:
        indeksi_arrow = ":arrow_down:"

    # --- VIKING LINE ---
    viking_percent = 1 - (viking.fast_info['previousClose'] / viking.fast_info['lastPrice'])
    viking_arrow = ":arrow_up:"
    if viking_percent < 0:
        viking_arrow = ":arrow_down:"


    # --- NORDEA ---
    nordea_percent = 1 - (nordea.fast_info['previousClose'] / nordea.fast_info['lastPrice'])
    nordea_arrow = ":arrow_up:"
    if nordea_percent < 0:
        nordea_arrow = ":arrow_down:"

    # --- FINNAIR ---
    finnair_percent = 1 - (finnair.fast_info['previousClose'] / finnair.fast_info['lastPrice'])
    finnair_arrow = ":arrow_up:"
    if finnair_percent < 0:
        finnair_arrow = ":arrow_down:"

    # --- VALMET ---
    valmet_percent = 1 - (valmet.fast_info['previousClose'] / valmet.fast_info['lastPrice'])
    valmet_arrow = ":arrow_up:"
    if valmet_percent < 0:
        valmet_arrow = ":arrow_down:"

    # --- ELISA ---
    elisa_percent = 1 - (elisa.fast_info['previousClose'] / elisa.fast_info['lastPrice'])
    elisa_arrow = ":arrow_up:"
    if elisa_percent < 0:
        elisa_arrow = ":arrow_down:"

    # --- ENERGIAETF Xtrackers MSCI World Energy UCITS ---
    energiaetf_percent = 1 - (energiaetf.fast_info['previousClose'] / energiaetf.fast_info['lastPrice'])
    energiaetf_arrow = ":arrow_up:"
    if energiaetf_percent < 0:
        energiaetf_arrow = ":arrow_down:"

    # "kasaa" webhook-viestit osakkeiden tiedoista.
    indeksidiscord = "Nordnet Indeksi Helsinki:   "+indeksi_arrow+"   {:.2%}\n".format(indeksi_percent)
    kempowerdiscord = "Kempower:    "+"Hinta:"+str(kempowernyt)[:6]+"€ "+kempower_arrow+"   {:.2%}\n".format(kempower_percent)
    vikingdiscord = "Viking Line:    "+"Hinta:"+str(vikingnyt)[:6]+"€ "+viking_arrow+"   {:.2%}\n".format(viking_percent)
    nordeadiscord = "Nordea:    "+"Hinta:"+str(nordeanyt)[:6]+"€ "+nordea_arrow+"   {:.2%}\n".format(nordea_percent)
    finnairdiscord = "Finnair:    "+"Hinta:"+str(finnairnyt)[:6]+"€ "+finnair_arrow+"   {:.2%}\n".format(finnair_percent)
    valmetdiscord = "Valmet:    "+"Hinta:"+str(valmetnyt)[:6]+"€ "+valmet_arrow+"   {:.2%}\n".format(valmet_percent)
    elisadiscord = "Elisa:    "+"Hinta:"+str(elisanyt)[:6]+"€ "+elisa_arrow+"   {:.2%}\n".format(elisa_percent)
    energiaetfdiscord = "Energia-ETF:    "+"Hinta:"+str(energiaetfnyt)[:6]+"€"+energiaetf_arrow+"   {:.2%}\n".format(energiaetf_percent)

    #+"Hinta:"+str(energiaetfnyt)[:6]+"€"

    yksiviesti = alkuviesti+indeksidiscord+kempowerdiscord+vikingdiscord+nordeadiscord+finnairdiscord+valmetdiscord+elisadiscord+energiaetfdiscord




    #lähettää webhookit discord-palvelimelle

    webhook = SyncWebhook.from_url('https://discordapp.com/api/webhooks/1100039135676342332/I6ivWE3OvqohE3DCsCKAptcHU2VxCWxLkhYrcXMjGLQVbwf3OeZV73G6MWJNMWMh8i0Y')
    #webhook.send(content=alkuviesti)
    #webhook.send(content=indeksidiscord)
    #webhook.send(content=kempowerdiscord)
    #webhook.send(content=vikingdiscord)
    #webhook.send(content=nordeadiscord)
    #webhook.send(content=finnairdiscord)
    #webhook.send(content=valmetdiscord)
    #webhook.send(content=elisadiscord)
    #webhook.send(content=energiaetfdiscord)
    webhook.send(content=yksiviesti)
