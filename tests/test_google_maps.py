import sys, os, unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import google_maps

class TestStringMethods(unittest.TestCase):

  def test_nearby_places(self):
    results = google_maps.nearby_places('coworking', 37, -122, radius_miles=10)
    self.assertTrue('geometry' in results[0])
    self.assertEqual(8, len(results))

if __name__ == '__main__':
  unittest.main()
