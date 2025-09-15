# =====================================
# 🚀 Exercise 1: Fibonacci Calculation
# =====================================

def fib(n):
	"""
	Return the nth Fibonacci number using recursion.
	"""
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

# Test Exercise 1
print("Fibonacci Test:")
for i in range(11):
	print(f"fib({i}) = {fib(i)}")

# ============================================
# 🧠 Exercise 2: Convert Integer to Binary
# ============================================

def to_binary(n):
	"""
	Convert an integer n to its binary representation using recursion.
	"""
	if n == 0:
		return "0"
	elif n == 1:
		return "1"
	else:
		return to_binary(n // 2) + str(n % 2)

# Test Exercise 2
print("\nBinary Conversion Test:")
for num in [2, 12, 0, 7, 15]:
	print(f"to_binary({num}) = {to_binary(num)}")

# =============================================
# Exercise 3: Bellevue Almshouse Dataset
# =============================================

import pandas as pd

def task_1():
	url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
	df_bellevue = pd.read_csv(url)
	df_bellevue['gender'] = df_bellevue['gender'].str.strip().str.lower()
	df_bellevue.loc[~df_bellevue['gender'].isin(['m', 'f']), 'gender'] = pd.NA
	missing_counts = df_bellevue.isna().sum()
	sorted_columns = missing_counts.sort_values().index.tolist()
	return sorted_columns

def task_2(df_bellevue):
	print("Columns in dataset:", df_bellevue.columns.tolist())
	if 'date_in' in df_bellevue.columns:
		df_bellevue['year'] = pd.to_datetime(df_bellevue['date_in'], errors='coerce').dt.year
		admissions_per_year = df_bellevue.groupby('year').size().reset_index(name='total_admissions')
		return admissions_per_year
	else:
		print("No suitable column for year found.")
		return None

def task_3(df_bellevue):
	df_bellevue['gender'] = df_bellevue['gender'].str.strip().str.lower()
	df_bellevue.loc[~df_bellevue['gender'].isin(['m', 'f']), 'gender'] = pd.NA
	df_bellevue['age'] = pd.to_numeric(df_bellevue['age'], errors='coerce')
	if df_bellevue['age'].isna().sum() > 0:
		print("Some age values were non-numeric and converted to NaN.")
	avg_age_by_gender = df_bellevue.groupby('gender')['age'].mean()
	return avg_age_by_gender

def task_4(df_bellevue):
	df_bellevue['profession'] = df_bellevue['profession'].str.strip().str.lower()
	if df_bellevue['profession'].isna().sum() > 0:
		print("Some profession values are missing or invalid.")
	top5 = df_bellevue['profession'].value_counts().head(5).index.tolist()
	return top5

# Test Exercise 3
print("\nExercise 3 Tests:")
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)
print("Sorted columns by missing values:")
print(task_1())
print("Admissions per year:")
print(task_2(df_bellevue))
print("Average age by gender:")
print(task_3(df_bellevue))
print("Top 5 professions:")
print(task_4(df_bellevue))

