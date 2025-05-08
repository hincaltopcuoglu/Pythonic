import re
from collections import Counter, defaultdict, deque
import math
import heapq
from functools import reduce

'''
Python Fundamentals Question 1:
Write a function that takes a list of integers and returns a new list containing only the even numbers, 
sorted in descending order. Use list comprehension for this task.
'''

def even_num(nums : list[int]) -> list[int]:
    result = sorted([i for i in nums if i%2 == 0], reverse=True)
    return result


##print(even_num([1,2,3,4,5]))

#######################################################################
'''
Python Fundamentals Question 2:
Create a function that counts the frequency of each word in a given string, ignoring case and punctuation. 
Return the result as a dictionary where keys are words and values are their counts.
'''

def word_counts(s:str) -> dict[int]:
    text = s.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

#print(word_counts('Hello world! Hello, Python. World is amazing.'))


#######################################################################
'''
count each letter with counter method
'''

def count_letters(text:str) -> dict:
    text = text.lower()

    letter_counts = Counter(text)

    return dict(letter_counts)

#print(count_letters("Hello World"))



#######################################################################
'''
Python Fundamentals Question 3:
Write a function that takes a file path as input, reads the file, 
and returns the 5 most common words along with their counts. Handle potential file 
not found errors appropriately.

You can use what you've learned from the previous question about word counting, 
combined with error handling for file operations.
'''

def most_common_word(file_path):
    try:    
        with open(file_path, 'r') as file:
        
            text = file.read()
        
        
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        words = text.split()

        word_counts = Counter(words)

        top_5 = word_counts.most_common(5)

        return top_5
    
    except FileNotFoundError:
            return "Error: File not found"
    except Exception as e:
        return f"Error {str(e)}"
    

#print(most_common_word('sample.txt'))


#######################################################################
'''
Python Fundamentals Question 4:
Write a function that takes a list of strings and returns a new list 
containing only the strings that start with a vowel (a, e, i, o, u), 
converted to uppercase. Use list comprehension and lambda functions.
'''

#def vowel_words(s: list[str]) -> list[str]:



#######################################################################

'''
Lambda Practice 1:
Write a lambda function that takes a number and returns its square.
'''

numbers = [1,2,3,4,5]
squarred = list(map(lambda x: x**2, numbers))
#print(squarred)

#######################################################################

'''
Python Fundamentals Question 5:
Create a function that takes a list of dictionaries 
(each containing 'name' and 'age' keys) and returns the names of people who are 18 or older, 
sorted alphabetically.

This is a great opportunity to practice list comprehensions and sorting. Try to solve this one!
'''

# Example data
people_list = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 17},
    {'name': 'Charlie', 'age': 30},
    {'name': 'David', 'age': 16},
    {'name': 'Eve', 'age': 18}
]

def get_adult_names(people_list: list) -> list:
    adult_names = [person['name'] for person in people_list if person['age']>=18]
    sorted_names = sorted(adult_names)
       
    return sorted_names

#print(get_adult_names(people_list))


#######################################################################

'''
Python Fundamentals Question 6:
Write a function that takes a string and returns a dictionary where keys are characters 
and values are their positions (indices) in the string. 
If a character appears multiple times, store all positions in a list.
'''

def char_positions(s:str) -> dict:
    positions = {}

    for index, char in enumerate(s):
        if char in positions:
            positions[char].append(index)
        else:
            positions[char] = [index]

    return positions
    
###print(char_positions("hello"))


#######################################################################


'''
Python Fundamentals Question 7:
Write a function that takes a list of numbers and returns a new list where each element is 
the product of all numbers in the original list except the one at that position.

Example:

Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Think about:

How would you calculate the product of all numbers in a list?
How would you exclude just one number from that calculation?
How would you do this for each position in the list?
'''

def product_numbers(numbers: list[int]) -> list[int]:
    result = []

    for i in range(len(numbers)):
        product = 1
        for j in range(len(numbers)):
            if i != j:
                product *= numbers[j] 
        result.append(product)
    
    return result


#print(product_numbers([1,2,3,4]))



#######################################################################
'''
Python Fundamentals Question 8:
Create a function that takes a list of strings and groups them by their first letter. 
Return a dictionary where keys are first letters and values are lists of words starting with that letter.

Example:

Input: ["apple", "banana", "cherry", "avocado", "blueberry"]
Output: {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
Give this one a try!
'''

def grouping_letters(s: list[str]) -> dict:

    letter_dict = {}

    for word in s:
        first_letter = word[0].lower()
        if first_letter in letter_dict:
            letter_dict[first_letter].append(word)
        else:
            letter_dict[first_letter] = [word]
    return letter_dict


#print(grouping_letters(["apple", "banana", "cherry", "avocado", "blueberry"]))

#######################################################################

'''
Python Fundamentals Question 9:
Write a function that takes a list of integers and returns the second largest number. 
If there is no second largest (e.g., all numbers are the same), return the same as the largest.

Example:

Input: [10, 5, 7, 7, 10, 15, 8]
Output: 10
'''

def second_largest_number(numbers: list[int]) -> int:
    unique_sorted = sorted(set(numbers),reverse=True)

    if len(unique_sorted) == 1:
        return unique_sorted[0]
    
    return unique_sorted[1]


#print(second_largest_number([10, 5, 7, 7, 10, 15, 8]))


#######################################################################

'''
Python Fundamentals Question 10:
Create a function that takes a sentence (string) and returns 
the most frequent word and its count. Ignore case and punctuation.

Example:

Input: "The quick brown fox jumps over the lazy dog. The dog was not very lazy."
'''

def most_frequent_word(text: str) -> tuple:
    
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()

    word_counts = Counter(words)
    most_common_word, count = word_counts.most_common(1)[0]

    return (most_common_word,count)

#print(most_frequent_word("The quick brown fox jumps over the lazy dog. The dog was not very lazy."))


#######################################################################

'''
Python Fundamentals Question 11:
Write a function that takes a list of strings and returns a new list with duplicates 
removed while preserving the original order.

Example:

Input: ["apple", "banana", "apple", "cherry", "banana"]
'''

def remove_duplicates(items : list[str]) -> list[str]:
    unique_items = []

    seen = set()

    for item in items:
        if item not in seen:
            unique_items.append(item)
            seen.add(item)

    return unique_items

#print(remove_duplicates(["apple", "banana", "apple", "cherry", "banana"]))

#######################################################################

'''
Python Fundamentals Question 12:
Write a function that takes two lists and returns a new list containing elements that appear in both lists.

Example:

Input: [1, 2, 3, 4, 5], [4, 5, 6, 7, 8]
'''

def unique_elements(list1 : list[int], list2: list[int]) -> list:
    unique_list = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                unique_list.append(list1[i])
    return unique_list

#print(unique_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))

## or ##

def common_elements(list1: list[int], list2: list[int]) -> list:
    # Convert lists to sets and find the intersection
    common = set(list1) & set(list2)

    # Convert back to a list
    return list(common)

# Test
#print(common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))


#######################################################################

'''
Python Fundamentals Question 13:
Write a function that takes a string and returns True if it's a palindrome 
(reads the same forward and backward), ignoring spaces, punctuation, and case.

Example:

Input: "A man, a plan, a canal: Panama"
'''

def is_palindrome(s:str) -> bool:
    s = s.lower()
    s = re.sub(r'[^a-z0-9]', '', s)

    return s == s[::-1]
    

#print(is_palindrome("A man, a plan, a canal: Panama"))


#######################################################################

'''
Python Fundamentals Question 14:
Create a function that takes a list of integers and returns the longest consecutive sequence length.

Example:

Input: [100, 4, 200, 1, 3, 2]
'''

def longest_consecutive_sequence(numbers: list[int]) -> int:
    if not numbers:
        return 0

    numbers = sorted(numbers)
    current_length = 1
    max_length = 1

    for i in range(1, len(numbers)):
        # Skip duplicates
        if numbers[i] == numbers[i-1]:
            continue

        # Check if current number is consecutive to previous
        if numbers[i] == numbers[i-1] + 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            # Reset current length if sequence breaks
            current_length = 1

    return max_length

# Test
#print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))  # Should output: 4



#######################################################################

'''
Python Fundamentals Question 15:
Write a function that takes a list of numbers and a target number, 
then returns the indices of two numbers that add up to the target.

Example:

Input: [2, 7, 11, 15], target = 9
'''

def added_indices(numbers: list[int], target:int) -> list[int]:
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i,j]
    return []
            

#print(added_indices([2, 7, 11, 15], target = 9))

#######################################################################
'''
Python Fundamentals Question 16:
Write a function that takes a string and returns the first non-repeating character. 
If there is no non-repeating character, return None.

Example:

Input: "stress"
'''
def none_repeating(s:str) -> str :
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

#print(none_repeating("stress"))


#######################################################################
'''
Python Fundamentals Question 17:
Create a function that takes a list of integers and rotates it to the right by k steps.

Example:

Input: [1, 2, 3, 4, 5, 6, 7], k = 3
'''

def rotate_right(number: list[int], k: int) -> list[int]:
    k = k % len(numbers)

    return number[-k:] + number[:-k]

#print(rotate_right([1,2,3,4,5,6,7],k=3))


#######################################################################

'''
Slicing Practice 1:
Write a function that reverses a list using slicing (don't use the reverse() method).

Example:

Input: [1, 2, 3, 4, 5]
'''

def reverse_list(numbers_list: list[int]) -> list[int]:
    numbers_list = numbers_list[::-1]
    return numbers_list

#print(reverse_list([1,2,3,4,5]))


#######################################################################

'''
Slicing Practice 2:
Write a function that returns every second element of a list using slicing.

Example:

Input: [1, 2, 3, 4, 5, 6, 7, 8]

'''

def second_element(numbers: list[int]) -> list[int]:
    second_elements = []
    for i in range(len(numbers)):
        if i%2 != 0:
            second_elements.append(numbers[i])
    return second_elements
        
#print(second_element([1,2,3,4,5,6,7,8]))


#######################################################################

'''
Slicing Practice 3:
Write a function that takes a list and returns a new list with the first and last n elements removed.

Example:

Input: [1, 2, 3, 4, 5, 6, 7, 8], n = 2
'''

def remove_first_last(numbers: list[int], k:int) -> list[int]:
    return numbers[k:-k]

#print(remove_first_last([1,2,3,4,5,6,7,8],k=2))

#######################################################################

'''
Slicing Practice 4:
Write a function that returns the middle element of a list. 
If the list has an even length, return the average of the two middle elements.

Example:

Input: [1, 2, 3, 4, 5]
'''

def middle_element(number: list[int]) -> int:
    length = len(numbers)

    if length %2 != 0:
        return numbers[length // 2]
    else:
        middle_right = length // 2
        middle_left = middle_right -1
        return (numbers[middle_left] + numbers[middle_right]) /2


#print(middle_element([1, 2, 3, 4, 5]))

#######################################################################

'''
Slicing Practice 5:
Write a function that takes a list and returns a new list with elements in chunks of size n.

Example:

Input: [1, 2, 3, 4, 5, 6, 7, 8], n = 3

'''

def chunk(numbers: list[int], n:int) -> list[int]:
    chunked = []
    for i in range(0, len(numbers), n):
        chunk = numbers[i:i+n]
        chunked.append(chunk)
    return chunked

#print(chunk([1, 2, 3, 4, 5, 6, 7, 8], n = 3))

#######################################################################

'''
Slicing Practice 7:
Write a function that takes a list and returns a new list where each element 
is the sum of n consecutive elements from the original list.

Example:

Input: [1, 2, 3, 4, 5, 6, 7, 8], n = 3

'''

def sliding_window_sum(numbers: list[int], n:int) -> list[int]:
    result = []
    for i in range(len(numbers) - n + 1):
        window = numbers[i: i+3]
        window_sum = sum(window)
        result.append(window_sum)
    
    return result

#print(sliding_window_sum([1, 2, 3, 4, 5, 6, 7, 8], n = 3))


#######################################################################

'''
Slicing Practice 8:
Write a function that takes a list and returns a new list where each element is 
the maximum value of non overlapping  sliding window of size n.

Example:

Input: [1, 3, 5, 7, 9, 2, 4, 6, 8], n = 3
'''

def maximum_non_overlap_sliding_window(numbers :list[int], n:int) -> list[int]:
    max_chunked = []
    for i in range(0, len(numbers), n):
        chunked = numbers[i:i+n]
        max_chunked.append(max(chunked))
    return max_chunked

#print(maximum_non_overlap_sliding_window([1, 3, 5, 7, 9, 2, 4, 6, 8], n = 3))


#######################################################################

'''
Slicing Practice 8:
Write a function that takes a list and returns a new list where each element is 
the maximum value in a sliding window of size n.

Example:

Input: [1, 3, 5, 7, 9, 2, 4, 6, 8], n = 3
'''

def overlapping_max_chunk(numbers: list[int], n=int) -> list[int]:
    max_value = []
    for i in range(len(numbers) -n +1):
        window = numbers[i: i+n]
        max_window = max(window)
        max_value.append(max_window)
    return max_value

#print(overlapping_max_chunk([1, 3, 5, 7, 9, 2, 4, 6, 8], n = 3))

#######################################################################

'''
Slicing Practice 9:
Write a function that takes a list and returns a new list 
where each element is the median of a sliding window of size n. 
(For even-sized windows, take the average of the two middle elements.)

Example:

Input: [1, 3, 5, 7, 9, 2, 4, 6, 8], n = 3

'''

def median_sliding_window(numbers: list[int], n:int) -> list[int]:
    result = []

    for i in range(len(numbers) - n + 1):
        window = numbers[i: i+n]
        sorted_window = sorted(window)

        if n % 2 == 1:
            median = sorted_window[n // 2]
        else:
            middle_right = n // 2
            middle_left = middle_right - 1
            median = (sorted_window[middle_left] + sorted_window[middle_right]) / 2
        result.append(median)

    return result

#print(median_sliding_window([1, 3, 5, 7, 9, 2, 4, 6, 8], 3))


#######################################################################

'''
Slicing Practice 10:
Write a function that takes a list and returns a new list 
where each element is the running average of all elements up to that point.

Example:

Input: [2, 4, 6, 8, 10]
'''

def running_slice_average(numbers: list[int]) -> list[int]:
    result = []
    for i in range(len(numbers)):
        current_slice = numbers[:i+1]
        current_avg = sum(current_slice) / len(current_slice)
        result.append(current_avg)
    return result

#print(running_slice_average([2, 4, 6, 8, 10]))

#######################################################################

'''
Slicing Practice 11:
Write a function that takes a list and returns a new list where 
each element is the result of applying a "centered difference" 
calculation (useful in numerical differentiation). 
For each position i, calculate (value at i+1 minus value at i-1) divided by 2. 
For the first and last elements, use the one-sided difference.

Example:

Input: [2, 4, 6, 8, 10]
'''

def centered_difference(numbers: list[int]) -> list[float]:
    result = []
    # handle first element, one sided difference
    if len(numbers) > 1:
        result.append(numbers[1] - numbers[0])

    # handle mid part
    for i in range(1,len(numbers)-1):
        diff = (numbers[i+1] - numbers[i-1]) / 2
        result.append(diff)

    # handle last part
    if len(numbers) > 1:
        result.append(numbers[-1] - numbers[-2])


    return result

#print(centered_difference([2, 4, 6, 8, 10]))

#######################################################################
'''
Slicing Practice 12:
Write a function that takes a list and returns a new list where each element 
is the product of all elements in the original list except the one at that position.

Example:

Input: [1, 2, 3, 4, 5]
Output: [120, 60, 40, 30, 24]
'''

def product_except_self(numbers: list[int]) -> list[int]:
    result = []
    for i in range(len(numbers)):
        elements_before = numbers[:i]
        elements_after = numbers[i+1:]

        elements_except_current = elements_before + elements_after

        product = 1
        for num in elements_except_current:
            product *= num
        
        result.append(product)

    return result

#print(product_except_self([1, 2, 3, 4, 5]))


#######################################################################
'''
Mixed Challenge:
Write a function that takes a list of numbers and returns a new list 
where each element is the range (maximum minus minimum) 
of a sliding window of size 3. For the first and last elements, use a smaller window size.

Example:

Input: [5, 2, 8, 1, 9, 3, 7]
Output: [3, 6, 7, 8, 8, 6]
'''

def sliding_window_range(numbers: list[int], n=3) -> list[int]:
    result = []

    print(f"Input: {numbers}, n={n}, len={len(numbers)}")

    if len(numbers) > 2:
        first_window = numbers[:2]
        result.append(max(first_window)-min(first_window))
        print(f"After first window: {result}")

    for i in range(len(numbers) - n + 1):
        chunk = numbers[i:i+n]
        chunk_range = max(chunk) - min(chunk)
        result.append(chunk_range)
        print(f"After chunk {i}: {result}")

    if len(numbers) >= 2 and n > 2:
        last_window = numbers[-2:]
        result.append(max(last_window) - min(last_window))
        print(f"After last window: {result}")

    return result

# Test
#print("Final result:", sliding_window_range([5, 2, 8, 1, 9, 3, 7], 3))

#######################################################################
'''
Mixed Challenge 2:
Write a function that takes a list of numbers and returns a new list where each element 
is the standard deviation of a sliding window of size 4. 
For windows at the beginning and end that would be smaller than 4, use the available elements.

Standard deviation can be calculated as:

Calculate the mean of the window
Calculate the sum of squared differences from the mean
Divide by the window size
Take the square root
Example:

Input: [2, 4, 6, 8, 10, 12]
Output: [2.0, 2.16, 2.5, 3.0, 3.65, 4.32]
# Explanation: 
# First window: std dev of [2, 4, 6] ≈ 2.0
# Second window: std dev of [2, 4, 6, 8] ≈ 2.16
# Third window: std dev of [4, 6, 8, 10] ≈ 2.5
# Fourth window: std dev of [6, 8, 10, 12] ≈ 3.0
# Fifth window: std dev of [8, 10, 12] ≈ 3.65
# Sixth window: std dev of [10, 12] ≈ 4.32

'''

def calculate_std_dev(numbers: list[int]) -> list[int]:

    mean = sum(numbers) / len(numbers)

    squarred_diff_sum = sum((x-mean) ** 2 for x in numbers)

    std_dev = math.sqrt(squarred_diff_sum / len(numbers))

    return std_dev

def sliding_std_deviation(numbers: list[int], n: int) -> list[int]:
    result = []
    for i in range(len(numbers)):
        start = max(0,i - n + 1)
        end = i + 1

        window = numbers[start:end]

        std_dev = calculate_std_dev(window)
        result.append(std_dev)
    
    return result

#print(sliding_std_deviation([2, 4, 6, 8, 10, 12],n=4))


## or

def sliding_window_std_dev(numbers, window_size=4):
    result = []

    # For each position in the list
    for i in range(len(numbers)):
        # Determine window boundaries
        start = max(0, i - window_size + 1)
        end = i + 1

        # Get the window
        window = numbers[start:end]

        # Calculate standard deviation
        std_dev = calculate_std_dev(window)
        result.append(round(std_dev, 2))

    return result

#print(sliding_window_std_dev([2, 4, 6, 8, 10, 12]))


#######################################################################

'''
Data Processing Challenge:
Write a function that takes a list of daily temperatures and returns a list where each element represents 
how many days you would have to wait until a warmer temperature. If there is no future day with a warmer temperature, 
put 0 instead.

Example:

Input: [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
# Explanation: 
# For 73, the next warmer temperature is 74 (1 day later)
# For 74, the next warmer temperature is 75 (1 day later)
# For 75, the next warmer temperature is 76 (4 days later)
# For 71, the next warmer temperature is 72 (2 days later)
# For 69, the next warmer temperature is 72 (1 day later)
# For 72, the next warmer temperature is 76 (1 day later)
# For 76, there is no warmer temperature in the future
# For 73, there is no warmer temperature in the future
'''

def future_hot_days_temp_diff(numbers: list[int]) -> list[int]:
    result = []
    for i in range(len(numbers) -1):
        if numbers[i] < numbers[i+1]:
            diff = numbers[i+1] - numbers[i]
            result.append(diff)
            i += 1
        else:
            result.append(0)

    return result

#print(future_hot_days_temp_diff([73, 74, 75, 71, 69, 72, 76, 73]))

def daily_temperatures(temparatures: list[int]) -> list[int]:
    result = []

    for i in range(len(temparatures)):
        days_to_wait = 0
        found_warmer = False
        
        for j in range(i+1, len(temparatures)):
            if temparatures[j] > temparatures[i]:
                days_to_wait = j - i
                found_warmer = True
                break


        result.append(days_to_wait)

    return result

# Test
#print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))


#######################################################################
'''
List Comparison Challenge:
Write a function that takes a list of integers and returns a new list 
where each element is the product of all elements in the original list that are greater than the current element.

Example:

Input: [5, 2, 8, 1, 9, 3]
Output: [216, 1080, 135, 1080, 0, 720]
# Explanation: 
# For 5: product of [8, 9] = 72
# For 2: product of [5, 8, 9, 3] = 1080
# For 8: product of [9] = 9
# For 1: product of [5, 2, 8, 9, 3] = 2160
# For 9: product of [] = 0 (no elements greater than 9)
# For 3: product of [5, 8, 9] = 360
'''

def list_comparison_product(numbers: list[int]) -> list[int]:
    result = []

    for i in range(len(numbers)):
        current = numbers[i]
        greater_elements = [num for num in numbers if num > current]

        if greater_elements:
            product = 1
            for num in greater_elements:
                product *= num
            result.append(product)
        else:
            result.append(0)        

    return result

#print(list_comparison_product([5, 2, 8, 1, 9, 3]))

#######################################################################

'''
List Transformation Challenge:
Write a function that takes a list of integers and returns a new list 
where each element is replaced by the sum of its neighbors 
(the elements immediately before and after it). 
For the first and last elements, consider only the one neighbor they have.

Example:

Input: [10, 20, 30, 40, 50]
Output: [20, 40, 60, 80, 40]
# Explanation: 
# For 10: sum of neighbors = 20 (only right neighbor)
# For 20: sum of neighbors = 10 + 30 = 40
# For 30: sum of neighbors = 20 + 40 = 60
# For 40: sum of neighbors = 30 + 50 = 80
# For 50: sum of neighbors = 40 (only left neighbor)
'''

def neigbour_sum(numbers: list[int]) -> list[int]:
    result = []
    for i in range(len(numbers)):
        if i == 0:
            neigbour = numbers[i+1]
        elif i == len(numbers)-1:
            neigbour = numbers[i-1]
        else:
            neigbour = numbers[i-1] + numbers[i+1]
        result.append(neigbour)
    return result

#print(neigbour_sum([10, 20, 30, 40, 50]))


#######################################################################
'''
List Pattern Challenge:
Write a function that takes a list of integers and returns the length of the longest "mountain" subarray.
A mountain is defined as a sequence that increases and then decreases (both strictly). 
A single element or a monotonically increasing/decreasing sequence is not considered a mountain.

Example:

Input: [2, 1, 4, 7, 3, 2, 5]
Output: 5
'''

def list_pattern(numbers: list[int]) -> int:
    if len(numbers) < 3:
        return 0
    
    longest = 0
    i = 1

    while i < len(numbers) - 1:
        is_peak = numbers[i-1] < numbers[i] and numbers[i] > numbers[i+1]

        if not is_peak:
            i += 1
            continue

        left = i - 1
        while left > 0 and numbers[left-1] < numbers[left]:
            left -= 1

        right = i + 1
        while right < len(numbers) -1 and numbers[right]> numbers[right+1]:
            right += 1

        mountain_lenght = right - left + 1

        longest = max(longest,mountain_lenght)

        i = right + 1   

    return longest

#print(list_pattern([2, 1, 4, 7, 3, 2, 5]))


#######################################################################
'''
Exercise 1: List Comprehensions
Write a list comprehension to create a list of all numbers from 1 to 20 that are divisible by 3 or 5.
'''
#print([num for num in range(1,20) if num % 3 == 0 or num % 5 == 0])


#######################################################################
'''
Exercise 2: Lambda Functions
Write a lambda function that takes a string and returns True 
if the string is a palindrome (reads the same forwards and backwards), False otherwise.
'''

def is_palindrome(s:str) -> bool:
    s = s.lower()
    s = re.sub(r'[^\w\s]', '', s)
    if s == s[::-1]:
        return True
    else:
        return False

#print(is_palindrome("radar"))

#or

is_palindrome_v2 = lambda s: s.lower() == s.lower()[::-1]

#print(is_palindrome_v2("radar"))

#or

is_palindrome_v3 = lambda s: re.sub(r'[^\w\s]', '', s.lower()) == re.sub(r'[^\w\s]', '', s.lower())[::-1]

#print(is_palindrome_v3("radarx"))


#######################################################################
'''
Exercise 3: Map Function
Use the map function to convert a list of temperatures in 
Celsius [0, 10, 20, 30, 40] to Fahrenheit. (Formula: F = C * 9/5 + 32)
'''
numbers = [0, 10, 20, 30, 40]
to_fahrenheight = list(map(lambda x : x * 9/5 + 32, numbers))
#print(to_fahrenheight)


#######################################################################
'''
Exercise 4: Filter Function
Use the filter function to get all prime numbers from a list of numbers from 1 to 20.
'''

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
    
        i += 6
    return True
    
prime_numbers = list(filter(is_prime, range(1,21)))
#print(prime_numbers)



#######################################################################

'''
Exercise 5: Combined Concepts
Given a list of words ["hello", "world", "python", "programming", "code"], use a combination of map, filter, and/or lambda 
to create a list containing only words with more than 5 characters, converted to uppercase.
'''

def string_cnt(s:str) -> int:
    if len(s) > 5:
        return s

strings = ["hello", "world", "python", "programming", "code"]

filtered_words = list(filter(lambda s: len(s) > 5, strings))

#print(list(map(lambda s: s.upper(), filtered_words)))

#######################################################################

'''
Dictionary Challenge 1:
Write a function that takes a string and returns a dictionary 
where the keys are the characters in the string 
and the values are the number of times each character appears.

Example:

Input: "hello world"
Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
This is a common interview question that tests your ability to work with dictionaries and count occurrences.
'''

def count_strings(s:str) -> dict:
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

#print(count_strings("hello world")) 


#######################################################################
'''
Dictionary Challenge 2:
Write a function that takes a list of strings and groups anagrams together.
Anagrams are words that have the same characters but in a different order.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
'''

def find_anagrams(words: list[str]) -> list[str]:
    anagram_groups = {}
    for word in words:
        sorted_word = ''.join(sorted(word))

        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    
    return list(anagram_groups.values())

#print(find_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


#######################################################################

'''
Set Challenge:
Write a function that takes two lists and returns a list containing:

Elements that appear in both lists (intersection)
Elements that appear in either list (union)
Elements that appear in the first list but not the second (difference)
Return these as a tuple of three lists.

Example:

Input: [1, 2, 3, 4, 5], [3, 4, 5, 6, 7]
Output: ([3, 4, 5], [1, 2, 3, 4, 5, 6, 7], [1, 2])
'''

def set_operation(list1: list[int], list2: list[int]) -> tuple:
    set1 = set(list1)
    set2 = set(list2)
    intersection = list(set1.intersection(set2))

    union = list(set1.union(set2))

    difference = list(set1.difference(set2))

    return (intersection,union,difference)

#print(set_operation([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

#######################################################################

'''
Dictionary and Set Challenge:
Write a function that takes a list of integers and 
returns the top 3 most frequent elements. If there's a tie, return the smaller number first.

Example:

Input: [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
Output: [4, 1, 2]
# Explanation: 
# 4 appears 4 times
# 1 appears 3 times
# 2 appears 2 times
# 3 appears 1 time
This problem tests your ability to count frequencies using dictionaries and sort based on multiple criteria.
'''

def top_k_elements(numbers: list[int], k: int = 3) -> list[int]:
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] +=1
        else:
            frequency[num] = 1

        sorted_items = sorted(frequency.items() , key=lambda x: (-x[1], x[0]))

        result = [item[0] for item in sorted_items[:k]]

    return result

#print(top_k_elements([1, 1, 1, 2, 2, 3, 4, 4, 4, 4]))



#######################################################################


'''
Tuple Challenge:
Write a function that takes a list of (name, age, score) tuples and returns a new list of names, 
sorted first by age (ascending) and then by score (descending) for people of the same age.

Example:

Input: [("Alice", 20, 88), ("Bob", 20, 92), ("Charlie", 19, 95), ("David", 22, 85)]
Output: ["Charlie", "Bob", "Alice", "David"]
# Explanation: 
# Charlie is youngest (19)
# Bob and Alice are both 20, but Bob has higher score
# David is oldest (22)
'''

def sort_by_age_and_score(people = list[tuple]) -> list[str]:
    # sort the list of tuples by age (ascending) and then by score (descending)
    sorted_people = sorted(people, key= lambda x: (x[1],-x[2]))

    # extract just names from sorted list
    result = [person[0] for person in sorted_people]

    return result


#print(sort_by_age_and_score([("Alice", 20, 88), ("Bob", 20, 92), ("Charlie", 19, 95), ("David", 22, 85)]))



#######################################################################

'''
Nested Data Structure Challenge:
Write a function that processes a list of sales records, 
where each record is a tuple of (product_id, quantity, price). 
The function should return a dictionary with:

The total revenue for each product
The total quantity sold for each product
The average price per unit for each product
Example:

Input: [(101, 3, 10), (102, 2, 15), (101, 5, 12), (103, 1, 20)]
Output: {
    101: {"revenue": 90, "quantity": 8, "average_price": 11.25},
    102: {"revenue": 30, "quantity": 2, "average_price": 15.0},
    103: {"revenue": 20, "quantity": 1, "average_price": 20.0}
}

'''

def process_sales(sales: list[tuple]) -> dict:
    
    # initilize a dictionary to store results
    results = {}
    
    for product_id, quantity, price in sales:
        revenue = quantity * price

        # if this is the first time we're seeing this product, initialize its entry
        if product_id not in results:
            results[product_id] = {
                "revenue":0,
                "quantity":0,
                "average_price":0
            }
    
    
        # Update the product's data
        results[product_id]["revenue"] += revenue
        results[product_id]["quantity"] += quantity
    
    # calculate average price for each product_id
    for product_id in results:
        total_revenue = results[product_id]["revenue"]
        total_quantity = results[product_id]["quantity"]
        results[product_id]["average_price"] = total_revenue / total_quantity

    return results
    

#print(process_sales([(101, 3, 10), (102, 2, 15), (101, 5, 12), (103, 1, 20)]))




#######################################################################

'''
Collections Counter Challenge:
Write a function that takes a list of integers and returns the k most common elements. 
If there's a tie, return the elements in order of their first appearance.

Example:

Input: [1, 1, 1, 2, 2, 3, 3, 3, 4], k=2
Output: [1, 3]

'''

def most_common_elements(numbers: list[int], k: int) -> list[int]:

    counter = Counter(numbers)

    most_common = counter.most_common(k)

    result = [item[0] for item in most_common]

    return result

#print(most_common_elements([1, 1, 1, 2, 2, 3, 3, 3, 4],2))



#######################################################################

'''
DefaultDict Challenge:
Write a function that groups strings by their first letter. 
Return a dictionary where keys are the first letters and values are lists of strings starting with that letter.

Example:

Input: ["apple", "banana", "cherry", "date", "blueberry", "avocado"]
Output: {
    'a': ['apple', 'avocado'],
    'b': ['banana', 'blueberry'],
    'c': ['cherry'],
    'd': ['date']
}

'''

def group_by_first_letter(words: list[str]) -> dict:

    grouped = defaultdict(list)

    for word in words:
        first_letter = word[0]
        grouped[first_letter].append(word)

    return (grouped)

#print(group_by_first_letter(["apple", "banana", "cherry", "date", "blueberry", "avocado"]))



#######################################################################
'''
Simple Sliding Window Solution:

'''

def max_sliding_window_simple(nums: list[int], k:int) -> list[int]:
    result = []

    # for each window position
    for i in range(len(nums) -k + 1):
        window = nums[i:i+k]
        max_val = max(window)
        result.append(max_val)

    return result


#print(max_sliding_window_simple([1, 3, -1, -3, 5, 3, 6, 7], 3))


#######################################################################

'''
Deque Challenge:
Implement a function that finds the maximum value in each sliding window of size k in an array.

Example:

Input: [1, 3, -1, -3, 5, 3, 6, 7], k=3
Output: [3, 3, 5, 5, 6, 7]
'''

def max_sliding_window(numbers: list[int], k:int) -> list[int]:
    result = []
    window = deque() # will store indices, not values

    for i, num in enumerate(numbers):
        # remove elements outside the current window
        while window and window[0] <= i - k:
            window.popleft()

        # remove elements smaller than the current element
        while window and numbers[window[-1]] < num:
            window.pop()

        # add current element's index
        window.append(i)

        # if we've processed at least k elements, add the maximum to result
        if i >= k-1:
            result.append(numbers[window[0]])
    return result

##print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))


#######################################################################

'''
Pattern 1: Fixed-size window
'''


def fixed_window(arr, k):
    result = []
    for i in range(len(arr) - k + 1):
        # Process window arr[i:i+k]
        window_result = process_window(arr[i:i+k])
        result.append(window_result)
    return result


'''
Let's implement a complete example for Pattern 1 (Fixed-size window):

Example: Calculate the average of each window of size k in an array
'''

def average_fixed_window(numbers:list[int], k:int) -> list:
    result = []
    for i in range(len(numbers) - k + 1):
        avg_window = sum(numbers[i:i+k]) / k
        result.append(avg_window)

    return result

#print(average_fixed_window([1, 3, 5, 7, 9, 2, 4],3)) # this is O(n*k)

# lets write it in O(n) optimized

def average_fixed_window_optimized(numbers:list[int], k:int) -> list:
    result = []

    # calculate sum of first window
    window_sum = sum(numbers[:k])
    result.append(window_sum / k)


    # use sliding window to calculate remaining averages
    for i in range(len(numbers) - k):
        # remove the element going out of the window
        window_sum -= numbers[i]

        # add the element coming into the window
        window_sum += numbers[i+k]

        # calculate average
        result.append(window_sum / k)
    
    return result

#print(average_fixed_window_optimized([1, 3, 5, 7, 9, 2, 4],3)) # this is O(n) approach.



#######################################################################

'''
Let's implement Pattern 2: Variable-size window with a condition.

Example: Find the smallest subarray with a sum greater than or equal to a target value
This is a classic variable-size window problem where we expand the window until we meet a condition, 
then shrink it to find the minimum size.
'''

def variable_size_window(numbers:list[int], target:int):
    min_length = float("inf")
    window_sum = 0
    left = 0

    for right in range(len(numbers)):
        # expand the window by including numbers[right]
        window_sum += numbers[right]

        # shrink window from left until condition is no longer met
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)

            # remove left most element from window
            window_sum -= numbers[left]
            left +=1

    # return 0 if no valid subarray found
    return min_length if min_length != float('inf') else 0

#print(variable_size_window([2, 1, 5, 2, 3, 2],7))


#######################################################################

'''
Let's try another example for Pattern 2 (variable-size window):

Example: Longest Substring with At Most K Distinct Characters
In this problem, we need to find the length of the longest substring that contains at most K distinct characters.

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring "ece" has length 3 with 2 distinct characters.
'''

def longest_substring_with_k_distinct(text:str,k:int) -> int:

    if not text or k == 0:
        return 0
    
    char_count = {}
    max_length = 0
    left = 0

    for right in range(len(text)):
        right_char = text[right]
        char_count[right_char] = char_count.get(right_char,0) + 1

        # shrink window from left until we have at most k distinct characcters
        while len(char_count) > k:
            left_char = text[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        # update maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

#print(longest_substring_with_k_distinct("eceba",2))



#######################################################################

'''
Let's explore Pattern 3: Sliding window with deque for finding maximum/minimum values.

Example: Maximum of All Subarrays of Size K
Given an array and an integer k, find the maximum element in each sliding window of size k.

Input: [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
'''

def max_sliding_windows(nums: list[int], k:int) -> list[int]:
    result = []
    window = deque() # will store indices, not values

    for i, num in enumerate(nums):
        # remove elements outside the current window
        while window and window[0] <= i - k:
            window.popleft()


        # remove samller elements from the back of the deque
        # they can never be the maximum in the current window
        while window and nums[window[-1]] < num:
            window.pop()

        # add current element's index
        window.append(i)

        # if we've processed at k elements, add the maximum to the result
        if i >= k -1:
            result.append(nums[window[0]])

    return result

#print(max_sliding_windows([1, 3, -1, -3, 5, 3, 6, 7], k = 3))


#######################################################################

'''
Let's try another example with deque: finding the minimum value in each sliding window.

Example: Minimum of All Subarrays of Size K
Given an array and an integer k, find the minimum element in each sliding window of size k.

Input: [2, 1, 4, 5, 3, 7, 1, 2], k = 3
Output: [1, 1, 3, 3, 1, 1]
'''

def min_sliding_windows(nums: list[int], k:int) -> list[int]:
    result = []
    window = deque()

    for i, num in enumerate(nums):
        while window and window[0] <= i - k:
            window.popleft()

        while window and nums[window[-1]] > num:
            window.pop()

        window.append(i)

        if i >=k -1:
            result.append(nums[window[0]])

    return result

#print(min_sliding_windows([2, 1, 4, 5, 3, 7, 1, 2], k = 3))


#######################################################################

'''
Let's try another example with deque: finding the median in each sliding window.

Example: Median of All Subarrays of Size K
Given an array and an integer k, find the median element in each sliding window of size k.

Input: [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1, -1, -1, 3, 5, 6]
This is more complex than finding min/max, as we need to maintain the elements in sorted order. 
We'll use two deques to track the smaller and larger halves of the window

'''

def median_sliding_window(nums:list[int], k:int) -> list[int]:
    result = []

    # for odd k, we want (k+1)/2 elements in the smaller half
    # for even k, we want k/2 elements in each half
    smaller_half_size = (k + 1) // 2

    # use a list to store the current window
    current_window = []

    for i in range(len(nums)):
        # add the current element to our window
        current_window.append(nums[i])

        # if we have more than k elements, remove the oldest one
        if len(current_window) > k:
            current_window.pop(0)

        # if we have a complete window, find the median
        if len(current_window) == k:
            sorted_window = sorted(current_window)

            # for odd k, the median is the middle element
            if k % 2 == 1:
                result.append(sorted_window[k // 2])
            # for even k, the median is the average of the two middle elements
            else:
                result.append((sorted_window[k // 2 - 1] + sorted_window[k // 2])/2)

    return result

#print(median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], k = 3))



#######################################################################

'''
1. Lists and List Comprehensions
'''

# Exercise 1.1: Create a list of squares for numbers from 1 to 10 using a list comprehension.

#print(list(map(lambda x: x*x ,range(1,10))))

# Exercise 1.2: Given a list of strings, create a new list containing only strings with more than 5 characters.

strings = ['Hello There','adad','dskfmds']

#print(list(filter(lambda s: len(s)>5,  strings )))

# Exercise 1.3: Flatten a list of lists into a single list using a list comprehension.

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#print(list(val for sublist in nested_list for val in sublist))



#######################################################################

'''
2. Dictionaries
'''

# Exercise 2.1: Count the frequency of each character in a string using a dictionary.
# Input: "hello world"

#string = "hello world"
#print(Counter(string))

# Exercise 2.2: Merge two dictionaries into one.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)

#print(dict1)

# Exercise 2.3: Create a dictionary where keys are numbers from 1 to 10 and values are their cubes.

dct = {}

for i in range(1,11):
    dct[i] = i**3

#print(dct)




#######################################################################

'''
3. Sets
'''

# Exercise 3.1: Find common elements between two lists using sets.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

#print(set(list1).intersection(list2))

# Exercise 3.2: Remove duplicates from a list while preserving order.

input_list = [1, 2, 3, 1, 2, 4, 5, 4, 6]
# Expected output: [1, 2, 3, 4, 5, 6]

#print(list(dict.fromkeys(input_list)))

# Exercise 3.3: Check if a string contains all the vowels using sets.

# Example: "sequoia" contains 'a', 'e', 'i', 'o', 'u'

# string = "sequoia"

def contains_all_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return vowels.issubset(set(s.lower()))

#print(contains_all_vowels(string))


#######################################################################

'''
4. Lambda Functions, Map, Filter, Reduce
'''

# Exercise 4.1: Use filter and a lambda function to get all even numbers from a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected output: [2, 4, 6, 8, 10]

#print(list(filter(lambda x: x % 2 == 0, numbers)))


# Exercise 4.2: Use map to convert a list of temperatures from Celsius to Fahrenheit.

celsius = [0, 10, 20, 30, 40]
# Formula: F = C * 9/5 + 32
# Expected output: [32.0, 50.0, 68.0, 86.0, 104.0]

#print(list(map(lambda x: x * 9/5 + 32, celsius)))


# Exercise 4.3: Use reduce to find the product of all numbers in a list.

numbers = [1, 2, 3, 4, 5]
# Expected output: 120

product = reduce(lambda x,y: x*y, numbers)
#print(product)




#######################################################################

'''
5. Combining Concepts
'''

# Exercise 5.1: Given a list of dictionaries representing people (with 'name' and 'age' keys), find the average age.

people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 40}
]
# Expected output: 32.5


ages = [person['age'] for person in people]

# calculate average
average_age = sum(ages) / len(ages)

#print(average_age)

# or 
#print(sum(map(lambda person: person['age'], people))/len(people))

# or 
average_age_v2 = sum(person['age'] for person in people) / len(people)
#print(average_age_v2)



# Exercise 5.2: Create a function that takes a sentence and returns a dictionary with words as keys and their lengths as values.

#string =  "The quick brown fox"
# Expected output: {'The': 3, 'quick': 5, 'brown': 5, 'fox': 3}

def word_cnts(s:str) -> dict:
    dct = {}
    for word in s.split():
        dct[word] = len(word)
    return dct
    

#print(word_cnts(string))

# or 

def word_lenghts(sentence):
    words = sentence.split()
    return dict(zip(words, map(len,words)))

#print(word_lenghts(string))



# Exercise 5.3: Given a list of numbers, create a new list where each element is the sum of itself and all previous elements.

nums = [1, 2, 3, 4, 5]
#Expected output: [1, 3, 6, 10, 15]

def running_sum(numbers):
    result = []
    current_sum = 0

    for num in numbers:
        current_sum += num
        result.append(current_sum)
    
    return result

#print(running_sum(nums))


