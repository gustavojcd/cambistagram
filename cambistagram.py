import os
from telegram.ext import (Updater, CommandHandler)
import requests

def get_data(market_id):
    url = f'https://www.buda.com/api/v2/markets/{market_id}/ticker'
    response = requests.get(url)
    data = response.json()
    return data['ticker']['last_price'][0]

def start(update, context):
    update.message.reply_text('Bienvenido')

def btc_pen(update, context):
    data = get_data('BTC-PEN')
    message = f'BTC-PEN: {data}'
    update.message.reply_text(message)

def ltc_pen(update, context):
    data = get_data('LTC-PEN')
    message = f'LTC-PEN: {data}'
    update.message.reply_text(message)

def eth_pen(update, context):
    data = get_data('ETH-PEN')
    message = f'ETH-PEN: {data}'
    update.message.reply_text(message)

if __name__ == '__main__':
    updater = Updater(
        token=os.environ['TOKEN'], use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('btc',btc_pen))
    dp.add_handler(CommandHandler('ltc',ltc_pen))
    dp.add_handler(CommandHandler('eth',eth_pen))
    updater.start_polling()
    updater.idle()
