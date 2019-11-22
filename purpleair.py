import json, os, math

import requests

if os.path.exists('purpleair.json'):
  with open('purpleair.json') as f:
    text = f.read()
  resp_dict = json.loads(text)
else:
  resp = requests.get('https://www.purpleair.com/data.json')
  resp_dict = resp.json()

  print('pulled {} sensors'.format(len(resp_dict['data'])))

  with open('purpleair.json', 'w') as f:
    f.write(json.dumps(resp_dict, indent=2))


# "ID","pm","age","pm_0","pm_1","pm_2","pm_3","pm_4","pm_5","pm_6","conf",
# "pm1","pm_10","p1","p2","p3","p4","p5","p6",
# "Humidity","Temperature","Pressure","Elevation","Type","Label",
# "Lat","Lon","Icon","isOwner","Flags","Voc","Ozone1","Adc","CH"


sensors = []
for row in resp_dict['data']:
  sensor = {key: val for key, val in zip(resp_dict['fields'], row)}
  if not sensor['Lat'] or not sensor['Lon']:
    continue
  sensors.append(sensor)

my_lat = 37.777904
my_lon = -122.411994

def dist_miles(sensor):
  return math.sqrt((sensor['Lat'] - my_lat) ** 2 + (sensor['Lon'] - my_lon) ** 2) * 69
print('nearby sensors:')
for sensor in sorted(sensors, key=dist_miles)[:5]:
  print('{} miles away: {}'.format(round(dist_miles(sensor), 2), sensor))
