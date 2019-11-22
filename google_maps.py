import json, time

import requests

import secrets

def nearby_places(query, lat, lng, radius_miles):
  url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
  all_results = []
  next_page_token = None
  print('searching google maps...')
  for page in range(10):
    print('  page: {}'.format(page))
    params = {
      'key': secrets.GOOGLE_MAPS_API_KEY,
      'keyword': query,
      'inputtype': 'textquery',
      'fields': 'name,formatted_address,geometry',
      'radius': radius_miles * 1609.34, # 1 mile = 1609.34 meters
      'location': '{},{}'.format(lat, lng),
    }
    if next_page_token:
      params['pagetoken'] = next_page_token
    resp = requests.get(url, params=params)

    resp_dict = resp.json()
    all_results += resp_dict['results']
    if 'next_page_token' not in resp_dict:
      break
    time.sleep(2)
    next_page_token = resp_dict['next_page_token']
  return all_results

if __name__ == '__main__':
  results = nearby_places('coworking', 37.777904, -122.411994, radius_miles=20)
  print('results:', len(results))
