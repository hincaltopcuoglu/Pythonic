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

print(median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], k = 3))