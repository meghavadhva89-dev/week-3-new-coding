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



