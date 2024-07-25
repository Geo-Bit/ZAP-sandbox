import time
import os
from zapv2 import ZAPv2

target = 'http://juice-shop:3000'
api_key = os.getenv('ZAP_API_KEY')

zap = ZAPv2(apikey=api_key, proxies={
            'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})

print(f'Accessing target {target}')
zap.urlopen(target)
time.sleep(2)

print('Spidering target')
scan_id = zap.spider.scan(target)
time.sleep(2)
while int(zap.spider.status(scan_id)) < 100:
    print(f'Spider progress %: {zap.spider.status(scan_id)}')
    time.sleep(2)

print('Spider completed')
print('Scanning target')
scan_id = zap.ascan.scan(target)
while int(zap.ascan.status(scan_id)) < 100:
    print(f'Scan progress %: {zap.ascan.status(scan_id)}')
    time.sleep(5)

print('Scan completed')
print('Alerts:')
alerts = zap.core.alerts(baseurl=target)
for alert in alerts:
    print(alert)
