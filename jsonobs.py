import ujson

f = open('config.json', 'r')
c = ujson.loads(f.read())
siec = c['siec']
print(siec['ssid'])
#print(c)
f.close()
