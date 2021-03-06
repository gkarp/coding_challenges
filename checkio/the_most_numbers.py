'''
Mission 7: The Most Numbers
You are given an array of numbers (floats). You should find the difference 
between the maximum and minimum element. Your function should be able to 
handle an undefined amount of arguments. For an empty argument list, 
the function should return 0.

Floating-point numbers are represented in computer hardware as base 2 (binary) 
fractions. So we should check the result with +/- 0.001 precision.
Think about how to work with an arbitrary number of arguments.

Input: An arbitrary number of arguments as numbers (int, float).

Output: The difference between maximum and minimum as a number (int, float).
'''
def checkio(*args):
    try:
        num_list = []
        for number in args:
            num_list.append(number)
        return (num_list != []) * round(max(num_list), 3) - round(min(num_list), 3)
    except ValueError:
        return 0
    

    