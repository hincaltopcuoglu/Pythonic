import numpy as np
from collections import Counter
from statistics import mean
from itertools import product

"""
Q-1 : Find the sum of even and odd numners splitted in a range (1,100)
"""


def sum_even_odd() -> tuple:
    even_numbers = 0
    odd_numbers = 0
    for i in range(1,101):
        if i % 2 == 0:
            even_numbers +=i
        else:
            odd_numbers +=i
    return f" sum of even numbers : {even_numbers} , sum of odd numbers {odd_numbers}"


#print(sum_even_odd())


############################################################################################

"""
Q-2 : given a three-figure number, find the unit digit, tens digit, hundred digit 
"""

def split_digits(num:int):
    hundreds = (num // 100)
    tens = (num //10) % 10
    units = num % 10
    return f"hundreds is : {hundreds}, tens is : {tens}, units is :  {units}"

#print(split_digits(num=123))

############################################################################################

"""
Q-3 : check the given input is square number
"""
def is_square_num(num:int):
    if num < 0:
        return f"{num} is not a square number (negative number)"
    root = int(num ** 0.5)
    if root * root == num:
        return f"{num} is square number" 
    else:
        return f"{num} is not square number" 
    
#print(is_square_num(16))
#print(is_square_num(20))
#print(is_square_num(31))
#print(is_square_num(36))


############################################################################################

"""
Q-4 : given user input in sequence 10 arbitrary numbers and one desired number find the nearest number to desired number
"""

def find_desired_number(des:int):
    # Ask user to input 10 numbers separated by spaces
    user_input = input("Enter 10 numbers separated by spaces: ")
    print(f"Desired number is {des}")

    diff = {}
    numbers = list(map(int, user_input.split()))
    if len(numbers)!=10:
        print("Please enter exactly 10 numbers")
        return []
    else:
        for num in numbers:
            if des > num:
                diff[num] =  des - num
            else:
                diff[num] = int(np.abs(num - des))

    return  [key for key, value in diff.items() if value == min(diff.values())]


#print(find_desired_number(9))
#print(find_desired_number(5))


############################################################################################

"""
Q-5 : find the how many numbers are there which ranges between 1 and 100 and its squre + 1 / 5 is zero
"""
def num_occur():
    count = 0
    for i in range(1,101):
        if ((i ** 2) + 1) %5 == 0:
            count += 1
   
    return count

### print(num_occur())

############################################################################################

"""
Q-6 : (Number compression example) Write a function that, given an integer between 1 and 100, allows reaching that number by entering numbers within this range.
"""

def number_compression(des:int) -> int:
    # Get user input with prompt
    user_input = int(input("Enter a number between 1 and 100: "))
    if user_input == des:
        return "You find the number"
    elif user_input < des:
        diff = des - user_input
        return f"Difference is {diff} You should input greater value"
    else:
        diff = user_input - des 
        return f"Different is {diff} You should input lesser value"


#print(number_compression(9))



############################################################################################

"""
Q-7 : Find the multiplication of all integer numbers between 1 and 10
"""

def multip() -> int:
    mult = 1
    for i in range(1,11):
        mult *= i
    return mult

#print(multip())

############################################################################################

"""
Q-8 : find the prime numbers between 10 and 100
"""

def is_prime(n:int) -> bool:
    if n<2:
        return False
    for  i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def find_prime() -> list[int]:
    primes = []
    for i in range(10,101):
        if is_prime(i):
            primes.append(i)
    return primes
    

#print(find_prime())

############################################################################################


"""
Q-9 : Write a function that takes the average of 10 randomly entered integers in sequence, 
then finds the average of the largest and smallest of these numbers, and returns the difference between these two averages.
"""

def find_mean_diff() -> int:
    user_input = input("Enter 10 numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    mean_lst = np.mean(numbers)
    min_lst = np.min(numbers)
    max_lst = np.max(numbers)
    min_max_mean = (max_lst + min_lst) / 2
    diff = np.abs(mean_lst - min_max_mean)
    return diff

#print(find_mean_diff())

############################################################################################

"""
Q-10 : Write a function that, given a 4-digit integer, finds the difference between the remainder obtained by dividing the digit in the hundreds place by 3 and the digit in the units place of the same number.
"""

def find_digit_diff() -> int:
    user_input = int(input("Enter a four digit number:"))
    hundereds = user_input % 1000
    val = (hundereds % 3)
    tens = hundereds % 100
    units = tens % 10

    return val - units

#print(find_digit_diff())


############################################################################################


"""
Q-11 : Write a function that, given a rational number whose integer part has at most 4 digits, checks if the hundreds digit of the integer part is even, and if so, determines whether the cube of that digit is a perfect square.
"""

def check_rational_square():
    user_input = input("Enter a rational numeber whose integer part has at most 4 digits:")
    integer_part = int((float(user_input)))
    hundreds = (integer_part // 100) % 10
    if hundreds % 2 == 0:
        cube = hundreds ** 3
        root = int(cube ** 0.5)

        if root * root == cube:
            return f"The cube of the hundreds digit ({hundreds}) of number {user_input} is a perfect square."
        else:
            return f"The cube of the hundreds digit ({hundreds}) of number {user_input} is not a perfect square."
    else:
        return f"The hundreds digit ({hundreds}) of number {user_input} is not even."
    

#print(check_rational_square())

############################################################################################

"""
Q-12 : Write a function that, given a positive rational number with a two-digit decimal part, determines whether the numeric value of the decimal part is a perfect square.
"""

def check_digit_square():
    user_input = input("Enter a positive rational number with two decimal places: ")
    num = float(user_input)
    
    # Extract decimal part as integer (two digits)
    decimal_part = int(round((num - int(num)) * 100))
    root = int(decimal_part ** 0.5)
    if decimal_part == root * root:
        return f"positive rational number with a two-digit decimal part {user_input} is square number" 
    else:
        return f"positive rational number with a two-digit decimal part {user_input} is not square number" 
    

#print(check_digit_square())


############################################################################################

"""
Q_13 : Write a function that, given a positive rational number with a two-digit decimal part, finds the distance of the integer value of the decimal part to the nearest perfect square number.
"""

def check_nearest_square():
    user_input = input("Enter a positive rational number with two decimal places: ")
    num = float(user_input)
    
    # Extract decimal part as integer (two digits)
    decimal_part = int(round((num - int(num)) * 100))
    
    square_list = [i * i for i in range(0, 11)]
    
    diff_list = [np.abs(decimal_part- sq) for sq in square_list]

    min_diff = min(diff_list)
    nearest_square = square_list[diff_list.index(min_diff)
                                 ]
    return  f" nearest point is {nearest_square} and diff is({min_diff})"


#print(check_nearest_square())

############################################################################################

"""
Q-14: Write a function that, given a positive rational number with a three-digit decimal part, 
checks whether the difference between the integer part and the integer value of the decimal part is positive, 
and if so, determines whether this difference is a perfect square.
"""


def diff_int_decimal():
    user_input = input("Enter a rational numeber whose decimal part has at most 3 digits:")
    integer_part = int((float(user_input)))

    num = float(user_input)
    
    # Extract decimal part as integer (three digits)
    decimal_part = int(round((num - int(num)) * 1000))

    diff = integer_part - decimal_part
    root = diff ** 0.5

    if diff > 0:
        root = int(diff ** 0.5)
        if root * root == diff:
            return f"rational numbers integer part minıus decimal part {diff} is perfect square"
        else:
            return f"rational numbers integer part minıus decimal part {diff} is not perfect square"

    else:
        return f"Difference {diff} is not positive, so condition not met."

#print(diff_int_decimal())


############################################################################################

"""
Q-15: Write a function that, given a randomly entered rational number, finds the number of digits in its decimal part and the number of digits in its integer part.
"""

def count_digits(num_str:str):
    splitted_num = str(num_str).split(".")
    count_integer = len(splitted_num[0])
    count_decimal = len(splitted_num[1]) if len(splitted_num) > 1 else 0

    return count_integer, count_decimal

#print(count_digits(13.4567))


############################################################################################

"""
Q-16 : Write a function that finds the largest digit in the digits of a given integer.
"""

def find_biggest_digit(num:int) -> int:
    return int(max((str(num))))

#print(find_biggest_digit(123))
#print(find_biggest_digit(4525425))
#print(find_biggest_digit(459))

############################################################################################

"""
Q-17 : Write a function that finds the repeating digits in the digits of a given integer.
"""

def repeating_digits(num:int) -> list[int]:
    repeats_dict = Counter(str(num))
    repeated_nums = []
    for key,value in repeats_dict.items():
        if value>1:
            repeated_nums.append(int(key))
    return repeated_nums

#print(repeating_digits(45566667))

############################################################################################

"""
Q-18 : Write a function that separates the digits of any given integer into a list.
"""

def split_to_digits(num:int) -> list:
    return [int(digit) for digit in str(num)]

#print(split_to_digits(45673234))

############################################################################################

"""
Q-19 : Write a function that takes input for a sequence of N numbers.
"""

def seq_to_list():
    n = int(input("Enter the number of elements (N):"))
    user_input = input(f"Enter {n} numbers seperated by spaces: ")
    numbers  = list(map(int,user_input.split()))
    
    if len(numbers) != n:
        print(f"Warning: Expected {n} numbers but got {len(numbers)}.")
    return numbers

#print(seq_to_list())

############################################################################################

"""
Q-20 : Write a function that finds the sum of the elements of a 10-element number sequence.
"""

def sum_of_ten_num_digits():
    n = 10
    user_input = input(f"Enter {n} numbers separated by spaces: ")
    numbers  = list(map(int,user_input.split()))
    

    if len(numbers) != n:
        print(f"Warning: Expected {n} numbers but got {len(numbers)}.")
    
    return sum(numbers)

#print(sum_of_ten_num_digits())


############################################################################################

"""
Q-21 : Write a function that finds the largest element in a 10-element number sequence.
"""


def max_of_ten_num_digits():
    n = 10
    user_input = input(f"Enter {n} numbers separated by spaces: ")
    numbers  = list(map(int,user_input.split()))
    

    if len(numbers) != n:
        print(f"Warning: Expected {n} numbers but got {len(numbers)}.")
    
    return max(numbers)

#print(max_of_ten_num_digits())

############################################################################################

"""
Q-22 : Write a function that finds the sum of the negative elements in a 10-element number sequence.
"""

def sum_neg_elements():
    n = 10
    user_input = input(f"Enter {n} numbers separated by spaces: ")
    numbers  = list(map(int,user_input.split()))
    
    if len(numbers) != n:
        print(f"Warning: Expected {n} numbers but got {len(numbers)}.")

    neg_sums = sum(num for num in numbers if num<0)

    return neg_sums


#print(sum_neg_elements())

############################################################################################

"""
Q-23: Write a function that finds the separate averages of the negative and positive elements in a 10-element number sequence.
"""

def sep_means():
    n = 10
    user_input = input(f"Enter {n} numbers separated by spaces: ")
    numbers  = list(map(int,user_input.split()))
    
    if len(numbers) != n:
        print(f"Warning: Expected {n} numbers but got {len(numbers)}.")

    neg_nums = [num for num in numbers if num<0]
    pos_nums = [num for num in numbers if num>0]

    neg_mean = mean(neg_nums) if neg_nums else None
    pos_mean = mean(pos_nums) if pos_nums else None

    return f" average of negative values is {neg_mean}, average of positive values is {pos_mean}"

#print(sep_means())


############################################################################################

"""
Q-24:  Write a function that counts the number of negative and positive elements in a number sequence of any length.
"""

def cnt_neg_pos():
    user_input = input(f"Enter numbers separated by spaces: ")
    numbers  = list(map(int,user_input.split()))

    neg_nums = [num for num in numbers if num < 0]
    pos_nums = [num for num in numbers if num > 0]


    return f"Count of negative numbers is {len(neg_nums)}, Count of positive numbers is {len(pos_nums)}"

#print(cnt_neg_pos())


############################################################################################

"""
Q-25: Write a function that, given a sequence A of 10 elements, loads the negative elements into a separate list and the positive elements into another separate list.
"""

def sep_neg_pos_elements():
    n = 10
    user_input = input(f"Enter {n} numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))

    if len(numbers) != n:
        print(f"Warning: Expected {n} numbers but got {len(numbers)}.")

    neg_nums = [num for num in numbers if num < 0]
    pos_nums = [num for num in numbers if num > 0]
    
    return f"Negative numbers is {neg_nums}, Positive numbers is {pos_nums}"

#print(sep_neg_pos_elements())

############################################################################################

"""
Q-26: Write a function that sorts a number sequence A of N elements in ascending order.
"""

def sorted_elements():
    user_input = input(f"Enter numbers separated by spaces: ")
    numbers = list(map(int,user_input.split()))
    return sorted(numbers)

#print(sorted_elements())


############################################################################################

"""
Q-27: Write a function that, given an ascending sorted sequence of N numbers, finds a desired number using binary search.
"""

def find_num_binary():
    user_input = input("Enter numbers separated by spaces in ascending order: ")
    desired_num = int(input("Enter your desired number to be found: "))
    numbers = list(map(int, user_input.split()))

    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == desired_num:
            return mid  # Found, return index
        elif numbers[mid] < desired_num:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found

#print(find_num_binary())

############################################################################################