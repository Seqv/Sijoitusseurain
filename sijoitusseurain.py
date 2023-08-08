import json
import subprocess
import sys
import os

import json

with open('config.json','r') as config_file:
    data = json.load(config_file)


discordwebhook = data['webhook']

sijoitus1ticker = data['sijoitus1ticker']
sijoitus2ticker = data['sijoitus2ticker']
sijoitus3ticker = data['sijoitus3ticker']
sijoitus4ticker = data['sijoitus4ticker']
sijoitus5ticker = data['sijoitus5ticker']
sijoitus6ticker = data['sijoitus6ticker']
sijoitus7ticker = data['sijoitus7ticker']
sijoitus8ticker = data['sijoitus8ticker']

sijoitus1nimi = data['sijoitus1nimi']
sijoitus2nimi = data['sijoitus2nimi']
sijoitus3nimi = data['sijoitus3nimi']
sijoitus4nimi = data['sijoitus4nimi']
sijoitus5nimi = data['sijoitus5nimi']
sijoitus6nimi = data['sijoitus6nimi']
sijoitus7nimi = data['sijoitus7nimi']
sijoitus8nimi = data['sijoitus8nimi']


# Asentaa yahoo finance- discord.py- ja requests-moduulit.
subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')
subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'requests'])
sys.path.append('/tmp')
subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'discord'])
sys.path.append('/tmp')
import requests
from discord import SyncWebhook

import yfinance

# Asettaa pörssiosakkeen YAHOO FINANCE-tickerin (löytääksesi omien sijoitusten tickerin, hae kyseistä osaketta sivulta finance.yahoo.com ja kopioi koodi.)
sijoitus1=yfinance.Ticker(sijoitus1ticker)
sijoitus2=yfinance.Ticker(sijoitus2ticker)
sijoitus3=yfinance.Ticker(sijoitus3ticker)
sijoitus4=yfinance.Ticker(sijoitus4ticker)
sijoitus5=yfinance.Ticker(sijoitus5ticker)
sijoitus6=yfinance.Ticker(sijoitus6ticker)
sijoitus7=yfinance.Ticker(sijoitus7ticker)
sijoitus8=yfinance.Ticker(sijoitus8ticker)


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

sijoitus1nyt = hintanyt(sijoitus1ticker)
#sijoitus2nyt = hintanyt(sijoitus2ticker) # ESIMERKKIOHJELMAN SIJOITUSKOHDE 2 ON RAHASTO - TÄMÄ TOIMINTO EI TOIMI RAHASTOILLA
sijoitus3nyt = hintanyt(sijoitus3ticker)
sijoitus4nyt = hintanyt(sijoitus4ticker)
sijoitus5nyt = hintanyt(sijoitus5ticker)
sijoitus6nyt = hintanyt(sijoitus6ticker)
sijoitus7nyt = hintanyt(sijoitus7ticker)
sijoitus8nyt = hintanyt(sijoitus8ticker)


#import boto3   ### TÄMÄ RIVI KOODIA MAHDOLLISTAA OHJELMAN TOIMIMISEN AWS LAMBDASSA, MUTTA TUO LAMBDAN ULKOPUOLELLA TURHAN RIIPPUVUUDEN. AWS LAMBDASSA POISTA TÄMÄN RIVIN KOMMENTOINTI POISTAMALLA # RIVIN ALUSTA
#def lambda_handler(event, context):  ### TÄMÄ RIVI KOODIA MAHDOLLISTAA OHJELMAN TOIMIMISEN AWS LAMBDASSA MUTTA RIKKOO OHJELMAN LAMBDAN ULKOPUOLELLA - AWS LAMBDASSA POISTA TÄMÄN RIVIN KOMMENTOINTI POISTAMALLA # RIVIN ALUSTA.

if 1 == 1:   ### JOS KÄYTÄT TÄTÄ OHJELMAA AWS LAMBDASSA, LISÄÄ TÄMÄN RIVIN ALKUUN #. NIMITTÄIN PYTHONISSA SISENNYKSILLÄ ON VÄLIÄ!

    alkuviesti = "--- Sijoitusten arvon muutos viime päivän ajalta: ---\n"

    # --- SIJOITUSKOHDE 1 - ESIMERKISSÄ KEMPOWER ---  # Hankitaan tiedot halutuista osakkeista Yahoo Financen kautta (ja tehdään sama homma muille osakkeille)
    sijoitus1_percent = 1 - (sijoitus1.get_fast_info['previousClose'] / sijoitus1.get_fast_info['lastPrice'])
    sijoitus1_arrow = ":arrow_up:"
    if sijoitus1_percent < 0:
        sijoitus1_arrow = ":arrow_down:"

    # --- SIJOITUSKOHDE 2 - ESIMERKISSÄ NORDNET INDEKSIRAHASTO SUOMI ESG ---
    sijoitus2_percent = 1 - (sijoitus2.get_fast_info['previousClose'] / sijoitus2.get_fast_info['lastPrice'])
    sijoitus2_arrow = ":arrow_up:"
    if sijoitus2_percent < 0:
        sijoitus2_arrow = ":arrow_down:"

    # --- SIJOITUSKOHDE 3 - ESIMERKISSÄ VIKING LINE ---
    sijoitus3_percent = 1 - (sijoitus3.get_fast_info['previousClose'] / sijoitus3.get_fast_info['lastPrice'])
    sijoitus3_arrow = ":arrow_up:"
    if sijoitus3_percent < 0:
        sijoitus3_arrow = ":arrow_down:"


    # --- SIJOITUSKOHDE 4 - ESIMERKISSÄ NORDEA ---
    sijoitus4_percent = 1 - (sijoitus4.get_fast_info['previousClose'] / sijoitus4.get_fast_info['lastPrice'])
    sijoitus4_arrow = ":arrow_up:"
    if sijoitus4_percent < 0:
        sijoitus4_arrow = ":arrow_down:"

    # --- SIJOITUSKOHDE 5 - ESIMERKISSÄ FINNAIR ---
    sijoitus5_percent = 1 - (sijoitus5.get_fast_info['previousClose'] / sijoitus5.get_fast_info['lastPrice'])
    sijoitus5_arrow = ":arrow_up:"
    if sijoitus5_percent < 0:
        sijoitus5_arrow = ":arrow_down:"

    # --- SIJOITUSKOHDE 6 - ESIMERKISSÄ sijoitus6 ---
    sijoitus6_percent = 1 - (sijoitus6.get_fast_info['previousClose'] / sijoitus6.get_fast_info['lastPrice'])
    sijoitus6_arrow = ":arrow_up:"
    if sijoitus6_percent < 0:
        sijoitus6_arrow = ":arrow_down:"

    # --- SIJOITUSKOHDE 7 - ESIMERKISSÄ sijoitus7 ---
    sijoitus7_percent = 1 - (sijoitus7.get_fast_info['previousClose'] / sijoitus7.get_fast_info['lastPrice'])
    sijoitus7_arrow = ":arrow_up:"
    if sijoitus7_percent < 0:
        sijoitus7_arrow = ":arrow_down:"

    # --- SIJOITUSKOHDE 8 - ESIMERKISSÄ sijoitus8 Xtrackers MSCI World Energy UCITS ---
    sijoitus8_percent = 1 - (sijoitus8.get_fast_info['previousClose'] / sijoitus8.get_fast_info['lastPrice'])
    sijoitus8_arrow = ":arrow_up:"
    if sijoitus8_percent < 0:
        sijoitus8_arrow = ":arrow_down:"

    # "kasaa" webhook-viestit osakkeiden tiedoista.
    sijoitus1discord = sijoitus1nimi+"Hinta:"+str(sijoitus1nyt)[:6]+"€ "+sijoitus1_arrow+"   {:.2%}\n".format(sijoitus1_percent)
    sijoitus2discord = sijoitus2nimi+sijoitus2_arrow+"   {:.2%}\n".format(sijoitus2_percent)           #tämä rivi on lyhyempi, koska tämä esimerkkisijoituskohde on rahasto, jolla ei ole osakkeiden kaltaista "hintaa"
    sijoitus3discord = sijoitus3nimi+"Hinta:"+str(sijoitus3nyt)[:6]+"€ "+sijoitus3_arrow+"   {:.2%}\n".format(sijoitus3_percent)
    sijoitus4discord = sijoitus4nimi+"Hinta:"+str(sijoitus4nyt)[:6]+"€ "+sijoitus4_arrow+"   {:.2%}\n".format(sijoitus4_percent)
    sijoitus5discord = sijoitus5nimi+"Hinta:"+str(sijoitus5nyt)[:6]+"€ "+sijoitus5_arrow+"   {:.2%}\n".format(sijoitus5_percent)
    sijoitus6discord = sijoitus6nimi+"Hinta:"+str(sijoitus6nyt)[:6]+"€ "+sijoitus6_arrow+"   {:.2%}\n".format(sijoitus6_percent)
    sijoitus7discord = sijoitus7nimi+"Hinta:"+str(sijoitus7nyt)[:6]+"€ "+sijoitus7_arrow+"   {:.2%}\n".format(sijoitus7_percent)
    sijoitus8discord = sijoitus8nimi+"Hinta:"+str(sijoitus8nyt)[:6]+"€"+sijoitus8_arrow+"   {:.2%}\n".format(sijoitus8_percent)

    #"kasaa" yksittäisten osakkeiden viestit yhdeksi kokonaiseksi viestiksi.
    yksiviesti = alkuviesti+sijoitus1discord+sijoitus2discord+sijoitus3discord+sijoitus4discord+sijoitus5discord+sijoitus6discord+sijoitus7discord+sijoitus8discord


    #lähettää webhookit discord-palvelimelle

    webhook = SyncWebhook.from_url(discordwebhook)
    webhook.send(content=yksiviesti)
