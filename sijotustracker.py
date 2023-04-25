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
nordeanyt = 1
nordeanytstring = 1

# Asettaa pörssiosakkeen YAHOO FINANCE-tickerin (jos haluat lisätä omia osakkeita, hae kyseistä osaketta sivulta finance.yahoo.com ja kopioi koodi.)
kem=yfinance.Ticker('KEMPOWR.HE')
indeksi=yfinance.Ticker('0P000134K9.F')
viking=yfinance.Ticker('VIK1V.HE')
nordea=yfinance.Ticker('NDA-FI.HE')
finnair=yfinance.Ticker('FIA1S.HE')
valmet=yfinance.Ticker('VALMT.HE')
elisa=yfinance.Ticker('ELISA.HE')
energiaetf=yfinance.Ticker('XDW0.DE')


# Luo funktion, jonka avulla ohjelma voi ilmoittaa tämänhetkisen hinnan - EI TOIMI VIELÄ, TODO
#def hintanyt(symbol):
#    ticker = yfinance.Ticker(symbol)
#    todays_data = ticker.history(period='1d')
#    return todays_data['Close'][0]
#print(hintanyt('FIA1S.HE'))

def lambda_handler(event, context):
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
    kempowerdiscord = "Kempower:    "+kempower_arrow+"   {:.2%}\n".format(kempower_percent)
    vikingdiscord = "Viking Line:    "+viking_arrow+"   {:.2%}\n".format(viking_percent)
    nordeadiscord = "Nordea:    "+nordea_arrow+"   {:.2%}\n".format(nordea_percent)
    finnairdiscord = "Finnair:    "+finnair_arrow+"   {:.2%}\n".format(finnair_percent)
    valmetdiscord = "Valmet:    "+valmet_arrow+"   {:.2%}\n".format(valmet_percent)
    elisadiscord = "Elisa:    "+elisa_arrow+"   {:.2%}\n".format(elisa_percent)
    energiaetfdiscord = "Energia-ETF (Xtrackers MSCI World Energy UCITS):    "+energiaetf_arrow+"   {:.2%}\n".format(energiaetf_percent)



    alkuviesti = "--- Sijoitusten arvon muutos viime päivän ajalta: ---"

    #lähettää webhookit discord-palvelimelle

    webhook = SyncWebhook.from_url('WEBHOOK TÄHÄN')
    webhook.send(content=alkuviesti)
    webhook.send(content=indeksidiscord)
    webhook.send(content=kempowerdiscord)
    webhook.send(content=vikingdiscord)
    webhook.send(content=nordeadiscord)
    webhook.send(content=finnairdiscord)
    webhook.send(content=valmetdiscord)
    webhook.send(content=elisadiscord)
    webhook.send(content=energiaetfdiscord)
