import json

import requests

import secrets

def pm25_info(dict_):
  coordinates = find_lat_lon(dict_)
  url = 'https://api.waqi.info/feed/geo:{};{}/'.format(coordinates['lat'], coordinates['lng'])
  resp = requests.get(url, params={'token': secrets.PM25_API_KEY})
  return json.loads(resp.content)

def find_lat_lon(dict_):
  if not hasattr(dict_, 'values'):
    return None
  for key, child in dict_.items():
    if key == 'lat':
      return dict_
    else:
      result = find_lat_lon(child)
      if result:
        return result

if __name__ == '__main__':
  url = 'https://api.waqi.info/feed/geo:10.3;20.7/'
  resp = requests.get(url, params={'token': 'demo'})
  print('url:', resp.url)
  print('resp:', json.loads(resp.content))
