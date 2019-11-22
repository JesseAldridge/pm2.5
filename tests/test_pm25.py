import sys, os, unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pm25

class TestStringMethods(unittest.TestCase):

  def test_find_lat_lon(self):
    results = pm25.find_lat_lon({'lat': 100, 'lng': 100})
    self.assertEqual({'lat': 100, 'lng': 100}, results)

  def test_pm25_info(self):
    results = pm25.pm25_info({'lat': 37.777904, 'lng': -122.411994})
    self.assertEqual(results['status'], 'ok')

if __name__ == '__main__':
  unittest.main()
