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

print(longest_substring_with_k_distinct("eceba",2))