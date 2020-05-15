from datetime import datetime
from time import sleep

from fxrt.broker import FX

fx = FX()

while True:
    print(datetime.now(), fx.rates)
    sleep(3)
