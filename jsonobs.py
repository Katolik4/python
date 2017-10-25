try:
    import json
except ImportError:
    import ujson as json

with open('config.json', 'r') as f:
    c = json.loads(f.read())

siec = c['siec']
print(siec['ssid'])
