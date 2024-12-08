# stats_function.py

import pandas as pd

def calc_age_stats(file_path):

    df = pd.read_csv(file_path)

    # Drop rows with missing 'Vict Age' values
    df_clean = df.dropna(subset=['Vict Age'])

    # If no rows have valid entires after cleaning
    if df_clean.empty:
        return {
            'mean_age': float('nan'),
            'median_age': float('nan')
        }

    # Calculate mean and median for 'Vict Age'
    mean_age = df_clean['Vict Age'].mean()
    median_age = df_clean['Vict Age'].median()

    return {
        'mean_age': mean_age,
        'median_age': median_age
    }
