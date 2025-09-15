def task_4(df_bellevue):
    """
    Return a list of the 5 most common professions in order of prevalence (most common first).
    """
    # Clean profession column (strip whitespace, lower case)
    df_bellevue['profession'] = df_bellevue['profession'].str.strip().str.lower()
    # Print explanation if there are missing or odd values
    if df_bellevue['profession'].isna().sum() > 0:
        print("Some profession values are missing or invalid.")
    # Get top 5 most common professions
    top5 = df_bellevue['profession'].value_counts().head(5).index.tolist()
    return top5
def task_3(df_bellevue):
    """
    Return a Series with:
    - Index: gender (for each gender in the data)
    - Values: the average age for the indexed gender.
    """
    # Clean gender column
    df_bellevue['gender'] = df_bellevue['gender'].str.strip().str.lower()
    df_bellevue.loc[~df_bellevue['gender'].isin(['m', 'f']), 'gender'] = pd.NA
    # Clean age column (convert to numeric, coerce errors)
    df_bellevue['age'] = pd.to_numeric(df_bellevue['age'], errors='coerce')
    # Print explanation if there are non-numeric ages
    if df_bellevue['age'].isna().sum() > 0:
        print("Some age values were non-numeric and converted to NaN.")
    # Calculate average age by gender
    avg_age_by_gender = df_bellevue.groupby('gender')['age'].mean()
    return avg_age_by_gender
def task_2():
    """
    Return a DataFrame with two columns:
    - year: each year in the data
    - total_admissions: total number of entries (immigrant admissions) for each year
    """
    if 'year' not in df_bellevue.columns:
        print("Warning: 'year' column not found in dataset.")
        return None
    admissions_per_year = df_bellevue.groupby('year').size().reset_index(name='total_admissions')
    return admissions_per_year
# =====================================
# 🚀 Exercise 1: Fibonacci Calculation
# =====================================

def fib(n):
    """
    Return the nth Fibonacci number using recursion.

    The Fibonacci sequence starts with:
    0, 1, 1, 2, 3, 5, 8, 13, 21, ...

    Each number is the sum of the two numbers before it.

    Parameters:
    n (int): The position in the Fibonacci sequence (starting from 0).

    Returns:
    int: The nth Fibonacci number.
    """
    # Base case: if n is 0, return 0
    if n == 0:
        return 0

    # Base case: if n is 1, return 1
    elif n == 1:
        return 1

    # Recursive case: sum of previous two Fibonacci numbers
    else:
        return fib(n - 1) + fib(n - 2)
    
# Example usage:
print(fib(0))   # Output: 0
print(fib(1))   # Output: 1
print(fib(5))   # Output: 5
print(fib(10))  # Output: 55

# ============================================
# 🧠 Exercise 2: Convert Integer to Binary
# ============================================

def to_binary(n):
    """
    Convert an integer n to its binary representation using recursion.

    Parameters:
    n (int): The integer to convert (assumed to be non-negative).

    Returns:
    str: The binary representation of n as a string.
    """
    # Base case: if n is 0 or 1, return the string version of n
    if n == 0:
        return "0"
    elif n == 1:
        return "1"

    # Recursive case:
    # Convert the quotient (n // 2) and append the remainder (n % 2)
    return to_binary(n // 2) + str(n % 2)


# Example usage:
print(to_binary(2))    # Output: 10
print(to_binary(12))   # Output: 1100
print(to_binary(0))    # Output: 0
print(to_binary(7))    # Output: 111



import pandas as pd
import numpy as np

# Load the dataset
url = 'https://raw.githubusercontent.com/melaniewalsh/Intro-Cultural-Analytics/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

# Replace '?' with NaN in the 'gender' column
df_bellevue['gender'] = df_bellevue['gender'].replace('?', np.nan)

# Confirm the replacement
print(df_bellevue['gender'].head())



# =============================================
# 🏥 Exercise 3: Bellevue Almshouse Dataset
# =============================================


import pandas as pd

def task_1():
    url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
    df_bellevue = pd.read_csv(url)

    # Fix gender column
    df_bellevue['gender'] = df_bellevue['gender'].str.strip().str.lower()
    # Set any value not 'm' or 'f' to NA
    df_bellevue.loc[~df_bellevue['gender'].isin(['m', 'f']), 'gender'] = pd.NA

    # Calculate missing counts per column
    missing_counts = df_bellevue.isna().sum()

    # Sort columns by missing values (least to most)
    sorted_columns = missing_counts.sort_values().index.tolist()

    return sorted_columns

# Example usage:
sorted_columns = task_1()
print(sorted_columns)

import pandas as pd

def task_2(df_bellevue):
    # Inspect columns to find the year column
    print("Columns in dataset:", df_bellevue.columns.tolist())
    # Try to extract year from a likely column
    if 'date_in' in df_bellevue.columns:
        # Extract year from 'date_in' column
        df_bellevue['year'] = pd.to_datetime(df_bellevue['date_in'], errors='coerce').dt.year
        admissions_per_year = df_bellevue.groupby('year').size().reset_index(name='total_admissions')
        return admissions_per_year
    else:
        print("No suitable column for year found.")
        return None

# Test task_2 function
if __name__ == "__main__":
    url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
    df_bellevue = pd.read_csv(url)
    admissions_per_year = task_2(df_bellevue)
    print(admissions_per_year)

    # Test task_3 function
    avg_age_by_gender = task_3(df_bellevue)
    print("Average age by gender:")
    print(avg_age_by_gender)

    # Test task_4 function
    top5_professions = task_4(df_bellevue)
    print("Top 5 professions:")
    print(top5_professions)

