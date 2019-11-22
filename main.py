import json

import google_maps, pm25

locations = google_maps.nearby_places('coworking', 37.77, -122.41, radius_miles=10)
for location in locations:
  print('adding pm25 info for location:', location['name'])
  location['pm25_info'] = pm25.pm25_info(location)

with open('out.json', 'w') as f:
  f.write(json.dumps(locations, indent=2))
