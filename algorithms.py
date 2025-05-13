import numpy as np

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