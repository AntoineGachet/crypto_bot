from datetime import datetime
import json
import os
from binance.client import Client 
from binance import BinanceSocketManager

client = Client('', '')
bsm = BinanceSocketManager(client)
# socket = 


class CryptoBot():
    def __init__(self, pair, frequency):
        self.pair = pair
        self.frequency = frequency
        self.interval_ = Client.KLINE_INTERVAL_1MINUTE if frequency == 'daily' else Client.KLINE_INTERVAL_1DAY
        self.period = '11' if frequency == 'daily' else '20'
        self.current_price = client.get_klines(symbol=self.pair, interval=self.interval_)
        self.closings_price = client.get_historical_klines(self.pair, Client.KLINE_INTERVAL_1MINUTE, f'{self.period} day ago UTC')
    
    def find_current_price(self):
        self.current_price = client.get_klines(symbol=self.pair, interval=self.interval_)

    def find_period_price(self):
        self.period_price = client.get_historical_klines(self.pair, Client.KLINE_INTERVAL_1MINUTE, f'{self.period} day ago UTC')
        return True

    def calc_RSI(self):
        self.pair = ''

    def calc_MA(self, period_price):
        pass

    def det_grid(self, name, currrent_price, calc_rsi):
        pass

    def trade(self, det_grid):
        pass


def add_crypto(pair, frequency):
        if str(datetime.now())[11:16:1] == "00:00":
            name = CryptoBot(pair, frequency)
