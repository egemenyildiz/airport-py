from collections import namedtuple

NodeResult = namedtuple(
    'NodeResult', 'ssid bssid rssi channel high_throughput country_code security')
NodeResult.__new__.__defaults__ = (None,) * len(NodeResult._fields)

InfoResult = namedtuple(
    'InfoResult', 'agrCtlRSSI agrExtRSSI agrCtlNoise agrExtNoise state '
                  'op_mode lastTxRate maxRate lastAssocStatus auth_80211 auth_link '
                  'BSSID SSID MCS channel'
)
InfoResult.__new__.__defaults__ = (None,) * len(InfoResult._fields)