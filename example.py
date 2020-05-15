from time import sleep

from fxrt import fx_rates
from datetime import datetime

while True:
    prices = fx_rates()
    print(datetime.now().replace(microsecond=0), prices)
    sleep(5)
