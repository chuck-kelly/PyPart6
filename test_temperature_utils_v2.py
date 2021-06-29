import unittest
import temperature_utils_v2


class TemperatureUtilsTest(unittest.TestCase):

    def test_convert_to_celsius(self):
        test_cases = [
            (32, 0),
            (68, 20),
            (100, 37.78),
            (104, 40)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_to_celsius(temp_in))

    def test_convert_to_fahrenheit(self):
        test_cases = [
            (-17.7778, 0),
            (0, 32),
            (100, 212)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_to_fahrenheit(temp_in))
    #c to k,done
    def test_convert_celsius_kelvin(self):
        test_cases = [
            (-17.7778, 255.37219999999996),
            (0, 273.15),
            (100, 373.15)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_celsius_kelvin(temp_in))
    #f to k,done
    def test_convert_fahrenheit_kelvin(self):
        test_cases = [
            (0, 255.36999999999998),
            (32, 273.15),
            (212, 373.15)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_fahrenheit_kelvin(temp_in))
    #k to c,done
    def test_convert_kelvin_to_celsius(self):
        test_cases = [
            (100, -173.14999999999998),
            (300, 26.850000000000023),
            (500, 226.85000000000002)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_kelvin_to_celsius(temp_in))
#k to f
    def test_convert_kelvin_to_fahrenheit(self):
        test_cases = [
            (100, -279),
            (300, 80),
            (500, 440)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_kelvin_to_fahrenheit(temp_in))    

    def test_temperature_tuple(self):
        temps_input = (32, 68, 100, 104)
        expected = ((32, 0.0), (68, 20.0), (100, 37.78), (104, 40.0))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "f",'c')
        self.assertEqual(expected, actual)

    def test2_temperature_tuple(self):
        temps_input = (-17.7778, 0, 100)
        expected = ((-17.7778, 0.0), (0, 32.0), (100, 212.0))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "c",'f')
        self.assertEqual(expected, actual)
#c to k , done
    def test4_temperature_tuple(self):
        temps_input = (-17.7778, 0, 100)
        expected = ((-17.7778, 255.37219999999996), (0, 273.15), (100, 373.15))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "c",'k')
        self.assertEqual(expected, actual)
#f to k, done
    def test5_temperature_tuple(self):
        temps_input = (0, 32, 212)
        expected = ((0, 255.36999999999998), (32,273.15), (212,373.15))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "f",'k')
        self.assertEqual(expected, actual)
#k to f ,done
    def test6_temperature_tuple(self):
        temps_input = (100, 300, 500)
        expected = ((100, -279), (300,80), (500,440))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "k",'f')
        self.assertEqual(expected, actual)
#k to c, done
    def test7_temperature_tuple(self):
        temps_input = (100, 300, 500)
        expected = ((100, -173.14999999999998), (300, 26.850000000000023), (500, 226.85000000000002))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "k",'c')
        self.assertEqual(expected, actual)

    def test3_temperature_tuple(self):
        temps_input = (1, 2, 3)
        self.assertEqual(tuple(), temperature_utils_v2.temperature_tuple(temps_input, "a",'b'))
