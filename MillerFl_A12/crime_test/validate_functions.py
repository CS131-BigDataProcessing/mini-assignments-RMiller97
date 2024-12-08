# validate_functions.py

import pandas as pd

def validate_data(file_path):

    # Read dataset
    df = pd.read_csv(file_path)
    

    # Initialize counters
    invalid_sex = 0
    missing_sex = 0
    invalid_age = 0
    missing_age = 0

    # Check for invalid or missing values in 'Vict sex'
    for sex in df['Vict Sex']:
        if pd.isnull(sex):
            missing_sex += 1
        elif sex not in ['M', 'F']:
            invalid_sex += 1

    # Check for invalid or missing values in 'Vict age'
    for age in df['Vict Age']:
        if pd.isnull(age):
            missing_age += 1
        else:
            try:
                # Try converting age to integer
                age = int(age)
                if not (1 <= age <= 100):
                    invalid_age += 1
            except ValueError:
                # If it can't be converted to an int, count as invalid age
                invalid_age += 1

    # Return
    return {
        'invalid_sex': invalid_sex,
        'missing_sex': missing_sex,
        'invalid_age': invalid_age,
        'missing_age': missing_age
    }
