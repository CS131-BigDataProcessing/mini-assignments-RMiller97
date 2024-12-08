# test_validate_functions.py

import unittest
import pandas as pd
from validate_functions import validate_data

class TestValidateFunctions(unittest.TestCase):

    def clean_csv_data(self, file_path):
        # Read csv data
        df = pd.read_csv(file_path)

        # Clean column names
        df.columns = df.columns.str.strip()
       
        # Strip spaced from each value in entire dataframe
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        # Save the cleaned data back to the file
        df.to_csv(file_path, index=False)

    def test_valid_data(self):
        test_data = """
        Vict Sex,Vict Age
        M,25
        F,30
        M,40
        """
        # Create sample csv file for testing
        with open('valid_test_data.csv', 'w') as f:
            f.write(test_data)

        # Clean the data (strip of whitespace)
        self.clean_csv_data('valid_test_data.csv')
        

        # Run the function
        results = validate_data('valid_test_data.csv')

        # Test if there are no invalid or missing values
        self.assertEqual(results['invalid_sex'], 0)
        self.assertEqual(results['missing_sex'], 0)
        self.assertEqual(results['invalid_age'], 0)
        self.assertEqual(results['missing_age'], 0)

    def test_invalid_sex_type(self):
        test_data = """
        Vict Sex,Vict Age
        123,25
        F,30
        M,40
        """

        # Create test csv file
        with open('invalid_sex_data.csv', 'w') as f:
            f.write(test_data)

        # Clean the data (strip of whitespace)
        self.clean_csv_data('invalid_sex_data.csv')

        # Run the function
        result = validate_data('invalid_sex_data.csv')

        # AssertEqual testing
        self.assertEqual(result['invalid_sex'], 1)
        self.assertEqual(result['missing_sex'], 0)
        self.assertEqual(result['invalid_age'], 0)
        self.assertEqual(result['missing_age'], 0)

    def test_invalid_age_type(self):
        test_data = """
        Vict Sex,Vict Age
        M,25
        F,abc
        M,40
        """

        # Create test csv file
        with open('invalid_age_data.csv', 'w') as f:
            f.write(test_data)

        # Clean the test data (strip white space)
        self.clean_csv_data('invalid_age_data.csv')

        # Run the function
        result = validate_data('invalid_age_data.csv')

        # Assert Equal test
        self.assertEqual(result['invalid_sex'], 0)
        self.assertEqual(result['missing_sex'], 0)
        self.assertEqual(result['invalid_age'], 1)
        self.assertEqual(result['missing_age'], 0)

if __name__ == '__main__':
    unittest.main()
