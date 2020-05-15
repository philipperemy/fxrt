## FXRT
 *Retrieve realtime FX prices from the Oanda broker.* 
 
 ### Installation
 
 From pip:
 
 ```
 pip install fxrt
 ```
 
 From the sources:
 
 ```
 git clone git@github.com:philipperemy/fxrt.git && cd fxrt
 pip3 install .
 ```
 
 
 ### Example
 
 Display the realtime feeds.
 
```bash
$ python example.py
{'AUD/CAD': {'bid': '0.90597', 'ask': '0.90626'}, 'AUD/CHF': {'bid': '0.62501', 'ask': '0.62530'} [...]
{'AUD/CAD': {'bid': '0.90584', 'ask': '0.90625'}, 'AUD/CHF': {'bid': '0.62498', 'ask': '0.62526'}, [...]
{'AUD/CAD': {'bid': '0.90584', 'ask': '0.90629'}, 'AUD/CHF': {'bid': '0.62493', 'ask': '0.62533'}, [...]
```
