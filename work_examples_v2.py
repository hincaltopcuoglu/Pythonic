'''
1. Efficient Data Processing
Problem: Given a large list of numbers, find the k most frequent elements.
'''

from collections import Counter,defaultdict
import pandas as pd
import numpy as np
import re

numbers = [1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,5,6,7,8]

def top_k_frequentv1(nums: list[int], k:[int]) -> tuple:
    top_k_elements = Counter(nums)
    return top_k_elements.most_common(k)

#print(top_k_frequentv1(numbers,3))



def top_k_frequentv2(nums: list[int], k:[int]) -> list[int]:
    counter = Counter(nums)
    sorted_elements = sorted(counter.items(), key=lambda x: x[1],reverse=True)
    return [item[0] for item in sorted_elements[:k]]

#print(top_k_frequentv2(numbers,3))

########################################################################################################

'''
2. String Manipulation
Problem: Parse a CSV string into a structured format.
'''

def parse_csv(csv_string):
    """
    Parse a CSV string into a list of dictionaries.

    Args:
        csv_string: String in CSV format with header row

    Returns:
        List of dictionaries where keys are column names and values are row values
    """

    # split the string into lines
    lines = csv_string.strip().split("\n")

    # extraxt headers from the first lie
    headers = lines[0].split(',')

    # initialize result list
    result = []

    # process each data row
    for i in range(1,len(lines)):
        values = lines[i].split(',')
        row_dict = {}

        for j in range(len(headers)):
            row_dict[headers[j]] = values[j]
        
        result.append(row_dict)
    
    return result

#print(parse_csv(csv_string = """name,age,city
#John,30,New York
#Alice,25,Boston
#Bob,35,Chicago"""))




########################################################################################################

'''
3. Dictionary Operations
Problem: Implement a function to merge multiple dictionaries, summing values for common keys.
'''

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd':1}
dict2 = {'b': 3, 'c': 4, 'd': 5, 'e':2}
dict3 = {'c': 1, 'd': 2, 'e': 3, 'c':4, 'f':5}

def merge_dicts_with_sum(*dicts):
    """
    Merge multiple dictionaries, summing values for common keys.

    Args:
        *dicts: Variable number of dictionaries

    Returns:
        A new dictionary with combined keys and summed values

    Example input:
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    dict3 = {'c': 1, 'd': 2, 'e': 3}

    Expected output:
    {'a': 1, 'b': 5, 'c': 8, 'd': 7, 'e': 3}

    """
    
    merged = defaultdict(int)
    for d in dicts:
        for key,value in d.items():
            merged[key] += value

    merged = dict(merged)
    return merged
    
   

#print(merge_dicts_with_sum(dict1,dict2,dict3))


########################################################################################################

'''
4. Efficient Searching
Problem: Implement a binary search function for a sorted list.
'''

def binary_search(arrx, target):
    """
    Perform binary search on a sorted array.

    Args:
        arr: Sorted list of numbers
        target: Value to find

    Returns:
        Index of target if found, -1 otherwise
    """
    left = 0

    
    right = len(arrx) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is present at mid
        if arrx[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arrx[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target is not present in the array
    return -1



#arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]

#print(binary_search(arr,6))
#print(binary_search(arr,5))


########################################################################################################


"""
5. Data Transformation
Problem: Implement a function that flattens a nested list.
"""

nested = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]]

def flatten_list(nested_list):
    """
    Flatten a nested list of arbitrary depth.

    Args:
        nested_list: A list that may contain other lists

    Returns:
        A flattened list containing all elements
    """
    
    flattaned = []
    for item in nested_list:
        if isinstance(item,list):
            flattaned.extend(flatten_list(item))
        else:
            flattaned.append(item)

    return flattaned


#print(flatten_list(nested))



########################################################################################################
"""
Problem 6: Finding Pairs with a Target Sum
Problem: Given an array of integers and a target sum, find all pairs of integers in the array that add up to the target sum.
"""

def find_pairs_brute_force(numbers, target_sum):
    """
    Find all pairs of numbers that add up to the target sum using brute force.

    Time Complexity: O(n²)
    Space Complexity: O(n) for the result
    """
    result = []
    # Use a set to avoid duplicate pairs
    seen_pairs = set()

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):  # Start from i+1 to avoid duplicates
            if numbers[i] + numbers[j] == target_sum:
                # Sort the pair to ensure consistent ordering
                pair = tuple(sorted((numbers[i], numbers[j])))
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    result.append(pair)

    return result


numbers = [2, 7, 11, 15, 3, 6, 8, 10, 4, 5]
target = 9

#print(find_pairs_brute_force(numbers,target))

## or hash map approach

def find_pairs(numbers, target_sum):
    """
    Find all pairs of numbers that add up to the target sum using a hash map.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    result = []
    seen_numbers = {}  # Value -> Index
    seen_pairs = set()  # To avoid duplicate pairs
    for i, num in enumerate(numbers):
        complement = target_sum - num

        if complement in seen_numbers:
            pair = tuple(sorted((num,complement)))
            if pair not in seen_pairs:
                seen_pairs.add(pair)
                result.append(pair)

        seen_numbers[num] = i

    return result

#print(find_pairs(numbers,target))


########################################################################################################
"""
Problem 7: Implementing a Queue using Stacks
Problem: Implement a Queue data structure using two Stacks. The Queue should support the standard operations: enqueue, dequeue, and peek.
"""

class QueueUsingStacks:
    """
    A Queue implementation using two stacks.

    A queue follows First-In-First-Out (FIFO) principle, while
    a stack follows Last-In-First-Out (LIFO). This implementation
    uses two stacks to simulate FIFO behavior.
    """

    def __init__(self):
        """Initialize the queue with two empty stacks."""
        
        self.stack1 = [] # for enqueue operations
        self.stack2 = [] # for dequeue operations

    def enqueue(self, item):
        """
        Add an item to the back of the queue.

        Args:
            item: The item to add to the queue
        """
    
        self.stack1.append(item)

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.

        Returns:
            The item at the front of the queue

        Raises:
            IndexError: If the queue is empty
        """
        
        # if stack2 is empty, transfer all elements from stack1
        if not self.stack2:
            # transfer all items from stack1 to stack2, reversing their order
            while self.stack1:
                self.stack2.apend(self.stack1.pop())
        
        # if stack2 still empty, the queue is empty
        if not self.stack2:
            raise IndexError("Queue is empty")
        
        # return the top item from stack2
        return self.stack2.pop()


    def peek(self):
        """
        Return the item at the front of the queue without removing it.

        Returns:
            The item at the front of the queue

        Raises:
            IndexError: If the queue is empty
        """
        
        # If stack2 is empty, transfer all elements from stack1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # If stack2 is still empty, the queue is empty
        if not self.stack2:
            raise IndexError("Queue is empty")

        # Return the top item from stack2 without removing it
        return self.stack2[-1]
    

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise
        """
        
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def size(self):
        """
        Return the number of items in the queue.

        Returns:
            The number of items in the queue
        """
        
        return len(self.stack1) + len(self.stack2)
    

#queue = QueueUsingStacks()
#queue.enqueue(1)
#queue.enqueue(2)
#queue.enqueue(3)

#print(queue.peek())  # Should print 1
#print(queue.dequeue())  # Should print 1
#print(queue.dequeue())  # Should print 2
#print(queue.size())  # Should print 1





########################################################################################################
"""
Object-Oriented Programming for Data Scientists - Step by Step
"""

"""

Example 1: Dataset Class
Aim:
Create a class that represents a dataset with features and target variables, providing basic functionality like 
describing the dataset and splitting it into training and testing sets.

Why it's useful for data scientists:
Encapsulates data and related operations in one place
Provides a consistent interface for working with different datasets
Makes code more organized and reusable
Key methods to implement:
__init__(self, data, target=None): Initialize with data and optional target
describe(self): Print basic statistics about the dataset
split(self, test_size=0.2, random_state=None): Split into training and testing sets

"""

class Dataset:
    """A simple class to handle dataset operations"""
    def __init__(self,data,target=None):
        """
        Initialize a dataset with features and optional target

        Args:
            data: Feature data (list or numpy array)
            target: Target values (list or numpy array)
        """
        self.data = data
        self.target = target
        self.n_samples = len(data)
        self.n_features = len(data[0]) if self.n_samples > 0 else 0

    def describe(self):
        """Print basic statistics about the dataset"""
        print(f"Dataset with {self.n_samples} samples and {self.n_features} features")
        if self.target is not None:
            print(f"Target variable present with {len(self.target)} values")

    def split(self, test_size = 0.2, random_state=None, time_based=False):
        """
        Split the dataset into training and testing sets.

        Args:
            test_size: Proportion of the dataset to include in the test split
            random_state: Seed for random number generator

        Returns:
            train_data, test_data, train_target, test_target
        """

        import numpy as np
            
        if random_state is not None:
            np.random.seed(random_state)

            
        test_count = int(self.n_samples * test_size)
            
        if time_based:
            # time series split - earlier data for training and later for testing
            train_indices = list(range(self.n_samples-test_count))
            test_indices = list(range(self.n_samples-test_count, self.n_samples))
        else:
            indices = np.random.permutation(self.n_samples)
            test_indices = indices[:test_count]
            train_indices = indices[:test_count:]


        train_data = [self.data[i] for i in train_indices]
        test_data = [self.data[i] for i in test_indices]
                
        if self.target is not None:
            train_target = [self.target[i] for i in train_indices]
            test_target = [self.target[i] for i in test_indices]
            return train_data, test_data, train_target, test_target
            
        return train_data, test_data
        

# Create a simple dataset
#X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
#y = np.array([0, 1, 0, 1, 0])

# Create a Dataset instance
#dataset = Dataset(X, y)

# Describe the dataset
#dataset.describe()

# Split the dataset
#train_X, test_X, train_y, test_y = dataset.split(test_size=0.4, random_state=42)

#print("\nTraining data shape:", np.array(train_X).shape)
#print("Testing data shape:", np.array(test_X).shape)
#print("Training target shape:", np.array(train_y).shape)
#print("Testing target shape:", np.array(test_y).shape)


############################################################################################



def LongestWord(sen):
    # Remove punctuation using regex: keep letters, numbers, and spaces
    cleaned = re.sub(r'[^\w\s]', '', sen)
    words = cleaned.split()

    longest_word = ""
    max_length = 0

    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    return longest_word

print(LongestWord("fun&!! time"))