from main import CryptoBot

def main(pair, frequency):
    exchange = CryptoBot(pair, frequency)
    print(exchange.find_current_price())


main('BTCUSDT', 'dayly')