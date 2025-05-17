import numpy as np
from collections import Counter

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

