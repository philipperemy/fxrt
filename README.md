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
 pip install .
 ```
 
 
 ### Example
 
 Display the realtime feeds.
 
```bash
$ python example.py
2020-05-16 07:34:46 {'AUD/CAD': {'bid': '0.90453', 'ask': '0.90550'}, 'AUD/CHF': {'bid': '0.62273', 'ask': '0.62365'}, [...]
2020-05-16 07:34:51 {'AUD/CAD': {'bid': '0.90453', 'ask': '0.90550'}, 'AUD/CHF': {'bid': '0.62273', 'ask': '0.62365'}, [...]
2020-05-16 07:34:56 {'AUD/CAD': {'bid': '0.90453', 'ask': '0.90550'}, 'AUD/CHF': {'bid': '0.62273', 'ask': '0.62365'}, [...]
```
