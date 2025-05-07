def is_palindrome(s: str) -> bool:
   return s == s[::-1]

#print(is_palindrome("madam"))

#print(is_palindrome("islam"))

#####################################################################

def all_palindromes(s: str) -> list:
   result = []
   for i in range(len(s)):
      for j in range(i+1, len(s)+1):
         substing = s[i:j]
         if is_palindrome(substing):
            result.append(substing)
   return list(set(result))
               

#print(all_palindromes("banana"))

#####################################################################

def longest_palindromic_substring(s:str) -> str:
   def expand_around_center(left:int, right:int) -> str:
      while left>=0 and right< len(s) and s[left]==s[right]:
         left -= 1
         right += 1
      return s[left+1: right]
   
   longest = ""
   for i in range(len(s)):
      substr1 = expand_around_center(i,i)
      substr2 = expand_around_center(i,i+1)

      if len(substr1) > len(longest):
         longest = substr1

      if len(substr2) > len(longest):
         longest = substr2

   return longest

#print(longest_palindromic_substring("bababa"))

#print(longest_palindromic_substring("banana"))

#print(longest_palindromic_substring("baaaaab"))


#####################################################################

def count_palindromic_substrings(s: str) -> int:
   def expand_and_count(left:int, right:int) -> str:
      count = 0
      while left>=0 and right< len(s) and s[left]==s[right]:
         count += 1
         left -= 1
         right += 1
      return count
   
   total = 0
   for i in range(len(s)):
      total += expand_and_count(i,i)
      total += expand_and_count(i, i+1)

   return total

#print(count_palindromic_substrings("babababab"))

#print(count_palindromic_substrings("banana"))

#####################################################################

def count_distinct_palindromic_substrings(s:str) -> int:
   unique_palindromes = set()
   def expand_and_collect(left:int, right:int) -> str:
      while left>=0 and right< len(s) and s[left]==s[right]:
         unique_palindromes.add(s[left: right+1])
         left -= 1
         right += 1
      
   
   for i in range(len(s)):
      expand_and_collect(i,i)
      expand_and_collect(i,i+1)

   return len(unique_palindromes)
         

#print(count_distinct_palindromic_substrings("banana"))

#####################################################################

from collections import defaultdict

def list_palindromic_substrings_with_count(s:str):
   palindrome_counts = defaultdict(int)
   def expand_and_count(left:int, right:int):
      while left>=0 and right< len(s) and s[left]==s[right]:
         substr = s[left:right+1]
         palindrome_counts[substr] +=1
         left -= 1
         right += 1
   
   for i in range(len(s)):
      expand_and_count(i,i)
      expand_and_count(i, i+1)

   for p in sorted(palindrome_counts.keys(), key= lambda x: (-len(x),x)):
      print(f"{p!r} -> {palindrome_counts[p]}")
   
   return len(palindrome_counts)

   
   
#print(list_palindromic_substrings_with_count("banana"))


#####################################################################
def longest_palindromic_subsequence(s: str):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes
    for i in range(n):
        dp[i][i] = 1

    # Fill DP table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # Reconstruct actual subsequence
    i, j = 0, n - 1
    left = []
    right = []

    while i <= j:
        if s[i] == s[j]:
            left.append(s[i])
            if i != j:
                right.append(s[j])
            i += 1
            j -= 1
        elif dp[i + 1][j] >= dp[i][j - 1]:
            i += 1
        else:
            j -= 1

    subseq = ''.join(left + right[::-1])
    return dp[0][n - 1], subseq


#print(longest_palindromic_subsequence("bbbab"))
# ➜ (4, 'bbbb')

#print(longest_palindromic_subsequence("racecar"))
# ➜ (7, 'racecar')

#print(longest_palindromic_subsequence("bbab"))
#####################################################################

#Count All Palindromic Subsequences
def generate_and_count_subsequences(s: str) -> list:
   from collections import defaultdict

   palindrome_cnts = defaultdict(int)
   
   def is_palindrome(s: str) -> bool:
      return s == s[::-1] and s

   result = []

   def backtrack(index, path):
      if index == len(s):
            result.append(''.join(path))
            return
      # include s[index]
      backtrack(index + 1, path + [s[index]])
      # exclude s[index]
      backtrack(index + 1, path)
      

   backtrack(0, [])

   for seq in result:
      if is_palindrome(seq):
         palindrome_cnts[seq] += 1

   return len(palindrome_cnts)



#for s in ["abc", "bccb", "racecar"]:
#   count = generate_and_count_subsequences(s)
#   print(f"Subsequence count for '{s}: {count}")

#####################################################################

# Question : Minimum Insertions to Make a String Palindrome

def min_insertions_to_palindrome(s: str) -> int:
   def longest_palindromic_subsequence(s: str):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes
    for i in range(n):
        dp[i][i] = 1

    # Fill DP table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n-1]
   
   lps_length = longest_palindromic_subsequence(s)

   return len(s)-lps_length

#print(min_insertions_to_palindrome("abcda"))

#####################################################################


#actual constructed palindrome with the minimum insertions?

def construct_min_insert_palindrome(s: str):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Step 1: Build DP table (bottom-up)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

    # Step 2: Reconstruct palindrome using DP
    res = [""] * (n + dp[0][n - 1])
    i, j = 0, n - 1
    left, right = 0, len(res) - 1

    while i <= j:
        if s[i] == s[j]:
            res[left] = s[i]
            res[right] = s[j]
            i += 1
            j -= 1
        elif dp[i + 1][j] < dp[i][j - 1]:
            res[left] = s[i]
            res[right] = s[i]
            i += 1
        else:
            res[left] = s[j]
            res[right] = s[j]
            j -= 1
        left += 1
        right -= 1

    palindrome = ''.join(res)
    print(f"Original string      : {s}")
    print(f"Min insertions needed: {dp[0][n - 1]}")
    print(f"Palindrome formed    : {palindrome}")
    return palindrome



#construct_min_insert_palindrome("abcda")

#####################################################################

#Count Total Distinct LPS

def count_distinct_lps(s: str) -> int:

   def get_lps_length(s: str):
      n = len(s)
      dp = [[0] * n for _ in range(n)]

      # Base case: single characters are palindromes
      for i in range(n):
         dp[i][i] = 1

      # Fill DP table
      for length in range(2, n + 1):
         for i in range(n - length + 1):
               j = i + length - 1
               if s[i] == s[j]:
                  dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
               else:
                  dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

      return dp[0][n-1]
   
   def is_palindrome(s: str) -> bool:
      return s == s[::-1] and len(s)>0

   lps_len = get_lps_length(s)

   result = set()

   def backtrack(index, path):
      if index == len(s):
         candidate = ''.join(path)
         if is_palindrome(candidate) and len(candidate) == lps_len:
            result.add(candidate)
            #print("LPS Found:", candidate)
         return
      # include s[index]
      backtrack(index + 1, path + [s[index]])
      # exclude s[index]
      backtrack(index + 1, path)
      

   backtrack(0, [])

   for lps in sorted(result):
      print("Unique LPS:", lps)


   return len(result)

print("Count:", count_distinct_lps("aabaa"))

print("Count:", count_distinct_lps("aabcaab"))

print("Count:", count_distinct_lps("bbabcbcab"))