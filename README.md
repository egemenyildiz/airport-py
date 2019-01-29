airport-py
==========

Tiny MacOS only python library to integrate/use wi-fi scan results in your python projects. Wi-Fi scan data gathered by calling & parsing the results of a small MacOS cli utility called "[airport](https://eclecticlight.co/2017/07/08/airport-a-hidden-wi-fi-tool-in-macos-sierra)".

`/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport` is the default path to program executable. Exporting environment variable `AIRPORT_PATH` will update the defaults if you have your executable in a different path. 

Installation
------------

`pip install airport-py`


Usage
-----
```python
import airport

# current connection 

print airport.info()

InfoResult(agrCtlRSSI='-64', agrExtRSSI='0', agrCtlNoise='-92', agrExtNoise='0', state='running', 
op_mode='station', lastTxRate='702', maxRate='1300', lastAssocStatus='0', 
auth_80211='open', auth_link='wpa2-psk', BSSID='d0:3:4b:e9:55:99', SSID='AirPortTimeCapsule', 
MCS='5', channel='44,80')

# wi-fi scanning

scan_results = airport.scan()

print map(lambda r: (r.ssid, r.bssid, r.channel), scan_results[:3])

[('kablo-ac', 'fd:4a:e9:6f:95:7e', '52'),
 ('kablo', 'fd:4a:e9:6f:95:7d', '11'),
 ('oz-hukuk', '88:31:fd:4e:20:67', '11')]
 ```
