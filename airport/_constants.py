SCAN_RESULTS_GROUPED_PATTERN = (r'(?P<ssid>.+)\s+(?P<bssid>([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))\s+(?P<rssi>[0-9+\- '
                                r']{1,4})\s+(?P<channel>[0-9,\-+]{1,6})\s+(?P<high_throughput>[YN])\s+('
                                r'?P<country_code>[A-Z\-]{2,3})\s+(?P<security>.+)$')
