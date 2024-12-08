# test_stats_function.py

import unittest
from stats_function import calc_age_stats
from math import isnan

class TestStatsFunction(unittest.TestCase):

    def test_valid_data(self):
        test_data = """
        Vict Sex,Vict Age
        M,25
        F,30
        M,40
        F,50
        """
        # Create sample csv file for testing
        with open('valid_age_data.csv', 'w') as f:
            f.write(test_data)

        # Run the function
        result = calc_age_stats('valid_age_data.csv')

        # Test if mean and median are correct
        self.assertEqual(result['mean_age'], 36.25)
        self.assertEqual(result['median_age'], 35)

    def test_empty_data(self):
        test_data = """
        Vict Sex,Vict Age
        """
        # Create sample csv for testing
        with open('empty_age_data.csv', 'w') as f:
            f.write(test_data)

        # Run the function
        result = calc_age_stats('empty_age_data.csv')

        # Test if both mean and median are NaN
        self.assertTrue(isnan(result['mean_age']))
        self.assertTrue(isnan(result['median_age']))

    def test_missing_values(self):
        test_data = """
        Vict Sex,Vict Age
        M,
        F,30
        M,40
        """

        # Create sample csv for testing
        with open('missing_age_data.csv', 'w') as f:
            f.write(test_data)

        # Run the function
        result = calc_age_stats('missing_age_data.csv')

        # Test if the function handled missing values correctly
        self.assertEqual(result['mean_age'], 35)
        self.assertEqual(result['median_age'], 35)

if __name__ == '__main__':
    unittest.main()
