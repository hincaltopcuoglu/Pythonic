
'''You have a list of integers. Return the first number that occurs more than once.
If no number repeats, return None'''

def first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None

#print(first_duplicate([3, 1, 4, 1, 5, 3, 2]))

####################################################################

'''Question 2: First Non-Repeating Character
Given a string s, return the first character that appears only once in the string.
If no such character exists, return None.'''

def non_repeating_character(s:str):
    from collections import defaultdict

    counts = defaultdict(int)

    for char in s:
        counts[char] += 1
    
    for char in s:
        if counts[char]==1:
            return char
    
    return None
    

#print(non_repeating_character("statistics"))


####################################################################

'''Question 3: Group Anagrams
Given a list of strings, group the ones that are anagrams of each other.'''

def group_anagrams(words:list[str]) -> list[list[str]]:
    from collections import defaultdict
    anagrams = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        anagrams[key].append(word)

    return list(anagrams.values())


#words = ["bat", "tab", "tap", "pat", "cat", "act"]
#print(group_anagrams(words))

####################################################################

'''
Question 4: Top K Frequent Elements
Given a list of integers nums and an integer k, return the k most frequent elements.
'''
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    from collections import Counter

    counts = Counter(nums)
    top_k = counts.most_common(k)
    return [item[0] for item in top_k]


#print(top_k_frequent([1,1,1,2,2,3], 2))

####################################################################

'''
Question 5: Longest Substring Without Repeating Characters
Given a string s, return the length of the longest substring without repeating characters.
'''
def length_of_longest_unique_substrings(s:str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right- left + 1)

    return max_len

#print(length_of_longest_unique_substrings("abcabcbb"))

#print(length_of_longest_unique_substrings("bbbb"))

####################################################################

'''
Question 6: Minimum Size Subarray Sum
Given an array of positive integers nums and an integer target, return the minimum length of a contiguous subarray of which the sum is greater than or equal to target.
If no such subarray exists, return 0.
'''

def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    total = 0
    min_len = float("inf")

    for right in range(len(nums)):
        total += nums[right]

    while total >= target:
        min_len = min(min_len,right - left + 1)
        total -= nums[left]
        left += 1

    return 0 if min_len == float("inf") else min_len


#print(min_subarray_len(7, [2,3,1,2,4,3]))
#print(min_subarray_len(15, [1,2,3,4,5]))  
#print(min_subarray_len(100, [1,2,3]))     

#################################################################### 

'''
Problem: Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
'''
def length_of_longest_unique_substring(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


#print(length_of_longest_unique_substring("abcabcbb")) 
#print(length_of_longest_unique_substring("pwwkew"))   
#print(length_of_longest_unique_substring("bbbb"))      

#################################################################### 

'''
seeing both the actual substring and its length helps
'''

def longest_unique_substring(s:str) -> tuple[int, str]:
    seen = set()
    left = 0
    max_len= 0
    start_index = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])

        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_index = left
    
    longest_substr = s[start_index: start_index + max_len]
    print(f"longest substring without repeating characters: {longest_substr}")
    print(f"length: {max_len}")
    return max_len, longest_substr

#longest_unique_substring("abcabcbb")
#longest_unique_substring("pwwkew")
#longest_unique_substring("bbbb")


####################################################################

'''
Question: Longest Substring with At Most Two Distinct Characters
Given a string s, return the length of the longest substring that contains at most two distinct characters.
'''

def longest_substring_two_distinct(s:str) -> int:
    from collections import defaultdict

    left = 0
    max_len = 0
    char_count = defaultdict(int)

    for right in range(len(s)):
        char = s[right]
        char_count[char] += 1

         # 🧾 Print before shrinking
        print(f"Window before check: {s[left:right+1]} | char_count: {dict(char_count)}")

        while len(char_count)>2:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left +=1
            print(f"  Shrinking window: {s[left:right+1]} | char_count: {dict(char_count)}")

        # ✅ Update max length AFTER the window is valid
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_index = left  # record where the valid substring starts


    longest_substring = s[start_index:start_index + max_len]

    print(f"Longest valid substring (≤2 distinct): '{longest_substring}'")
    print(f"Length: {max_len}")
    return max_len

print(longest_substring_two_distinct("eceba"))     # Output: 3 ("ece")
print(longest_substring_two_distinct("ccaabbb"))   # Output: 5 ("aabbb")
