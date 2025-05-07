import re
from collections import Counter
import math

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
Write a function that takes a list of integers and returns the top 3 most frequent elements. If there's a tie, return the smaller number first.

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