import unittest
import sensor_app


class Testing(unittest.TestCase):
    def test_average(self):
        test_list = [{"1" : 30, "2" : 0, "3" : 10, "4" : 3}, {"1" : 20, "2" : 4, "3" : 18}, {"1" : 0, "2" : 15, "3" : 40}]

        a = sensor_app.average("1", test_list)
        b = round(50/3, 2)
        self.assertEqual(a, b)

        c = sensor_app.average("10", test_list)
        self.assertEqual(c, 0)

        d = sensor_app.average("4", test_list)
        self.assertEqual(d, 3)

if __name__ == '__main__':
    unittest.main()