from collections import Counter, defaultdict
import numpy as np



# Reverse a string: "hello" → "olleh"
def reverse_string(s: str) -> str:
    return s[::-1]

#print(reverse_string("hello"))



#Count character frequency in a string
def count_char(s: str) -> dict:
    return Counter(s)

#print(count_char('hello'))


#Find unique elements in a list
def unique_elements(nums: list[int]) -> list[int]:
    return list(set(nums))

#print(unique_elements([1, 2, 2, 3, 4, 4]))


#Merge two dictionaries
def merge_dict(dict1,dict2):
    dict_all = dict1 | dict2
    return dict_all

#d1 = {'a': 1}
#d2 = {'b': 2}

#print(merge_dict(d1,d2))

#numbers = [1, 2, 2, 3, 4, 4]

# Use list comprehension to filter even numbers from a list
def filter_even_nums(nums:list[int]) -> list[int]:
    return [num for num in nums if num % 2 == 0]

#print(filter_even_nums(numbers))


###############################################################################
"""
Example 1: Fixed-size sliding window
Problem: Find the maximum sum of any contiguous subarray of size k.
"""
#arr = [2, 1, 5, 1, 3, 2]
#k = 3

def max_sum_subarray(arr: list[int], k:int) -> int:
    if len(arr) < 0:
        return 0 # handle error
    
    window_sum = sum(arr[:k]) # sum of the first window
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k] #slide window: add new, remove old
        max_sum = max(max_sum,window_sum)
    
    return max_sum

#print(max_sum_subarray(arr,3))




"""
Problem: Length of the longest substring without repeating characters
"""
#s = "abcabcbb"

def length_of_longest_substring(s: str) -> int:

    seen = set()
    left = 0
    max_lenght = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left +=1
        seen.add(s[right])
        max_lenght = max(max_lenght, right - left + 1)
            
    return max_lenght

#print(length_of_longest_substring(s))




"""
Example Problem: Given a sorted array, find if there exists two numbers that add up to a target sum.
"""

#arr = [1, 2, 3, 4, 6]
#target = 6

def has_pair_with_sum(arr: list[int], target: int) -> bool:
    
    left = 0
    right = len(arr) -1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True, arr[left], arr[right]
        elif current_sum<target:
            left +=1
        else:
            right -= 1
    return False 
    

#print(has_pair_with_sum(arr,target))




"""
Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
"""
#nums = [2, 7, 11, 15]
#target = 9

def two_sum(arr: list[int], target: int) -> list[int]:
    seen = {}

    for i , num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


#print(two_sum(nums,target))






"""
Sliding Window Question
Problem: Find the length of the longest subarray with sum less than or equal to k
"""
#arr = [2, 1, 5, 2, 8]
#k = 7

def longest_subarray_with_sum_at_most_k(arr: list[int], k: int) -> int:
    start = 0
    end = 0
    window_sum = 0
    max_length = 0
    max_start = 0

    for end in range(len(arr)):
        window_sum += arr[end]
        while window_sum > k:
            window_sum -= arr[start]
            start +=1
        
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length
            max_start = start

        max_length = max(max_length, end - start + 1)

    return max_length, end, start


#print(longest_subarray_with_sum_at_most_k(arr,k))

 




""""
Question 1: Sliding Window
Problem: Find the maximum length of a subarray with at most k distinct integers.
"""
#arr = [1, 2, 1, 2, 3]
#k = 2

def max_subarray_with_k_distinct(arr: list[int], k: int) -> int:
    count = defaultdict(int)
    left = 0
    max_length = 0

    for right in range(len(arr)):
        count[arr[right]] += 1

        while len(count)>k:
            count[arr[left]] -=1
            if count[arr[left]] == 0:
                del count[arr[left]]
            left += 1

        max_length = max(max_length, right - left + 1)
    
    return max_length


#print(max_subarray_with_k_distinct(arr,k))




"""
Question 2: Two Pointers
Problem: Given a sorted array, remove duplicates in-place such that each element appears only once and return the new length.
"""
#nums = [1, 1, 2]

def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


#print(remove_duplicates(nums))



"""
Exercise 1: Normalize a 2D array (zero mean, unit variance per column)
"""
def normalize_columns(arr: np.ndarray) -> np.ndarray:
    means = []
    variances = []
    for i in range(len(arr)):
        means.append(np.mean(arr[i]))
        variances.append(np.var(arr[i]))
    return means, variances

#arr = np.array([[1, 2], [3, 4], [5, 6]])

#print(normalize_columns(arr))



"""
Exercise 2: Given two arrays, find the indices where elements are equal
"""
#a = np.array([1, 2, 3, 4])
#b = np.array([2, 2, 3, 5])

def find_indices(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    return np.where(a==b)[0]

#print(find_indices(a,b))


"""
Exercise 3: Pairwise Euclidean distance matrix
"""
def pairwise_distances(X: np.ndarray) -> np.ndarray:
    # Using broadcasting
    diff = X[:, np.newaxis, :] - X[np.newaxis, :, :]
    dist_matrix = np.sqrt(np.sum(diff ** 2, axis=-1))
    return dist_matrix



#X = np.array([[0, 0], [1, 0], [0, 1]])
#print(pairwise_distances(X))


########################################################

import numpy as np

# Load data as strings (no header)
data = np.genfromtxt('iris.csv', delimiter=',', dtype=str)

# Extract features and species
features = data[:, :4].astype(float)  # first 4 columns are features
species = data[:, 4]                  # last column is species

# sepal_width is the second column (index 1)
sepal_width = features[:, 1]

# Unique species
unique_species = np.unique(species)

# Compute mean sepal_width per species
means = {}
for sp in unique_species:
    means[sp] = np.mean(sepal_width[species == sp])

print(means)