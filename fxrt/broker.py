import re
import threading
from time import time, sleep

import requests

from fxrt.rc4 import decrypt


def fx_rates():
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,fr;q=0.8,pt;q=0.7,zh-CN;q=0.6,zh;q=0.5',
        'origin': 'https://www1.oanda.com',
        'referer': 'https://www1.oanda.com/currency/live-exchange-rates/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

    # Found in ./Live Exchange Rates _ OANDA_files/rc4-ea63ca8c97e3cbcd75f72603d4e99df48eb46f66.js
    # Called in ./Live Exchange Rates _ OANDA_files/liverates.js
    # 355:                            ref.update(rc4decrypt(request.responseText));
    key = 'aaf6cb4f0ced8a211c2728328597268509ade33040233a11af'
    ts = int(time() * 1000)
    assert len(str(ts)) == len(str('1589549499500'))
    url = f'https://www.oanda.com/lfr/rates_lrrr?tstamp={ts}'
    prices = decrypt(key, requests.get(url=url, headers=headers).content.decode('utf8'))
    prices = re.findall('[A-Z]{3}/[A-Z]{3}=[0-9.=]+', prices)
    return {k: dict(zip(['bid', 'ask'], v.split('=')[:2])) for (k, v)
            in dict([p.split('=', 1) for p in prices]).items()}


class FX:

    def __init__(self):
        self.rates = {}
        self.thread = threading.Thread(target=self.poll)
        self.thread.start()
        self.ready = False
        while not self.ready:
            sleep(0.001)

    def poll(self):
        while True:
            self.rates = fx_rates()
            self.ready = True
            sleep(1)
