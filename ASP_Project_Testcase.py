import unittest
import Group6_ASP_Project as prog


class MyTestCase(unittest.TestCase):

    def test_sum(self):
        total = prog.CountryVisitors.total
        self.assertEqual(total, 26011511)

    def test_mean(self):
        mean = prog.CountryVisitors.mean
        self.assertEqual(mean, 1234567)


if __name__ == '__main__':
    unittest.main()