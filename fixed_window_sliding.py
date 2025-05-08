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

print(average_fixed_window_optimized([1, 3, 5, 7, 9, 2, 4],3)) # this is O(n) approach.