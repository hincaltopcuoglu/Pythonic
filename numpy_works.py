import numpy as np


##################################################################################

'''
1. Array Creation and Basic Operations
'''

# Exercise 1.1: Create a NumPy array from a Python list and perform basic operations.

arr1 = np.array([1,2,3,4,5])
#print(arr1)

arr2 = np.array([[1,2,3], [4,5,6]])
#print(arr2)

range_arr = np.arange(0,10,2)
#print(range_arr)

linspace = np.linspace(0,1,5)
#print(linspace)

identity = np.eye(3)
#print(identity)


'''
2. Array Indexing and Slicing
'''

# Exercise 2.1: Access elements and slices of a NumPy array.

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

#print(arr)
element = arr[1,2]
#print(element)

row_slice = arr[1:3]
#print(row_slice)

col_slice = arr[:,1:3]
#print(col_slice)

## boolean indexing
boold_idx = arr > 5
filtered = arr[boold_idx]
##print(filtered)

##################################################################################

'''
NumPy Problem Set
'''

'''
Given an array of temperatures in Fahrenheit, convert them to Celsius using NumPy's vectorized operations.
'''

# Formula: C = (F - 32) * 5/9
fahrenheit = np.array([32, 68, 86, 104, 122])

celcius = (fahrenheit -32) * 5/9
#print(celcius)

##################################################################################

'''
Problem 2: Array Manipulation
Create a 5x5 array with random integers between 1 and 100, then:

Extract the largest value in each row
Calculate the mean of each column
Replace all values greater than 50 with the value 50
'''

# Create a 5x5 array with random integers between 1 and 100
arr = np.random.randint(1,101, size=(5,5))
#print("Original Array")
#print(arr)

# 1. Extract the largest value in each row
max_in_rows = np.max(arr, axis= 1)
#print("\nMax in each row:",max_in_rows)


# 2. Calculate the mean of each column
mean_of_columns = np.mean(arr,axis=0)
#print("\nMean of each column:" ,mean_of_columns)

# 3. Replace all values greater than 50 with the value 50
bool_idx = arr > 50
arr[bool_idx]=50
#print("\nArray with values capped at 50:")
#print(arr)

##################################################################################

'''
Problem 3: Broadcasting
You have two arrays:

heights = np.array([1.65, 1.75, 1.80, 1.90, 1.60])  # in meters
weights = np.array([70, 80, 85, 90, 65])  # in kg

Calculate the BMI (Body Mass Index) for each person using the formula: BMI = weight / (height^2)

'''
heights = np.array([1.65, 1.75, 1.80, 1.90, 1.60])
weights = np.array([70, 80, 85, 90, 65])

bmi = weights / heights**2
#print(bmi)

##################################################################################

'''
Problem 4:

scores = np.array([85, 90, 75, 95, 65, 70, 88, 92, 78, 80])

Find the mean, median, and standard deviation
Normalize the scores (subtract mean and divide by standard deviation)
Find how many scores are above the mean

'''
scores = np.array([85, 90, 75, 95, 65, 70, 88, 92, 78, 80])

mean_scores = np.mean(scores)
#print(f"mean_scores:{mean_scores}")

std_scores = np.std(scores)
#print(f"standart deviation:{std_scores}")

normalized_scores = (scores - mean_scores) / std_scores
#print(f"Normalized Scores: {normalized_scores}")

idx_scores = scores > mean_scores
upper_mean_scores = scores[idx_scores]
#print(f"Scores above than mean: {upper_mean_scores}")


##################################################################################

'''
Problem 5

Calculate A + B
Calculate the matrix product A @ B
Calculate the determinant of A
Find the inverse of A

'''

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

sum_arrays = A + B
#print(f"sum of arrays: {sum_arrays}")

matrix_product = A @ B
#print(f"product of arrays: {matrix_product}")

det_A = np.linalg.det(A)
#print(f"Determinant of A : {det_A}")

inv_a = np.linalg.inv(A)
#print(f"Inverse of A: {inv_a}")



##################################################################################

'''
Problem 6: Data Analysis with NumPy
You are given a dataset of daily temperatures for a month:

Perform the following analyses:

Calculate the average temperature for each week
Find the hottest day of the month (row and column index)
Calculate the temperature range (max - min) for each week
Create a boolean mask showing days with temperatures above 32°C
Calculate the 7-day moving average of temperatures (hint: use np.convolve)

'''
temperatures = np.array([
    [25, 28, 30, 32, 35, 37, 38],  # Week 1
    [28, 30, 32, 33, 35, 36, 37],  # Week 2
    [26, 29, 31, 33, 34, 35, 36],  # Week 3
    [24, 27, 29, 31, 33, 34, 35]   # Week 4
])

avg_temp_each_week = np.mean(temperatures,axis=1)
#print(f"Average temperature for each week: {avg_temp_each_week}")

hottest_day = np.max(temperatures)
bool_idx  = temperatures == hottest_day
#print(np.where(temperatures == hottest_day))


max_of_each_week = np.max(temperatures,axis=1)
min_of_each_week = np.min(temperatures,axis=1)
temperature_range_each_week = max_of_each_week - min_of_each_week
#print(f"temperature range of each week: {temperature_range_each_week}")


bool_idx = temperatures >32
bool_mask  = (temperatures > 32)
masked_temp = temperatures[bool_idx]

#print(f"temperature boolen mask is: {bool_mask}")
#print(f"temperatue above 32 is: {masked_temp}")


flat_temps = temperatures.flatten()
# Calculate 7-day moving average
# We use 'valid' mode to only get results where the window fully overlaps with the input
window = np.ones(7) / 7  # Create a window of size 7 with equal weights
moving_avg = np.convolve(flat_temps, window, mode='valid')

#print(f"7-day moving average: {moving_avg}")


##################################################################################