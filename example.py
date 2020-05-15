from time import sleep

from fxrt import fx_rates

while True:
    prices = fx_rates()
    print(prices)
    sleep(5)
